import json
import sys
from pathlib import Path
import requests

API_URL = "https://api.meiji.su/audio-to-bars"


def send_audio_to_bars(
    file_path: str | Path, output_file: str | Path | None = None
) -> dict | None:
    path = Path(file_path)
    if not path.is_file():
        print(f"Error: File not found at {path}")
        return None

    with open(path, "rb") as f:
        files = {"file": (path.name, f)}
        response = requests.post(API_URL, files=files, timeout=60)

    print(f"Status Code: {response.status_code}")
    if response.ok:
        try:
            data = response.json()
            if output_file:
                out_path = Path(output_file)
                with open(out_path, "w", encoding="utf-8") as out_f:
                    json.dump(data, out_f, ensure_ascii=False, indent=2)
                print(f"Saved response to {out_path}")
            return data
        except ValueError:
            print("Response is not valid JSON:")
            print(response.text)
            return None
    else:
        print(f"Request failed: {response.status_code} {response.reason}")
        print(response.text)
        return None


if __name__ == "__main__":
    target_file = sys.argv[1] if len(sys.argv) > 1 else "ShadowShadow.m4a"
    out_file = sys.argv[2] if len(sys.argv) > 2 else None
    send_audio_to_bars(target_file, out_file)

