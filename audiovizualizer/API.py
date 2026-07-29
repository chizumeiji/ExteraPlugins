# ── Audio-to-Bars ────────────────────────────────────────────────────────

# это - фрагмент из апи, сам апи работает с большим кол-вом эндпоинтов и микросервисов, но этот фрагмент - отдельный модуль, некоторого рода гарантия прозрасности.

import os
import json
import hashlib
import tempfile
import subprocess
import logging
import warnings
from typing import List, Optional
from app.db import async_session, engine

import numpy as np
import librosa
from pydantic import BaseModel
from fastapi import FastAPI, Request, HTTPException, UploadFile, File
from sqlalchemy import text as sa_text

warnings.filterwarnings("ignore", category=UserWarning, module="librosa")
warnings.filterwarnings("ignore", category=FutureWarning, module="librosa")

logging.basicConfig(level=logging.INFO, format="%(asctime)s | %(levelname)s | %(message)s")
logger = logging.getLogger("api")

app = FastAPI(
    title="MG PROJECT Backend",
    docs_url=None,
    redoc_url=None,
    openapi_url=None
)

MAX_AUDIO_SIZE_BYTES = 30 * 1024 * 1024  # 30MB limit

class AudioBarsResponse(BaseModel):
    duration: float
    fps: int = 30
    frames: List[List[float]]

def compute_audio_bars(audio_bytes: bytes, fps: int = 30, num_bars: int = 30, sensitivity: float = 1.1) -> dict:
    with tempfile.NamedTemporaryFile(suffix=".tmp", delete=False) as tmp:
        tmp.write(audio_bytes)
        tmp_path = tmp.name

    try:
        process = subprocess.Popen(
            [
                "ffmpeg",
                "-y",
                "-i", tmp_path,
                "-f", "s16le",
                "-ac", "1",
                "-ar", "22050",
                "-loglevel", "error",
                "pipe:1"
            ],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        raw_pcm, stderr = process.communicate()
    finally:
        if os.path.exists(tmp_path):
            try:
                os.remove(tmp_path)
            except OSError:
                pass

    if process.returncode != 0 or not raw_pcm:
        err_msg = stderr.decode("utf-8", errors="ignore") if stderr else "Unknown ffmpeg error"
        raise ValueError(f"Failed to decode audio stream: {err_msg}")

    sr = 22050
    pcm_data = np.frombuffer(raw_pcm, dtype=np.int16).astype(np.float32) / 32768.0
    if len(pcm_data) == 0:
        raise ValueError("Decoded audio payload is empty")

    duration = round(len(pcm_data) / sr, 1)
    total_frames = int(round(duration * fps))
    if total_frames <= 0:
        total_frames = 1

    y_pre = librosa.effects.preemphasis(pcm_data, coef=0.97)

    S = librosa.feature.melspectrogram(y=y_pre, sr=sr, n_mels=num_bars, fmax=sr / 2.0)

    S_dB = librosa.power_to_db(S, ref=np.max)

    min_val = -30.0
    S_norm = np.clip((S_dB - min_val) / (0.0 - min_val), 0.0, 1.0)

    S_norm = np.power(S_norm, 1.2)

    tilt = np.linspace(1.0, 2.2, num_bars)[:, np.newaxis]
    S_norm = S_norm * tilt

    S_norm = np.clip(S_norm * sensitivity, 0.0, 1.0)

    hop_length = 512
    n_time_frames = S_norm.shape[1]

    frame_spectrums = []
    for f_idx in range(total_frames):
        t_rel = f_idx / fps
        col_idx = int(round(t_rel * sr / hop_length))
        col_idx = max(0, min(n_time_frames - 1, col_idx))
        frame_spectrums.append(S_norm[:, col_idx])

    frame_spectrums = np.array(frame_spectrums)
    smoothed = np.zeros_like(frame_spectrums)
    for f_idx in range(total_frames):
        sf = max(0, f_idx - 1)
        ef = min(total_frames, f_idx + 2)
        smoothed[f_idx] = np.mean(frame_spectrums[sf:ef], axis=0)

    frames_output = np.round(smoothed, 3).tolist()

    return {
        "duration": duration,
        "fps": fps,
        "frames": frames_output
    }

async def _ensure_audio_cache_table():
    async with engine.begin() as conn:
        await conn.execute(sa_text("""
            CREATE TABLE IF NOT EXISTS audio_bars_cache (
                file_unique_id VARCHAR(128) PRIMARY KEY,
                duration DOUBLE PRECISION NOT NULL,
                fps INTEGER NOT NULL DEFAULT 30,
                frames_json TEXT NOT NULL,
                created_at TIMESTAMPTZ NOT NULL DEFAULT now()
            )
        """))

@app.on_event("startup")
async def _on_startup():
    await _ensure_audio_cache_table()


async def _get_cached_bars(cache_key: str) -> Optional[dict]:
    try:
        async with async_session() as session:
            row = (await session.execute(
                sa_text("SELECT duration, fps, frames_json FROM audio_bars_cache WHERE file_unique_id = :fuid"),
                {"fuid": cache_key}
            )).first()
            if row:
                return {
                    "duration": row.duration,
                    "fps": row.fps,
                    "frames": json.loads(row.frames_json)
                }
    except Exception as exc:
        logger.warning(f"DB cache read error: {exc}")
    return None


async def _save_cached_bars(cache_key: str, bars_data: dict) -> None:
    try:
        async with async_session() as session:
            await session.execute(
                sa_text("""
                    INSERT INTO audio_bars_cache (file_unique_id, duration, fps, frames_json)
                    VALUES (:fuid, :dur, :fps, :frames)
                    ON CONFLICT (file_unique_id) DO UPDATE
                        SET duration = EXCLUDED.duration,
                            fps = EXCLUDED.fps,
                            frames_json = EXCLUDED.frames_json
                """),
                {
                    "fuid": cache_key,
                    "dur": bars_data["duration"],
                    "fps": bars_data["fps"],
                    "frames": json.dumps(bars_data["frames"]),
                }
            )
            await session.commit()
    except Exception as exc:
        logger.warning(f"DB cache write error: {exc}")


@app.post("/audio-to-bars", response_model=AudioBarsResponse)
async def audio_to_bars(
    request: Request,
    file: Optional[UploadFile] = File(None),
    fps: int = 30,
    num_bars: int = 30,
    sensitivity: float = 1.1
):
    if num_bars < 1 or num_bars > 250:
        raise HTTPException(status_code=400, detail="num_bars must be between 1 and 250")
    if fps < 1 or fps > 120:
        raise HTTPException(status_code=400, detail="fps must be between 1 and 120")
    if sensitivity <= 0 or sensitivity > 10.0:
        raise HTTPException(status_code=400, detail="sensitivity must be between 0.1 and 10.0")

    if file is not None:
        audio_bytes = await file.read()
    else:
        audio_bytes = await request.body()

    if not audio_bytes:
        raise HTTPException(status_code=400, detail="No audio file content provided")

    if len(audio_bytes) > MAX_AUDIO_SIZE_BYTES:
        raise HTTPException(status_code=400, detail=f"File size ({len(audio_bytes)} bytes) exceeds limit of 30MB")

    raw_hash = hashlib.sha256(audio_bytes).hexdigest()
    cache_key = hashlib.sha256(f"{raw_hash}_{fps}_{num_bars}_{sensitivity}".encode("utf-8")).hexdigest()

    cached = await _get_cached_bars(cache_key)
    if cached:
        logger.info(f"audio-to-bars cache HIT for key {cache_key[:12]}")
        return cached

    try:
        bars_data = compute_audio_bars(audio_bytes, fps=fps, num_bars=num_bars, sensitivity=sensitivity)
    except ValueError as val_err:
        logger.error(f"Audio processing error: {val_err}")
        raise HTTPException(status_code=400, detail=str(val_err))
    except Exception as exc:
        logger.error(f"Unexpected audio processing error: {exc}", exc_info=True)
        raise HTTPException(status_code=500, detail="Internal audio processing error")

    try:
        await _save_cached_bars(cache_key, bars_data)
        logger.info(f"audio-to-bars cache SAVED for key {cache_key[:12]}")
    except Exception as exc:
        logger.warning(f"Failed to save audio bars cache: {exc}")

    return bars_data