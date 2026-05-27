# плагин для работы с апи фанстат 
# автор: @chizumeij
# мой канал: @meijinolife
# разработка начата 4 марта 2026 года

# @@@@@@@@@@@@@@@@@@@@@@@@@@@#kW@=     .--::::-===+++++++++++++++++++++++++++++++++++++==e#W@@@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@@@@#=:W@@-     ....::--====++++=+++++++++++++++++++++++++++++++++++k$%@@@@@@@
# @@@@@@@@@@@@@@@@@@@@@@%k:  :@@@e       .....:::---======++++++++++++++++++++++++++++++++++k$k$W@@@@
# @@@@@@@@@@@@@@@@@@@@@k#W.   #%+.   ..       ...:::-----===++++++++++=+++++++++++++++++++++=+$#k$W@@
# @@@@@@@@@@@@@@@@@@@@k$@@-   ...-+k#k:        .....::::---========+++==++++++++++++++++++===--k#%k$W
# @@@@@@@@@@@@@@@@@@%= e@@#   .-k%WW%+-             .....:::---=======+==++++++++++++++++===-::-k@@%k
# @@@@@@@@@@@@@@@@@e   .#%e.:e$%WWW%e$.                 ....:::-----====-==++==+++=+=+=+==--::.+%@@@@
# @@@@@@@@@@@@@@@%e      :-k%WWWWWW$k@+                    ....:::::::--:---==-=======-----::..-#@@@@
# @@@@@@@@@@@@@@%k:     -k%WWWWWWW#e%@%                         .  ..:::::::-:::------:::::..=#W%k$kk
# @@@@@@@@@@@@@#%k  . :k%WWWWWWWW%#e@@@= .                           .......:.:.::::::....-$kkk-  .
# @@@@@@@@@@@@$#W- - =%WWWWWWWWWW#$e@@@$==--            .                    ........:-+kk-=:
# @@@@@@@@@@@#kW%e=.+WWWWWWWWWWW#%+$@@@$W$$= ... ...  . ..                         :---:.
# @@@@@@@@@@W=#%%k:+WWWWWWWWWWW%#%:$k+=e@@W=.::. .-:..   ...            :
# @@@@@@@@@@e-==e=-WWWWWWWWWWWW#%#.e::.-@@@=.::..:%e.........           -
# @@@@@@@@@W.   =:%WWWWWWWWWWWW$Wk.-::::#@W-::---+@%+.::........        :=
# @@@@@@@@@$    .kWWWWWWWWWWWW##W+:::--:-$#::::=-+@@#+-::...... ..:.    .e.
# @@@@@@@@@$:.  :WWWWWWWWWWWWW#WW=-:---:-++---:e=+@@W#k-:.::::....e-    :#-
# @@@@@@@@@#-   eWWWWWWWWWWWW%#W%-=:===:=-=--=-$+=W%$##k-::::...:.+e.   =W+
# @@@@@@@@@$:   #WWWWWWWWWWWW#%W%-=:===:====-==#e+$e-=kk+:::... ..-+:   +@k.
# @@@@@@@@@kk  .%WWWWW%#keeekk%W#-=:===-=====-e$k+e+-:-++-:::..  ..::   e@k-
# @@@@@@@@@kW. :WWWWWWWWWW%%#k%W#--=-++:=+===-k$%ek-=::---:-:::  ....   k@$=.
# @@@@@@@@@k@+ :WWWWWWWWWWWW%#WW$--k-++-=++===$##=e---:-------:.  ...   $W$+:
# @@@@@@@@@kWW..%WWWWWWWWWWW%#WW#--#+-+-=+++=e$%%$+k-=-------::-:  .   .#$e=:
# @@@@@@@@@#k%= k$$$#%WWWWWW%#WW#--%$-==-+++=$$%WWe%+--e-----:--+      :$=-::
# @@@@@@@@@@k$#+.=+==--+k#W%#$%%%=-%#k-=-++==$#WWW#k%=-+k-=----:$.     -e.  :
# @@@@@@@@@@@%%$.+@@W=...:=k$e$#%e-%###+:=+=e$%WWWWk%#-:$k----:-$+     =-  ..
# @@@@@@@@@@@@@$=-%@@$%#-  .+k$$%#=%%$W%+=+=$$##%WW%$W#-+#$=---:$$.    +.  ..
# @@@@@@@@@@@@@%kW#%W==%$-.::=#WWW#%%#WWW+==$kkk$%%W#%W%k$$#+:-:k#+   .=   :
# @@@@@@@@@@@@@#kWW%%#e$#$$$e=e%WWWWW%WWW%ekk+==--=+ee$%%%$#Wk::$$$.  ..   :    ..  .:--
# @@@@@@@@@@@@@$kWWWWWWWW%#$kk%WWWWWWWWWWWW%$k$#$$e:. .--=+k%W$:k##e       :    =e=e$$#$+
# @@@@@@@@@@@@@e$%%%%%%%WWWW%%%WWWWWWWWWWWWW@@@@@@W%#e:.=:..:-eek#$%:     ..    e$$$$e+++.
# @@@@@@@@@@@@@+$%%%###%%WWWW%##%%WWWWWWWWWWW@WWWW#-+kekk-.=+=---e$W$     :.   .$ke$kk$$$:
# @@@@@@@@@@@@@ek%%#####%%WW$k###%WWWWWWWWWWWW#$$$$kk$$##$kkkk$e::=#$     :    :k+kkkkkkk=
# @@@@@@@@@@@@@$eW%%###%%WWW%%WWWWWWWWWWWWWWWW%%%WWWW%%%###$$$$e$%#%+     :    +ee$$$ek#$k
# @@@@@@@@@@@@@W=WWWWWWWWWWWWWWWWWWWWWWW%W%%%%###%##%%%WW%%%W%%%WWWW-    ..    e+k#$$$$k$#-
# @@@@@@@@@@@@@@$eWWWWWWWWWWWWWWWWWWWWWW%%%%###%#%%%%%###%%%%WWWWWW%.    :    .ek$$$kkkk#k.
# @@@@@@@@@@@@@@@ekWWWWWWWWWWWWWWWWWWWWWWWWWWW%WW%%%###%%%%%%%%WWWW$     :    -kekkkk$$$e.
# @@@@@@@@@@@@@@@W+eWWWWWWWWW%%%%WWWWWWWWWWWWWWWWWWWWWWW%%%%WWWWWWW+     .    +$$$$$#$+:
# @@@@@@@@@@@@@@@%e :$WWWWWWW$.+W%####%%WWWWWWWWWWWWWWWWWWWWWWWWWW%.    ..   .$#$$$$e:
# @@@@@@@@@@@@@@@%e   =#WWWWWWk+%@@@@WW%####%WW%%W%%#k%WWWWWWWWWWWk     .    :=:::.
# @@@@@@@@@@@@@@@#+    .+%WWWWW#$#@@@@@@@@@W%%W%$kke+#WWWWWWWWWWWW:     .    +:
# @@@@@@@@@@@@@@W#=    . :$WWWWW%##%W@@@@@W%%$%$+=+$WWWWWWWWWWWW@$     ..   .$e-k$$e.          ......
# @@@@@@@@@@@@@@W#:    +-  =#WWWWWW%###%WW@@W%$$#%WWWWWWWWWWWWW#k:     ..   -##+..=$+         .::::::
# @@@@@@@@@@@@@@%#     k%.  .e%WWWWWWW%%%#WW%%WWWWWWWWWWWWW#k=:.:  .........+#$$e. +%+ :====:. :---::
# @@@@@@@@@@@@@@#k     $@#.   :$WWWWWWWWWWWWWWWWWWWW%#$k+-.  .-e- .::.::::..k$$$#ke#%%k+$%%%%#=.==---
# @@@@@@@@@@@@@W#+     %@@%-    +$%WWWWWWW%%##$k+=-:.      :+k$k  .::::::-:=$$$$ek%%%%%#==$%%%%e-====
# @@@@@@@@@@@@@%%-    .W@@@@#::$W#kk$$$$kek$#%#$e:     ..-ek$$#=  :------=:e#$ke$%%%%%%%%==e%%%We-+++
# @@@@@@@@@@@@@#%     :@@@@@#$@@@@@@@@@%#W@@@#%@@#=.-.:+k$$$$$k..::------=-$kek%%%%%%%%%%+k=$WWWWk=++
# @@@@@@@@@@@@W%$     =@@@@$$@@@@@@@@@##@@@W$W@##%%e+k$$$$$$$#= =---------=e+#%%%%%%%%%%$+WkkWWW@@%kk

import time
import re
from collections import OrderedDict
import traceback
import threading
from datetime import datetime
from typing import Any, List

import requests

from java.util import ArrayList
from android_utils import log, run_on_ui_thread
from base_plugin import BasePlugin, HookResult, HookStrategy
from ui.settings import Header, Input, Divider, Selector

__id__ = "funstat"
__name__ = "Funstat"
__description__ = (
    "Работает с API funstat без сторонних ботов.\n"
    "для работы нужен токен подробнее: .fs help\n\n"
    "Works with funstat API without third-party bots.\n"
    "token is required details: .fs help"
)
__author__ = "@chizumeij"
__version__ = "3.7.0"
__icon__ = "MeijiPlugins/1"
__min_version__ = "11.12.0"

STRINGS: dict[str, dict[str, str]] = {
    "ru": {
        "help_title":    "📊 Funstat — справка",
        "help_user":     "👤 Пользователь (-u юзер)",
        "help_group":    "💬 Группа (-g группа)",
        "help_other":    "🔧 Прочее",
        "help_flags":    "🏳️ Флаги",
        "help_flag_s":   "-s — отправить результат в чат",
        "help_flag_p":   "-p N — страница",
        "help_flag_f":   "-f текст — фильтр сообщений (можно несколько слов)",
        "help_flag_t":   "-t sent|recv|mutual — фильтр подарков",
        "cmd_ping":      "ping — задержка сервера",
        "cmd_balance":   "balance — баланс API",
        "cmd_sm":        "sm [юзер] — базовая стата",
        "cmd_s":         "s [юзер] — полная стата",
        "cmd_chats":     "chats [юзер] — чаты",
        "cmd_names":     "names [юзер] — история имён",
        "cmd_us":        "us [юзер] — история юзернеймов",
        "cmd_msg":       "msg [юзер] [-f текст] [-p N] — сообщения",
        "cmd_gc":        "gc [юзер] — кол-во групп",
        "cmd_mc":        "mc [юзер] — кол-во сообщений",
        "cmd_rep":       "rep [юзер] — репутация",
        "cmd_cg":        "cg [юзер] — общие чаты",
        "cmd_sticks":    "sticks [юзер] — стикеры",
        "cmd_gifts":     "gifts [юзер] [-t sent|recv|mutual] — подарки",
        "cmd_uu":        "uu [юзернейм] — где использовался",
        "cmd_gi":        "gi [группа] — инфо о группе",
        "cmd_gm":        "gm [группа] — участники группы",
        "cmd_cgf":       "cgf [юзер1] [юзер2] [юзер3 ...] — общие группы",
        "cmd_st":        "st [запрос] — поиск текста",
        "cmd_bi":        "bi [юзер] — инфо по ID",
        "tpl_sm": (
            "ㅤЭто <a href=\"tg://openmessage?user_id={id}\">{first_name}</a>\n"
            "ID: <code>{id}</code>\n"
            "С <b>{first_msg_date}</b>\n"
            "<b>{total_msg_count}</b> сообщ. в <b>{msg_in_groups_count}</b> чатах\n"
            "Всего чатов: <b>{total_groups}</b>\nАдмин в чатах: <b>{adm_in_groups}</b>\n"
            "Юзернеймов: <b>{usernames_count}</b>\nИмён: <b>{names_count}</b>\n\n"
            "Последнее обновление: <b>{last_msg_date}</b>"
        ),
        "tpl_s": (
            "ㅤЭто <a href=\"tg://openmessage?user_id={id}\">{first_name}</a>\n"
            "ID: <code>{id}</code>\n\n"
            "Разнообразие сообщ. <b>{unique_percent}</b>\n"
            "С <b>{first_msg_date}</b> по <b>{last_msg_date}</b>\n"
            "<b>{total_msg_count}</b> сообщ. в <b>{msg_in_groups_count}</b> чатах\n"
            "Всего чатов: <b>{total_groups}</b>\n"
            "<b>{reply_percent}</b> реплаи <b>{media_percent}</b> медиа\n"
            "Кружки: <b>{circle_count}</b>  Голос: <b>{voice_count}</b>\n"
            "Ссылки: <b>{link_percent}</b>\n"
            "Любимый чат: {favorite_chat_title}\n"
            "Админ в <b>{adm_in_groups}</b> чатах\n\n"
            "Юзернеймов: <b>{usernames_count}</b>  Имён: <b>{names_count}</b>\n"
            "{stars_line}{about_line}"
        ),
        "tpl_ping":    "⏱ request: <b>{request_ping}</b>ms\n⏱ response: <b>{responce_ping}</b>ms",
        "tpl_balance": "Баланс: <b>{current_ballance}</b> 💠",
        "tpl_rep": (
            "ㅤРепутация <a href=\"tg://openmessage?user_id={user_id}\">{first_name}</a>: <b>{reputation_name}</b>\n"
            "✅ <b>{positive_count}</b> | ❌ <b>{negative_count}</b> | всего: <b>{num_votes}</b>\n"
            "Анонимных: <b>{anon_votes_count}</b>\n"
            "Последний: <b>{last_time}</b>"
        ),
        "no_data":              "нет данных",
        "unknown_cmd":          "❓ Неизвестная команда: {cmd}\nПомощь: .fs help",
        "need_u":               "⚠️ Укажи -u юзер",
        "need_g":               "⚠️ Укажи -g группа",
        "need_q":               "⚠️ Укажи -q запрос",
        "error":                "❌ Ошибка: <code>{err}</code>",
        "chats_header":         "👮-адм  🔒-приват  ✖-вышел\nПерв. | Посл. — чат (сообщений)",
        "usernames_header":     "Юзернеймы:",
        "names_header":         "Имена:",
        "messages_header":      "Сообщения: [R]-ответ  📢-канал",
        "common_groups_header": "Общие чаты:",
        "stickers_header":      "Стикеры:",
        "gifts_header":         "Подарки:  ⬅️получил  ➡️отдал  ↔️взаимно",
        "group_info_header":    "Группа:",
        "group_members_header": "Участники ({count}):",
        "usage_header":         "Использование @{username}:",
        "usage_current":        "Текущий пользователь:",
        "usage_past":           "Ранее использовали:",
        "usage_groups":         "Группы/каналы:",
        "cgf_header":           "Общие группы {users}:",
        "search_header":        "Поиск «{q}» — {total} результатов:",
        "stars":                "⭐ Stars: {val}  ур. {level}",
        "about":                "Bio: {about}",
        "btn_profile":          "👤 Профиль",
        "btn_names":            "📝 Имена",
        "btn_groups":           "💬 Группы",
        "btn_messages":         "✉️ Сообщения",
        "btn_reputation":       "⭐ Репутация",
        "btn_common":           "🤝 Общие",
        "btn_gifts":            "🎁 Подарки",
        "search_in_funstat":    "🔍 Найти в Funstat",
        "page_info":            "Стр. {page} / {total}",
        "pages_loaded":         "↓{loaded}/{total_pg}стр",
        "btn_refresh":          "🔄",
        "loading_page":         "⏳ Загрузка страницы...",
        "loading_init":         "⏳ Запрос выполняется, ждите...",
        "resolving_id":         "Вычисляю... ",
        "hidden_user":          "👻 Пользователь скрыт или не найден",
        "user_not_found":       "🔍 Пользователь не найден",
        "error_403":            "🔒 Пользователь скрыт (403)",
        "btn_goto_page":        "🔍",
        "goto_page_hint":       "№ страницы",
        "gifts_filter_all":     "Все",
        "gifts_filter_sent":    "➡️ Отправил",
        "gifts_filter_recv":    "⬅️ Получил",
        "gifts_filter_mutual":  "↔️ Взаимно",
        "btn_names_add":        "➕",
        "btn_usernames_copy":   "📋",
        "history_title":        "История поисков",
        "history_empty":        "История пуста",
        "cache_stats_title":    "📦 Статистика кеша",
        "cache_users":          "Пользователи: {n}",
        "cache_hidden":         "  Скрытых: {n}",
        "cache_total":          "Записей всего: {n}",
        "cache_weight":         "Вес: ~{kb} КБ",
        "cache_cleared_at":     "Очищен: {dt}",
        "cache_stores":         "Сторов: {n}",
        "evicted_back_profile": "← Назад к профилю",
        "btn_evict_cache":      "🗑 Удалить из кеша",
        "cache_evicted":        "✅ Кеш пользователя {uid} очищен",
        "cache_cleared":        "✅ Весь кеш очищен",
        "cache_stats":          "📦 Кеш: {stats}",
        "btn_retry":            "🔄 Повторить",
        "btn_evict_and_retry":  "🗑 Очистить кеш",
        "btn_back":             "← Назад",
        "btn_close":            "Закрыть",
        "tpl_gc":               "Групп: {count}",
        "tpl_mc":               "Сообщений: {count}",
    },
    "en": {
        "help_title":    "📊 Funstat — help",
        "help_user":     "👤 User (-u user)",
        "help_group":    "💬 Group (-g group)",
        "help_other":    "🔧 Other",
        "help_flags":    "🏳️ Flags",
        "help_flag_s":   "-s — send result to chat",
        "help_flag_p":   "-p N — page",
        "help_flag_f":   "-f text — message filter (multiple words supported)",
        "help_flag_t":   "-t sent|recv|mutual — gifts filter",
        "cmd_ping":      "ping — server latency",
        "cmd_balance":   "balance — API balance",
        "cmd_sm":        "sm [user] — basic stats",
        "cmd_s":         "s [user] — full stats",
        "cmd_chats":     "chats [user] — chats list",
        "cmd_names":     "names [user] — name history",
        "cmd_us":        "us [user] — username history",
        "cmd_msg":       "msg [user] [-f text] [-p N] — messages",
        "cmd_gc":        "gc [user] — groups count",
        "cmd_mc":        "mc [user] — messages count",
        "cmd_rep":       "rep [user] — reputation",
        "cmd_cg":        "cg [user] — common groups",
        "cmd_sticks":    "sticks [user] — sticker packs",
        "cmd_gifts":     "gifts [user] [-t sent|recv|mutual] — gifts",
        "cmd_uu":        "uu [username] — usage history",
        "cmd_gi":        "gi [group] — group info",
        "cmd_gm":        "gm [group] — group members",
        "cmd_cgf":       "cgf [user1] [user2] [user3 ...] — common groups",
        "cmd_st":        "st [query] — search text",
        "cmd_bi":        "bi [user] — basic info by ID",
        "tpl_sm": (
            "ㅤThis is <a href=\"tg://openmessage?user_id={id}\">{first_name}</a>\n"
            "ID: <code>{id}</code>\n"
            "Since {first_msg_date}\n"
            "{total_msg_count} msgs in {msg_in_groups_count} chats\n"
            "Total chats: {total_groups}\nAdmin in: {adm_in_groups}\n"
            "Usernames: {usernames_count}\nNames: {names_count}\n\n"
            "Last updated: {last_msg_date}"
        ),
        "tpl_s": (
            "ㅤThis is <a href=\"tg://openmessage?user_id={id}\">{first_name}</a>\n"
            "ID: <pre>{id}</pre>\n\n"
            "Uniqueness {unique_percent}\n"
            "From {first_msg_date} to {last_msg_date}\n"
            "{total_msg_count} msgs in {msg_in_groups_count} chats\n"
            "Total chats: {total_groups}\n"
            "{reply_percent} replies {media_percent} media\n"
            "Circles: {circle_count}  Voice: {voice_count}\n"
            "Links: {link_percent}\n"
            "Fav chat: {favorite_chat_title}\n"
            "Admin in {adm_in_groups} chats\n\n"
            "Usernames: {usernames_count}  Names: {names_count}\n"
            "{stars_line}{about_line}"
        ),
        "tpl_ping":    "⏱ request: {request_ping}ms\n⏱ response: {responce_ping}ms",
        "tpl_balance": "Balance: {current_ballance} 💠",
        "tpl_rep": (
            "Reputation <a href=\"tg://openmessage?user_id={user_id}\">{first_name}</a>: {reputation_name}\n"
            "✅ {positive_count}  ❌ {negative_count}  total: {num_votes}\n"
            "Anonymous: {anon_votes_count}\n"
            "Last: {last_time}"
        ),
        "no_data":              "no data",
        "unknown_cmd":          "❓ Unknown command: {cmd}\nHelp: .fs help",
        "need_u":               "⚠️ Specify -u user",
        "need_g":               "⚠️ Specify -g group",
        "need_q":               "⚠️ Specify -q query",
        "error":                "❌ Error: {err}",
        "chats_header":         "👮-admin  🔒-private  ✖-left\nFirst | Last — chat (messages)",
        "usernames_header":     "Usernames:",
        "names_header":         "Names:",
        "messages_header":      "Messages: [R]-reply  📢-channel",
        "common_groups_header": "Common groups:",
        "stickers_header":      "Sticker packs:",
        "gifts_header":         "Gifts:  ⬅️received  ➡️sent  ↔️mutual",
        "group_info_header":    "Group:",
        "group_members_header": "Members ({count}):",
        "usage_header":         "Usage of @{username}:",
        "usage_current":        "Current user:",
        "usage_past":           "Used in the past:",
        "usage_groups":         "Groups/channels:",
        "cgf_header":           "Common groups of {users}:",
        "search_header":        "Search «{q}» — {total} results:",
        "stars":                "⭐ Stars: {val}  lv.{level}",
        "about":                "Bio: {about}",
        "btn_profile":          "👤 Profile",
        "btn_names":            "📝 Names",
        "btn_groups":           "💬 Groups",
        "btn_messages":         "✉️ Messages",
        "btn_reputation":       "⭐ Reputation",
        "btn_common":           "🤝 Common",
        "btn_gifts":            "🎁 Gifts",
        "search_in_funstat":    "🔍 Search in Funstat",
        "page_info":            "Page {page} / {total}",
        "pages_loaded":         "↓{loaded}/{total_pg}pg",
        "btn_refresh":          "🔄",
        "loading_page":         "⏳ Loading page...",
        "loading_init":         "⏳ Please wait...",
        "resolving_id":         "Resolving... ",
        "hidden_user":          "👻 User is hidden or not found",
        "user_not_found":       "🔍 User not found",
        "error_403":            "🔒 User is hidden (403)",
        "btn_goto_page":        "🔍",
        "goto_page_hint":       "Page #",
        "gifts_filter_all":     "All",
        "gifts_filter_sent":    "➡️ Sent",
        "gifts_filter_recv":    "⬅️ Received",
        "gifts_filter_mutual":  "↔️ Mutual",
        "btn_names_add":        "➕",
        "btn_usernames_copy":   "📋",
        "history_title":        "Search history",
        "history_empty":        "History is empty",
        "cache_stats_title":    "📦 Cache statistics",
        "cache_users":          "Users: {n}",
        "cache_hidden":         "  Hidden: {n}",
        "cache_total":          "Entries total: {n}",
        "cache_weight":         "Size: ~{kb} KB",
        "cache_cleared_at":     "Cleared: {dt}",
        "cache_stores":         "Stores: {n}",
        "evicted_back_profile": "← Back to profile",
        "btn_evict_cache":      "🗑 Remove from cache",
        "cache_evicted":        "✅ Cache for user {uid} cleared",
        "cache_cleared":        "✅ All cache cleared",
        "cache_stats":          "📦 Cache: {stats}",
        "btn_retry":            "🔄 Retry",
        "btn_evict_and_retry":  "🗑 Clear cache",
        "btn_back":             "← Back",
        "btn_close":            "Close",
        "tpl_gc":               "Groups: {count}",
        "tpl_mc":               "Messages: {count}",
    },
}

RU_MONTHS = {
    1: "Янв", 2: "Фев", 3: "Мар", 4: "Апр",
    5: "Май", 6: "Июн", 7: "Июл", 8: "Авг",
    9: "Сен", 10: "Окт", 11: "Ноя", 12: "Дек",
}

BASE_URL      = "https://funstat.in/api/v1"
INITIAL_BATCH = 200


def _t(lang: str, key: str, **kw) -> str:
    s = STRINGS.get(lang, STRINGS["ru"]).get(key, key)
    return s.format(**kw) if kw else s

_HIDDEN_SENTINEL    = -1
_NOT_FOUND_SENTINEL = -2

class _UserCache:
    def __init__(self):
        self._d: dict[str, int] = {}
        self._lock = threading.Lock()

    def get(self, key: str) -> int | None:
        with self._lock:
            return self._d.get(str(key).lower())

    def put(self, key: str, uid: int) -> None:
        with self._lock:
            k = str(key).lower()
            self._d[k]        = uid
            self._d[str(uid)] = uid

    def put_hidden(self, key: str) -> None:
        with self._lock:
            self._d[str(key).lower()] = _HIDDEN_SENTINEL

    def put_not_found(self, key: str) -> None:
        with self._lock:
            self._d[str(key).lower()] = _NOT_FOUND_SENTINEL

    def is_hidden(self, key: str) -> bool:
        with self._lock:
            return self._d.get(str(key).lower()) == _HIDDEN_SENTINEL

    def is_not_found(self, key: str) -> bool:
        with self._lock:
            return self._d.get(str(key).lower()) == _NOT_FOUND_SENTINEL

    def evict(self, uid: int) -> None:
        with self._lock:
            uid_s = str(uid)
            dead  = [k for k, v in self._d.items() if v == uid or k == uid_s]
            for k in dead:
                del self._d[k]

    def clear(self):
        with self._lock:
            self._d.clear()

    def size(self) -> int:
        with self._lock:
            return len({v for v in self._d.values() if v != _HIDDEN_SENTINEL and v != _NOT_FOUND_SENTINEL})

    def hidden_count(self) -> int:
        with self._lock:
            return sum(1 for v in self._d.values() if v == _HIDDEN_SENTINEL)

_user_cache = _UserCache()

class _RangeCache:
    def __init__(self, max_size: int = 2000):
        self.max_size     = max_size
        self.last_cleared: float = time.time()
        self._d: OrderedDict = OrderedDict()
        self._lock           = threading.Lock()

    def _make_key(self, path: str, params: dict) -> tuple:
        def norm(v):
            if isinstance(v, list):
                return tuple(sorted(str(x) for x in v))
            return v
        return (path, frozenset((k, norm(v)) for k, v in (params or {}).items()))

    def get(self, path: str, params: dict):
        key = self._make_key(path, params)
        with self._lock:
            if key not in self._d:
                return None
            self._d.move_to_end(key)
            return self._d[key]

    def put(self, path: str, params: dict, data) -> None:
        key = self._make_key(path, params)
        with self._lock:
            if key in self._d:
                self._d.move_to_end(key)
            else:
                if len(self._d) >= self.max_size:
                    self._d.popitem(last=False)
            self._d[key] = data

    def evict_prefix(self, path_prefix: str) -> int:
        with self._lock:
            dead = [k for k in self._d if str(k[0]).startswith(path_prefix)]
            for k in dead:
                del self._d[k]
            return len(dead)

    def clear(self) -> None:
        with self._lock:
            self._d.clear()
            self.last_cleared = time.time()

    def size(self) -> int:
        with self._lock:
            return len(self._d)

    def size_bytes(self) -> int:
        import json as _json
        total = 0
        with self._lock:
            for v in self._d.values():
                try:
                    total += len(_json.dumps(v, ensure_ascii=False))
                except Exception:
                    total += 64
        return total

    def set_max_size(self, n: int) -> None:
        with self._lock:
            self.max_size = max(1, n)
            while len(self._d) > self.max_size:
                self._d.popitem(last=False)

    def categorized_stats(self) -> dict:
        cats = {
            "stats_min":  0, "stats":       0, "messages":  0,
            "names":      0, "usernames":   0, "groups":    0,
            "gifts":      0, "stickers":    0, "reputation":0,
            "search":     0, "other":       0,
        }
        with self._lock:
            for key in self._d:
                path = str(key[0])
                if "stats_min" in path:      cats["stats_min"]  += 1
                elif "stats" in path:        cats["stats"]       += 1
                elif "messages" in path:     cats["messages"]    += 1
                elif "names" in path:        cats["names"]       += 1
                elif "usernames" in path:    cats["usernames"]   += 1
                elif "groups" in path or "common_group" in path:
                                             cats["groups"]      += 1
                elif "gifts" in path:        cats["gifts"]       += 1
                elif "stickers" in path:     cats["stickers"]    += 1
                elif "reputation" in path:   cats["reputation"]  += 1
                elif "search" in path:       cats["search"]      += 1
                else:                        cats["other"]       += 1
        return cats

    def stats(self) -> str:
        with self._lock:
            return f"entries={len(self._d)} max={self.max_size}"

_api_cache = _RangeCache(max_size=2000)

_search_history: list = []
_SEARCH_HISTORY_MAX  = 100
_search_history_lock = threading.Lock()

_HISTORY_SKIP = {".fs help", ".fs ping", ".fs balance", ".fs history"}

def _add_to_history(cmd: str) -> None:
    base = _strip_page_static(cmd)
    if not base:
        return
    for skip in _HISTORY_SKIP:
        if base.startswith(skip):
            return
    with _search_history_lock:
        if base in _search_history:
            _search_history.remove(base)
        _search_history.insert(0, base)
        if len(_search_history) > _SEARCH_HISTORY_MAX:
            _search_history.pop()

def _strip_page_static(text: str) -> str:
    return re.sub(r"\s+-p\s+\d+", "", text).strip()

class PaginatedStore:
    MAX_PAGES = 200

    def __init__(self, key: str, page_size: int, total_known: int = -1):
        self.key          = key
        self.page_size    = max(1, page_size)
        self.pages: dict  = {}
        self.total_known  = total_known
        self.exhausted    = False
        self.loaded_pages: set  = set()
        self.inflight: dict     = {}
        self._seen_ids: set     = set()
        self._lru: OrderedDict  = OrderedDict()
        self.fetcher            = None
        self._lock              = threading.Lock()

    def reset(self):
        with self._lock:
            self.pages        = {}
            self.exhausted    = False
            self.loaded_pages = set()
            self.inflight     = {}
            self._seen_ids    = set()
            self._lru         = OrderedDict()

    def store_page(self, page: int, items: list,
                   api_total: int | None = None,
                   is_exhausted: bool = False) -> int:
        with self._lock:
            deduped = []
            for item in items:
                item_id = (item.get("id") or item.get("messageId")
                           or item.get("message_id") or item.get("user_id"))
                if item_id is not None:
                    if item_id in self._seen_ids:
                        continue
                    self._seen_ids.add(item_id)
                deduped.append(item)

            self.pages[page] = deduped
            self.loaded_pages.add(page)

            self._lru[page] = True
            self._lru.move_to_end(page)

            while len(self._lru) > self.MAX_PAGES:
                oldest, _ = self._lru.popitem(last=False)
                self.pages.pop(oldest, None)
                self.loaded_pages.discard(oldest)

            if api_total is not None and api_total >= 0 and self.total_known < 0:
                self.total_known = api_total

            if is_exhausted:
                self.exhausted = True
                if self.total_known < 0:
                    self.total_known = (page - 1) * self.page_size + len(deduped)

            total_items = sum(len(v) for v in self.pages.values())
            _log_args = (self.key[:40], page, len(deduped), len(items),
                         len(self.loaded_pages), total_items,
                         self.total_known, self.exhausted)

        log(f"[funstat] store[{_log_args[0]}] store_page: "
            f"pg={_log_args[1]} +{_log_args[2]}/{_log_args[3]} "
            f"pages_in_mem={_log_args[4]} total_items≈{_log_args[5]} "
            f"total_known={_log_args[6]} exhausted={_log_args[7]}")
        return len(deduped)

    def add_items(self, new_items: list, api_total: int | None = None,
                  page: int | None = None, is_exhausted: bool = False) -> int:
        if page is not None:
            return self.store_page(page, new_items, api_total, is_exhausted)
        ps    = self.page_size
        added = 0
        for i in range(0, max(1, len(new_items)), ps):
            p      = (i // ps) + 1
            chunk  = new_items[i:i + ps]
            ch_ex  = is_exhausted and (i + ps >= len(new_items))
            added += self.store_page(p, chunk,
                                     api_total if i == 0 else None,
                                     is_exhausted=ch_ex)
        if not new_items and is_exhausted:
            with self._lock:
                self.exhausted = True
        return added

    def set_total(self, total: int):
        with self._lock:
            self.total_known = total

    def mark_loaded(self, page: int):
        with self._lock:
            self.loaded_pages.add(page)

    def total_pages(self) -> int:
        with self._lock:
            ps    = self.page_size
            total = self.total_known if self.total_known >= 0 else (
                max(self.loaded_pages) * ps if self.loaded_pages else 0
            )
            return max(1, (total + ps - 1) // ps)

    def has_page_data(self, page: int) -> bool:
        with self._lock:
            return page in self.loaded_pages

    def is_inflight(self, page: int) -> bool:
        with self._lock:
            return page in self.inflight

    def set_inflight(self, page: int, value: bool):
        with self._lock:
            if value:
                self.inflight[page] = True
            else:
                self.inflight.pop(page, None)

    def get_page(self, page: int) -> list:
        with self._lock:
            return list(self.pages.get(page, []))

    @property
    def items(self) -> list:
        with self._lock:
            result = []
            for p in sorted(self.pages.keys()):
                result.extend(self.pages[p])
            return result

    def get_all_items_for_sets(self) -> list:
        with self._lock:
            return [item for p in sorted(self.pages.keys()) for item in self.pages[p]]

    def is_fresh(self) -> bool:
        with self._lock:
            return len(self.loaded_pages) > 0 or self.exhausted

    def resize(self, new_page_size: int) -> None:
        new_ps = max(1, new_page_size)
        if new_ps == self.page_size:
            return

        with self._lock:
            if new_ps == self.page_size:
                return
            old_ps = self.page_size
            flat = [item for p in sorted(self.pages.keys()) for item in self.pages[p]]

        log(f"[funstat] store[{self.key[:40]}] resize: {old_ps} → {new_ps}, {len(flat)} items")

        new_pages: dict      = {}
        new_loaded: set      = set()
        new_lru: OrderedDict = OrderedDict()
        new_seen: set        = set()

        for i in range(0, max(1, len(flat)), new_ps):
            p     = (i // new_ps) + 1
            chunk = flat[i:i + new_ps]
            if not chunk:
                break
            new_pages[p] = chunk
            new_loaded.add(p)
            new_lru[p] = True

        for pg_items in new_pages.values():
            for item in pg_items:
                iid = (item.get("id") or item.get("messageId")
                       or item.get("message_id") or item.get("user_id"))
                if iid is not None:
                    new_seen.add(iid)

        last_len = len(new_pages[max(new_loaded)]) if new_loaded else 0
        new_exhausted = (last_len < new_ps) if new_loaded else False

        with self._lock:
            self.page_size    = new_ps
            self.pages        = new_pages
            self.loaded_pages = new_loaded
            self._lru         = new_lru
            self._seen_ids    = new_seen
            self.inflight     = {}
            self.exhausted    = new_exhausted

        log(f"[funstat] store[{self.key[:40]}] resize done: "
            f"{len(new_loaded)} pages, {len(flat)} items, "
            f"exhausted={new_exhausted} seen={len(new_seen)}")


_stores: dict[str, PaginatedStore] = {}
_stores_lock      = threading.Lock()
_stores_last_used: dict[str, float] = {}
_STORE_TTL        = 1800.0

_stores_get_counter = 0


def _evict_stale_stores() -> None:
    now  = time.time()
    dead = [k for k, ts in _stores_last_used.items() if now - ts > _STORE_TTL]
    for k in dead:
        _stores.pop(k, None)
        _stores_last_used.pop(k, None)
    if dead:
        log(f"[funstat] evicted {len(dead)} stale stores, {len(_stores)} remain")


def _get_store(key: str, page_size: int,
               reset: bool = False,
               total_known: int = -1) -> PaginatedStore:
    with _stores_lock:
        global _stores_get_counter
        _stores_get_counter += 1
        if _stores_get_counter % 200 == 0 and len(_stores) > 10:
            _evict_stale_stores()

        _stores_last_used[key] = time.time()

        if key not in _stores:
            _stores[key] = PaginatedStore(key, page_size, total_known)
        else:
            st = _stores[key]
            if reset:
                st.page_size = max(1, page_size)
                st.reset()
            elif st.page_size != max(1, page_size):
                st.resize(page_size)
            if total_known >= 0 and not reset:
                st.total_known = total_known
        return _stores[key]

_USER_AGENT = "Mozilla/5.0 (Linux; Android 14; Pixel 8) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36"

_EXTRA_HEADERS = {
    "Accept":          "application/json",
    "Accept-Language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
    "Referer":         "https://funstat.in/swagger/index.html",
    "Sec-Fetch-Dest":  "empty",
    "Sec-Fetch-Mode":  "cors",
    "Sec-Fetch-Site":  "same-origin",
    "Priority":        "u=0",
    "Connection": "keep-alive",
}

_REQUEST_TIMEOUT = 10


class FunstatClient:
    def __init__(self, token: str) -> None:
        self.token    = token
        self._session = requests.Session()
        self._session.headers.update({
            "Authorization": f"Bearer {token}",
            **_EXTRA_HEADERS,
        })

    _NO_CACHE: set = set()
    _LIVE_ONLY: set = {"users/resolve_username"}

    def _get(self, path: str, use_cache: bool = True, **params) -> dict | None:
        url        = f"{BASE_URL}/{path.lstrip('/')}"
        params_log = {k: v for k, v in params.items() if k != "Authorization"}

        if use_cache and path not in self._LIVE_ONLY:
            cached = _api_cache.get(path, params)
            if cached is not None:
                log(f"[funstat] CACHE HIT {path}  params={params_log}")
                return cached

        log(f"[funstat] → GET {path}  params={params_log}")
        t0    = time.time()
        delay = 1.0
        for attempt in range(3):
            try:
                headers = {"User-Agent": _USER_AGENT}
                r       = self._session.get(url, params=params or None,
                                            headers=headers, timeout=_REQUEST_TIMEOUT)
                elapsed = round((time.time() - t0) * 1000)
                if r.status_code == 200:
                    data = r.json()
                    if use_cache and path not in self._LIVE_ONLY:
                        _api_cache.put(path, params, data)
                    if isinstance(data, dict):
                        log(f"[funstat] ← 200 {path}  [{elapsed}ms]  keys={list(data.keys())[:6]}")
                    else:
                        log(f"[funstat] ← 200 {path}  [{elapsed}ms]  type={type(data).__name__}")
                    return data
                elif r.status_code == 403:
                    log(f"[funstat] ← 403 {path}  [{elapsed}ms]  (hidden user)")
                    return {"error": 403, "hidden": True}
                elif r.status_code in (500, 502, 503, 504) and attempt < 2:
                    log(f"[funstat] ← {r.status_code} {path}  [{elapsed}ms]  retry {attempt+1}")
                    time.sleep(delay); delay *= 2
                    continue
                else:
                    log(f"[funstat] ← ERROR {r.status_code} {path}  [{elapsed}ms]")
                    return {"error": r.status_code}
            except Exception as e:
                elapsed = round((time.time() - t0) * 1000)
                is_timeout = "timed out" in str(e).lower() or "timeout" in str(e).lower()
                if attempt < 2:
                    log(f"[funstat] ← EXCEPTION {path}  [{elapsed}ms]  {e}  retry {attempt+1}")
                    time.sleep(delay); delay *= 2
                    continue
                log(f"[funstat] ← EXCEPTION {path}  [{elapsed}ms]  {e} (no more retries)")
                return {"error": "⏱ timeout" if is_timeout else str(e)}
        return {"error": "max retries exceeded"}

    def resolve_user(self, user, on_resolved=None) -> int | None:
        raw   = str(user).strip()
        clean = raw.lstrip("@")
        clean = re.sub(r"^(?:https?://)?(?:www\.)?t\.me/", "", clean).split("/")[0]

        if clean.lstrip("-").isdigit():
            uid = int(clean)
            _user_cache.put(clean, uid)
            log(f"[funstat] resolve_user({raw}) → numeric {uid}")
            return uid

        if _user_cache.is_hidden(clean):
            log(f"[funstat] resolve_user({raw}) → cached hidden")
            return None

        if _user_cache.is_not_found(clean):
            log(f"[funstat] resolve_user({raw}) → cached not found")
            return None

        cached = _user_cache.get(clean)
        if cached is not None:
            log(f"[funstat] resolve_user({raw}) → cache hit {cached}")
            return cached

        log(f"[funstat] resolve_user({raw}) → cache miss, resolving via API")

        try:
            from org.telegram.tgnet import TLRPC, ConnectionsManager
            from org.telegram.messenger import UserConfig
            account = UserConfig.selectedAccount
            req = TLRPC.TL_contacts_resolveUsername()
            req.username = clean
            _event   = threading.Event()
            _mtproto = [None]

            def _cb(response, error, _e=_event, _r=_mtproto):
                try:
                    if response is not None:
                        peer = response.peer
                        if hasattr(peer, "user_id") and peer.user_id:
                            _r[0] = int(peer.user_id)
                        elif hasattr(peer, "channel_id") and peer.channel_id:
                            _r[0] = int(peer.channel_id)
                        elif hasattr(peer, "chat_id") and peer.chat_id:
                            _r[0] = int(peer.chat_id)
                except Exception:
                    pass
                finally:
                    _e.set()

            ConnectionsManager.getInstance(account).sendRequest(req, _cb, 0)
            _event.wait(timeout=5.0)

            if _mtproto[0] is not None:
                uid = _mtproto[0]
                _user_cache.put(clean, uid)
                log(f"[funstat] resolve_user({raw}) → MTProto resolved {uid}")
                if on_resolved: on_resolved(uid)
                return uid
            log(f"[funstat] resolve_user({raw}) → MTProto gave no result, falling back to API")
        except Exception as _e:
            log(f"[funstat] resolve_user({raw}) → MTProto unavailable: {_e}, falling back")

        r = self._get("users/resolve_username", name=clean)

        if isinstance(r, dict) and r.get("hidden"):
            _user_cache.put_hidden(clean)
            log(f"[funstat] resolve_user({raw}) → 403 hidden (cached)")
            return None

        data = (r or {}).get("data")
        if data:
            uid = data[0].get("id")
            if uid:
                _user_cache.put(clean, uid)
                log(f"[funstat] resolve_user({raw}) → resolved {uid}")
                if on_resolved: on_resolved(uid)
                return uid

        _user_cache.put_not_found(clean)
        log(f"[funstat] resolve_user({raw}) → NOT FOUND (cached as not_found)")
        return None

    def _resolve_group(self, group) -> int | None:
        clean = str(group).strip().lstrip("@")
        clean = re.sub(r"^(?:https?://)?t\.me/", "", clean).split("/")[0]
        if clean.lstrip("-").isdigit():
            return int(clean)
        r     = self._get("users/username_usage", username=clean)
        chats = ((r or {}).get("data") or {}).get("actualGroupsOrChannels") or []
        return chats[0]["id"] if chats else None

    def ping(self) -> dict:
        t0      = time.time()
        r       = self._get("users/resolve_username", name="q")
        elapsed = time.time() - t0
        tech    = (r or {}).get("tech", {})
        return {"request_ping": tech.get("request_duration", "0"), "responce_ping": elapsed}

    def get_balance(self) -> dict:
        r = self._get("users/resolve_username", name="q")
        return (r or {}).get("tech") or {}

    def basic_info_by_id(self, ids) -> dict | None:
        if not isinstance(ids, list):
            ids = [ids]
        resolved = [i if isinstance(i, int) else self.resolve_user(i) for i in ids]
        return self._get("users/basic_info_by_id", id=[x for x in resolved if x])

    def stats_min(self, user) -> dict | None:
        uid = user if isinstance(user, int) else self.resolve_user(user)
        if uid is None:
            return None
        r = self._get(f"users/{uid}/stats_min")
        if isinstance(r, dict) and r.get("hidden"):
            return r
        return r

    def stats(self, user) -> dict | None:
        uid = user if isinstance(user, int) else self.resolve_user(user)
        if uid is None:
            return None
        r = self._get(f"users/{uid}/stats")
        if isinstance(r, dict) and r.get("hidden"):
            return r
        return r

    def messages_count_by_uid(self, uid: int) -> int:
        r     = self._get(f"users/{uid}/messages_count")
        count = int(r) if isinstance(r, int) else 0
        log(f"[funstat] messages_count({uid}) → {count}")
        return count

    def messages_count(self, user) -> int:
        uid = self.resolve_user(user)
        if uid is None:
            return 0
        return self.messages_count_by_uid(uid)

    def groups_count(self, user, only_msg: bool = False) -> int:
        uid = user if isinstance(user, int) else self.resolve_user(user)
        if uid is None:
            return 0
        r = self._get(f"users/{uid}/groups_count", onlyMsg=str(only_msg).lower())
        return int(r) if isinstance(r, int) else 0

    def get_names(self, user) -> dict | None:
        uid = user if isinstance(user, int) else self.resolve_user(user)
        return self._get(f"users/{uid}/names") if uid else None

    def get_usernames(self, user) -> dict | None:
        uid = user if isinstance(user, int) else self.resolve_user(user)
        return self._get(f"users/{uid}/usernames") if uid else None

    def rep(self, user) -> dict | None:
        uid = user if isinstance(user, int) else self.resolve_user(user)
        if uid is None:
            return None
        r = self._get("users/reputation", id=uid)
        if isinstance(r, dict) and "user_id" in r:
            return {"data": r}
        return r

    def common_groups(self, user) -> dict | None:
        uid = user if isinstance(user, int) else self.resolve_user(user)
        return self._get(f"users/{uid}/common_groups_stat") if uid else None

    def get_stickers(self, user) -> dict | None:
        uid = user if isinstance(user, int) else self.resolve_user(user)
        return self._get(f"users/{uid}/stickers") if uid else None

    def username_usage(self, username: str) -> dict | None:
        clean = re.sub(r"^(?:https?://)?t\.me/", "", username.lstrip("@")).split("/")[0]
        return self._get("users/username_usage", username=clean)

    def common_groups_for_users(self, ids: list) -> dict | None:
        resolved = [i if isinstance(i, int) else self.resolve_user(i) for i in ids]
        resolved = [x for x in resolved if x]
        return self._get("groups/common_groups", id=resolved) if len(resolved) >= 2 else None

    def get_group_info(self, group) -> dict | None:
        gid = self._resolve_group(group)
        return self._get(f"groups/{gid}") if gid else None

    def evict_user_cache(self, uid: int) -> None:
        count = _api_cache.evict_prefix(f"users/{uid}")
        _user_cache.evict(uid)
        store_count = 0
        uid_str = str(uid)
        with _stores_lock:
            dead = [k for k in _stores if f"|u={uid_str}|" in k or f"|u={uid_str}" in k]
            for k in dead:
                _stores.pop(k, None)
                _stores_last_used.pop(k, None)
                store_count += 1
        log(f"[funstat] evict_user_cache({uid}): "
            f"api={count} stores={store_count} user_cache entries removed")

    def evict_group_cache(self, gid: int) -> None:
        count = _api_cache.evict_prefix(f"groups/{gid}")
        store_count = 0
        gid_str = str(gid)
        with _stores_lock:
            dead = [k for k in _stores if f"|g={gid_str}|" in k or f"|g={gid_str}" in k]
            for k in dead:
                _stores.pop(k, None)
                _stores_last_used.pop(k, None)
                store_count += 1
        log(f"[funstat] evict_group_cache({gid}): api={count} stores={store_count} removed")

    def clear_all_cache(self) -> None:
        _api_cache.clear()
        _user_cache.clear()
        with _stores_lock:
            _stores.clear()
            _stores_last_used.clear()
        log("[funstat] clear_all_cache: all caches cleared")

    def cache_stats(self) -> str:
        return (f"api_cache: {_api_cache.stats()}  |  "
                f"user_cache: {_user_cache.size()} entries  |  "
                f"stores: {len(_stores)}")

    def fetch_messages(self, uid: int, offset: int, limit: int,
                       text_filter=None, group_id=None) -> dict | None:
        page   = (offset // limit) + 1 if limit > 0 else 1
        params = {"page": page, "pageSize": limit}
        if text_filter:
            params["text_contains"] = text_filter
        if group_id is not None:
            params["group_id"] = group_id
        return self._get(f"users/{uid}/messages", **params)

    def fetch_chats(self, uid: int) -> dict | None:
        return self._get(f"users/{uid}/groups")

    def fetch_gifts(self, uid: int, offset: int, limit: int) -> dict | None:
        page = (offset // limit) + 1 if limit > 0 else 1
        return self._get(f"users/{uid}/gifts_relation", page=page, pageSize=limit)

    def fetch_group_members(self, gid: int) -> dict | None:
        return self._get(f"groups/{gid}/members")

    def fetch_search(self, query: str, offset: int, limit: int) -> dict | None:
        page = (offset // limit) + 1 if limit > 0 else 1
        return self._get("text/search", input=query, page=page, pageSize=limit)

def _fmt_date(s, fmt="%d.%m.%Y %H:%M") -> str:
    if not s:
        return "-"
    try:
        return datetime.fromisoformat(str(s).replace("Z", "+00:00")).strftime(fmt)
    except Exception:
        return str(s)

def _fmt_pct(v) -> str:
    return f"{float(v):.1f}%" if v is not None else "-"

def _parse_dur_ms(hms: str) -> float:
    try:
        if ":" in hms:
            h, m, s = hms.split(":")
            return round((int(h)*3600 + int(m)*60 + float(s))*1000, 2)
        return round(float(hms)*1000, 2)
    except Exception:
        return 0.0

def _link_msg(chat_id, msg_id) -> str:
    """Deep link к сообщению в группе/канале."""
    if not msg_id:
        return ""
    cid = str(chat_id or "")
    cid = cid[4:] if cid.startswith("-100") else (cid[1:] if cid.startswith("-") else cid)
    return f"tg://privatepost?channel={cid}&post={msg_id}"

def _link_chat(chat_id) -> str:
    """Deep link к чату/каналу по числовому ID."""
    if not chat_id:
        return ""
    cid = str(chat_id)
    cid = cid[4:] if cid.startswith("-100") else (cid[1:] if cid.startswith("-") else cid)
    return f"tg://privatepost?channel={cid}"

def _link_user(user_id) -> str:
    """Deep link к профилю пользователя."""
    return f"tg://openmessage?user_id={user_id}" if user_id else ""

def _link_username(username: str) -> str:
    """Deep link по @username (через resolve)."""
    if not username:
        return ""
    clean = username.lstrip("@")
    return f"tg://resolve?domain={clean}"

def _link_sticker_pack(short_name: str) -> str:
    """Deep link к набору стикеров."""
    if not short_name:
        return ""
    return f"tg://addstickers?set={short_name}"

def _render_chat(chat: dict) -> str:
    ch    = chat.get("chat") or {}
    icons = (
        ("👮" if chat.get("isAdmin") else "")
        + ("🔒" if ch.get("isPrivate") else "")
        + ("✖"  if chat.get("isLeft") else "")
    )
    first = _fmt_date(chat.get("firstMessage"), "%d %b")
    last  = _fmt_date(chat.get("lastMessage"),  "%d %b")
    last_msg_id = chat.get("lastMessageId")
    ch_id       = ch.get("id")
    username    = ch.get("username") or ch.get("link") or ""
    if last_msg_id and ch_id:
        link = _link_msg(ch_id, last_msg_id)
    elif username:
        link = _link_username(username)
    else:
        link = _link_chat(ch_id) if ch_id else ""
    title = ch.get("title", "?")
    name_part = f"<a href=\"{link}\">{title}</a>" if link else title
    return (f"{icons} {first} | {last} — {name_part} ({chat.get('messagesCount', 0)})")

def _render_message(m: dict) -> str:
    grp      = m.get("group") or {}
    link     = _link_msg(grp.get("id"), m.get("messageId") or m.get("message_id"))
    dt       = m.get("date", "")
    date_s   = ""
    if dt:
        try:
            d      = datetime.fromisoformat(dt.replace("Z", "+00:00"))
            date_s = f"[{d.day:02d} {RU_MONTHS[d.month]}]"
        except Exception:
            date_s = dt
    ch_icon  = "📢 " if grp.get("isPrivate") else ""
    rep_icon = " [R]" if m.get("replyToMessageId") or m.get("reply_to_message_id") else ""
    text     = (m.get("text") or "")[:120]
    grp_title = grp.get("title", "?")
    name_part = f"<a href=\"{link}\">{grp_title}</a>" if link else grp_title
    return f"{ch_icon}{name_part} {date_s}{rep_icon} {text}"

def _render_gift(item: dict, target_id: int, sent_to: set, recv_from: set) -> str | None:
    fid, tid   = item.get("from_user_id"), item.get("to_user_id")
    from_name  = item.get("from_first_name") or "?"
    to_name    = item.get("to_first_name")   or "?"
    date_s     = _fmt_date(item.get("last_gift_date"), "%d.%m.%Y")
    if fid == target_id:
        direction              = "↔️" if tid in recv_from else "➡️"
        other_id, other_name   = tid, to_name
    elif tid == target_id:
        direction              = "↔️" if fid in sent_to else "⬅️"
        other_id, other_name   = fid, from_name
    else:
        return None
    link = _link_user(other_id) if other_id else ""
    name_part = f"<a href=\"{link}\">{other_name}</a>" if link else other_name
    return f"{direction} {name_part} ({date_s})"

def _render_member(m: dict, _counter: list | None = None) -> str:
    deleted  = m.get("is_deleted") or m.get("deleted") or False
    status   = "❌" if deleted else "✔️"
    admin    = "👑" if m.get("is_admin") or m.get("isAdmin") else ""
    name     = m.get("name") or m.get("first_name") or ("Удалённый аккаунт" if deleted else "?")
    un       = m.get("username") or ""
    uid      = m.get("id") or m.get("user_id")
    cnt      = m.get("messages_count") or m.get("messagesCount") or m.get("count") or 0
    if un:
        link = _link_username(un)
    elif uid and not deleted:
        link = _link_user(uid)
    else:
        link = ""
    name_part = f"<a href=\"{link}\">{name}</a>" if link else name
    cnt_part  = f" - {cnt}" if cnt else ""
    num_part  = ""
    if _counter is not None:
        _counter[0] += 1
        num_part = f"{_counter[0]:02d}. "
    return f"{num_part}{status} {admin}{name_part}{cnt_part}"

def _render_search(m: dict) -> str:
    grp  = m.get("group") or {}
    uid  = m.get("user_id") or m.get("id")
    link = _link_msg(grp.get("id"), m.get("message_id"))
    name = m.get("name", "?")
    name_part = f"<a href=\"{link}\">{name}</a>" if link else (
        f"<a href=\"{_link_user(uid)}\">{name}</a>" if uid else name
    )
    text = (m.get("text") or "")[:80]
    return f"• {name_part}: {text}"

def _fmt_ping(data: dict, lang: str) -> str:
    return _t(lang, "tpl_ping",
              request_ping=_parse_dur_ms(str(data.get("request_ping","0"))),
              responce_ping=round(float(data.get("responce_ping",0))*1000, 2))

def _fmt_balance(data: dict, lang: str) -> str:
    val = data.get("current_ballance") or data.get("currentBallance") or "?"
    return _t(lang, "tpl_balance", current_ballance=val)

def _coerce(d: dict) -> dict:
    return {k: ("-" if v is None else v) for k, v in d.items()}

def _fmt_sm(data: dict, lang: str) -> str:
    d = data.get("data") if isinstance(data.get("data"), dict) else data
    if not isinstance(d, dict) or "id" not in d:
        return _t(lang, "no_data")
    d = dict(d)
    d["first_msg_date"] = _fmt_date(d.get("first_msg_date"))
    d["last_msg_date"]  = _fmt_date(d.get("last_msg_date"))
    return _t(lang, "tpl_sm", **_coerce(d))

def _fmt_s(data: dict, lang: str) -> str:
    d = data.get("data") if isinstance(data.get("data"), dict) else data
    if not isinstance(d, dict) or "id" not in d:
        return _t(lang, "no_data")
    d = dict(d)
    d["first_msg_date"]    = _fmt_date(d.get("first_msg_date"))
    d["last_msg_date"]     = _fmt_date(d.get("last_msg_date"))
    d["unique_percent"]    = _fmt_pct(d.get("unique_percent"))
    d["reply_percent"]     = _fmt_pct(d.get("reply_percent"))
    d["media_percent"]     = _fmt_pct(d.get("media_percent"))
    d["link_percent"]      = _fmt_pct(d.get("link_percent"))
    fc = d.get("favorite_chat")
    if isinstance(fc, dict):
        fc_id  = fc.get("id")
        fc_un  = fc.get("username") or fc.get("link") or ""
        fc_ttl = fc.get("title", "-")
        if fc_un:
            fc_link = _link_username(fc_un)
        elif fc_id:
            fc_link = _link_chat(fc_id)
        else:
            fc_link = ""
        d["favorite_chat_title"] = (
            f"<a href=\"{fc_link}\">{fc_ttl}</a>" if fc_link else fc_ttl
        )
    else:
        d["favorite_chat_title"] = "-"
    sv, sl = d.get("stars_val"), d.get("stars_level")
    d["stars_line"] = (_t(lang,"stars",val=sv,level=sl)+"\n") if sv else ""
    ab = d.get("about")
    d["about_line"] = (_t(lang,"about",about=ab)+"\n") if ab else ""
    return _t(lang, "tpl_s", **_coerce(d))

def _fmt_names(data: dict, lang: str) -> str:
    lines = [_t(lang,"names_header")]
    for n in (data.get("data") or []):
        lines.append(f"├ {_fmt_date(n.get('date_time'),'%d.%m.%Y')} ➜ {n.get('name','?')}")
    return "\n".join(lines)

def _fmt_usernames(data: dict, lang: str) -> str:
    items = sorted(data.get("data") or [], key=lambda n: n.get("date_time",""), reverse=True)
    lines = [_t(lang,"usernames_header")]
    for n in items:
        un   = n.get("name", "?")
        link = _link_username(un)
        un_part = f"<a href=\"{link}\">@{un}</a>" if link else f"@{un}"
        lines.append(f"↳ {_fmt_date(n.get('date_time'),'%d.%m.%Y')} ➜ {un_part}")
    return "\n".join(lines)

def _fmt_names_and_usernames(nd: dict, usd: dict, lang: str) -> str:
    lines = []
    if nd.get("data"):
        lines.append(_t(lang,"names_header"))
        for n in nd["data"]:
            lines.append(f"├ {_fmt_date(n.get('date_time'),'%d.%m.%Y')} ➜ {n.get('name','?')}")
    if usd.get("data"):
        lines.append(_t(lang,"usernames_header"))
        for n in sorted(usd["data"], key=lambda x: x.get("date_time",""), reverse=True):
            un   = n.get("name", "?")
            link = _link_username(un)
            un_part = f"<a href=\"{link}\">@{un}</a>" if link else f"@{un}"
            lines.append(f"↳ {_fmt_date(n.get('date_time'),'%d.%m.%Y')} ➜ {un_part}")
    return "\n".join(lines) if lines else _t(lang,"no_data")

def _fmt_common_groups(data: dict, lang: str) -> str:
    lines = [_t(lang,"common_groups_header")]
    for u in (data.get("data") or []):
        fn, un, uid = u.get("first_name","?"), u.get("username"), u.get("id")
        link = _link_user(uid) if uid else ""
        name_part = f"<a href=\"{link}\">{fn}</a>" if link else fn
        tag  = f" (<a href=\"{_link_username(un)}\">@{un}</a>)" if un else ""
        lines.append(f"• {name_part}{tag} — {u.get('common_groups',0)}")
    return "\n".join(lines)

def _fmt_stickers(data: dict, lang: str) -> str:
    lines = [_t(lang,"stickers_header")]
    for s in (data.get("data") or []):
        sn, ti, cnt = s.get("short_name",""), s.get("title","?"), s.get("stickers_count",0)
        link = _link_sticker_pack(sn) if sn else ""
        name_part = f"<a href=\"{link}\">{ti}</a>" if link else ti
        lines.append(f"• {name_part} ({cnt})")
    return "\n".join(lines)

def _fmt_group_info(data: dict, lang: str) -> str:
    info  = data.get("info") or {}
    stat  = data.get("today_group_stat") or {}
    title = info.get("title", "?")
    gid   = info.get("id")
    un    = info.get("username") or info.get("link") or ""
    if un:
        link = _link_username(un)
    elif gid:
        link = _link_chat(gid)
    else:
        link = ""

    lines = [f"ㅤ<a href=\"{link}\">{title}</a>" if link else f"ㅤ{title}"]

    rank      = stat.get("rank")
    total     = stat.get("totalUsersCount") or stat.get("total_users_count")
    active    = stat.get("activeUsersCount") or stat.get("active_users_count", 0)
    msg_count = stat.get("messagesCount") or stat.get("messages_count", 0)
    media_cnt = stat.get("mediaCount") or stat.get("media_count", 0)
    circles   = stat.get("circleCount") or stat.get("circle_count", 0)
    voices    = stat.get("voiceCount") or stat.get("voice_count", 0)
    media_pct = ""
    if msg_count and media_cnt:
        try:
            media_pct = f" ({float(media_cnt)/float(msg_count)*100:.2f}%)"
        except Exception:
            pass

    if rank and total:
        lines.append(f"В топе # {rank} из {total}")
    if active and msg_count:
        lines.append(f"{active} человек за сутки")
        lines.append(f"написали {msg_count} сообщений")
        if media_cnt:
            lines.append(f"из них {media_cnt}{media_pct} медиа")
        lines.append(f"{circles} кружков и {voices} голосовых")

    lines.append(f"ID: <code>{gid or '?'}</code>")

    about = info.get("description") or info.get("about") or ""
    if about:
        lines.append(f"Описание:\n{about}")

    top = stat.get("topUsers") or stat.get("top_users") or []
    if top:
        lines.append("Топ за сутки:")
        for i, u in enumerate(top, 1):
            name  = u.get("first_name") or u.get("name") or "?"
            uname = u.get("username") or ""
            cnt   = u.get("messages_count") or u.get("messagesCount") or u.get("count") or 0
            uid_u = u.get("id")
            prem  = "💎 " if u.get("has_premium") or u.get("hasPremium") else ""
            if uname:
                ulink = _link_username(uname)
            elif uid_u:
                ulink = _link_user(uid_u)
            else:
                ulink = ""
            name_part = f"<a href=\"{ulink}\">{prem}{name}</a>" if ulink else f"{prem}{name}"
            lines.append(f"{i}. {name_part} - {cnt}")

    return "\n".join(lines)

def _fmt_rep(data: dict, lang: str, uid: int | None = None) -> str:
    d = data.get("data") if isinstance(data, dict) else None
    if d is None:
        d = data
    if not isinstance(d, dict):
        log(f"[funstat] _fmt_rep: unexpected data type {type(d)}: {repr(d)[:200]}")
        return str(data)
    log(f"[funstat] _fmt_rep: keys={list(d.keys())}")
    def nd(k, transform=None):
        v = d.get(k)
        if v is None: return "-"
        return transform(v) if transform else v
    rep_uid  = d.get("user_id") or uid or 0
    rep_name = d.get("first_name") or d.get("name") or "?"
    return _t(lang, "tpl_rep",
              user_id=rep_uid,
              first_name=rep_name,
              reputation_name=nd("reputation_name"),
              positive_count=nd("positive_count"),
              negative_count=nd("negative_count"),
              num_votes=nd("num_votes"),
              anon_votes_count=nd("anon_votes_count"),
              last_time=nd("last_time", lambda v: _fmt_date(v, "%d.%m.%Y")))

def _fmt_usage(data: dict, username: str, lang: str) -> str:
    d     = data.get("data") or {}
    lines = [_t(lang,"usage_header", username=username)]
    for sk, hk in [("actualUsers","usage_current"),
                   ("usageByUsersInThePast","usage_past"),
                   ("actualGroupsOrChannels","usage_groups")]:
        items = d.get(sk) or []
        if not items:
            continue
        lines.append(_t(lang, hk))
        for item in items:
            if sk == "actualGroupsOrChannels":
                ch_title = item.get("title", "?")
                ch_link  = item.get("link") or item.get("username") or ""
                ch_id    = item.get("id")
                if ch_link:
                    tg_link = _link_username(ch_link)
                elif ch_id:
                    tg_link = _link_chat(ch_id)
                else:
                    tg_link = ""
                name_part = f"<a href=\"{tg_link}\">{ch_title}</a>" if tg_link else ch_title
                lines.append(f"  • {name_part}")
            else:
                uid_u = item.get("id")
                fn    = item.get("first_name", "")
                un_u  = item.get("username")
                link  = _link_user(uid_u) if uid_u else ""
                name_part = f"<a href=\"{link}\">{fn}</a>" if link else fn
                un_part = (
                    f" (<a href=\"{_link_username(un_u)}\">@{un_u}</a>)"
                    if un_u else ""
                )
                lines.append(f"  • {name_part}{un_part}")
    return "\n".join(lines)

def _fmt_cgf(data: dict, users: list, lang: str) -> str:
    label = " & ".join(str(u) for u in users)
    lines = [_t(lang,"cgf_header", users=label)]
    for g in (data.get("data") or []):
        gid   = g.get("id")
        title = g.get("title", "?")
        un    = g.get("username") or g.get("link") or ""
        if un:
            link = _link_username(un)
        elif gid:
            link = _link_chat(gid)
        else:
            link = ""
        name_part = f"<a href=\"{link}\">{title}</a>" if link else title
        lines.append(f"• {name_part}")
    return "\n".join(lines)

def _fmt_bi(items: list, lang: str) -> str:
    u  = items[0]
    uid = u.get("id")
    un  = u.get("username") or ""
    fn  = u.get("first_name", "")
    ln  = u.get("last_name", "")
    full_name = f"{fn} {ln}".strip() or "?"
    link = _link_user(uid) if uid else ""
    name_part = f"<a href=\"{link}\">{full_name}</a>" if link else full_name
    un_part = (
        f"<a href=\"{_link_username(un)}\">@{un}</a>" if un else "-"
    )
    return (
        f"{name_part}\n"
        f"ID: <code>{uid}</code>  {un_part}\n"
        f"Bot: {u.get('is_bot')}  Active: {u.get('is_active')}  Premium: {u.get('has_premium')}"
    )

def _render_page(store: PaginatedStore, page: int, header: str, renderer) -> str:
    lines = [header]
    for item in store.get_page(page):
        line = renderer(item)
        if line:
            lines.append(line)
    return "\n".join(lines)

def _extract_items(raw) -> list:
    if isinstance(raw, list):
        return raw
    if isinstance(raw, dict):
        data = raw.get("data")
        if isinstance(data, list):
            return data
        if isinstance(data, dict):
            return data.get("data") or []
    return []

def _extract_total(raw) -> int | None:
    if isinstance(raw, dict):
        data = raw.get("data")
        if isinstance(data, dict):
            t = data.get("total")
            if t is not None:
                return int(t)
        meta = raw.get("meta") or {}
        t    = meta.get("total")
        if t is not None:
            return int(t)
    return None

def _fetch_page(store: PaginatedStore, page: int, fetcher,
               max_retries: int = 2) -> list | None:
    if store.has_page_data(page):
        log(f"[funstat] fetch_page: page {page} already in loaded_pages")
        return store.get_page(page)

    if store.is_inflight(page):
        log(f"[funstat] fetch_page: page {page} is inflight, waiting...")
        for _ in range(30):
            time.sleep(0.1)
            if store.has_page_data(page):
                return store.get_page(page)
        log(f"[funstat] fetch_page: timeout waiting for inflight page {page}")
        return None

    store.set_inflight(page, True)
    try:
        ps     = store.page_size
        offset = (page - 1) * ps
        log(f"[funstat] fetch_page: page={page} offset={offset} limit={ps}")

        raw   = None
        delay = 0.5
        for attempt in range(max_retries + 1):
            try:
                raw = fetcher(offset, ps)
                break
            except Exception as exc:
                if attempt < max_retries:
                    log(f"[funstat] fetch_page: attempt {attempt+1} failed ({exc}), retry in {delay}s")
                    time.sleep(delay)
                    delay *= 2
                else:
                    log(f"[funstat] fetch_page: all retries failed for page {page}: {exc}")
                    return None

        if raw is None:
            log(f"[funstat] fetch_page: fetcher returned None for page {page}")
            return None
        if isinstance(raw, dict) and "error" in raw:
            log(f"[funstat] fetch_page: API error for page {page}: {raw['error']}")
            return None

        items = _extract_items(raw)
        total = _extract_total(raw)
        log(f"[funstat] fetch_page: page {page} → {len(items)} items, api_total={total}")

        is_exhausted = (len(items) < ps)

        store.store_page(page, items, total, is_exhausted=is_exhausted)
        return store.get_page(page)

    except Exception:
        log(f"[funstat] fetch_page EXCEPTION page={page}: {traceback.format_exc()}")
        return None
    finally:
        store.set_inflight(page, False)

def _prefetch_page(store: PaginatedStore, page: int,
                    fetcher=None) -> None:
    actual_fetcher = fetcher or store.fetcher
    if actual_fetcher is None:
        return
    if store.has_page_data(page) or store.is_inflight(page):
        return
    if store.exhausted:
        return
    def work():
        log(f"[funstat] prefetch: page={page}")
        _fetch_page(store, page, actual_fetcher)
        log(f"[funstat] prefetch: page={page} done")
    threading.Thread(target=work, daemon=True).start()

def _utf16_len(s: str) -> int:
    return len(s.encode("utf-16-le")) // 2

def _html_to_entities(html: str):
    from org.telegram.tgnet import TLRPC
    TAG_RE = re.compile(
        r'<a\s+href="([^"]*)">(.*?)</a>|<b>(.*?)</b>|<code>(.*?)</code>',
        re.DOTALL
    )
    parts, entities, last_end = [], [], 0
    for m in TAG_RE.finditer(html):
        parts.append(html[last_end:m.start()])
        offset = _utf16_len("".join(parts))
        if m.group(1) is not None:
            url, inner = m.group(1), m.group(2); parts.append(inner)
            ent = TLRPC.TL_messageEntityTextUrl()
            ent.offset = offset; ent.length = _utf16_len(inner); ent.url = url
        elif m.group(3) is not None:
            inner = m.group(3); parts.append(inner)
            ent = TLRPC.TL_messageEntityBold()
            ent.offset = offset; ent.length = _utf16_len(inner)
        elif m.group(4) is not None:
            inner = m.group(4); parts.append(inner)
            ent = TLRPC.TL_messageEntityCode()
            ent.offset = offset; ent.length = _utf16_len(inner)
        else:
            last_end = m.end(); continue
        entities.append(ent)
        last_end = m.end()
    parts.append(html[last_end:])
    return "".join(parts), entities

def _build_help(lang: str) -> str:
    t         = STRINGS.get(lang, STRINGS["ru"])
    cmd_user  = ["cmd_sm","cmd_s","cmd_chats","cmd_names","cmd_us","cmd_msg",
                 "cmd_gc","cmd_mc","cmd_rep","cmd_cg","cmd_sticks","cmd_gifts",
                 "cmd_uu","cmd_bi","cmd_cgf"]
    cmd_group = ["cmd_gi","cmd_gm"]
    cmd_other = ["cmd_ping","cmd_balance","cmd_st"]
    flags     = ["help_flag_s","help_flag_p","help_flag_f","help_flag_t"]
    bot_link  = '<a href="tg://resolve?domain=sgwlink">@sgwlink</a>'
    hint      = (
        f"🔑 <b>Токен:</b> отправь /api боту funstat\n(переходник на актуальную ссылку на бота: {bot_link})"
        if lang == "ru" else
        f"🔑 <b>Token:</b> send /api to the funstat bot\n(current bot link: {bot_link})"
    )
    def bold(key):
        cmd   = t[key]
        parts = cmd.split(" ", 1)
        return f"  .fs <b>{parts[0]}</b> {parts[1]}" if len(parts) > 1 else f"  .fs <b>{cmd}</b>"
    lines  = [f"<b>{t['help_title']}</b>", hint, "", f"<b>{t['help_user']}</b>"]
    lines += [bold(k) for k in cmd_user]
    lines += ["", f"<b>{t['help_group']}</b>"] + [bold(k) for k in cmd_group]
    lines += ["", f"<b>{t['help_other']}</b>"] + [bold(k) for k in cmd_other]
    lines += ["", f"<b>{t['help_flags']}</b>"] + [f"  {t[k]}" for k in flags]
    return "\n".join(lines)

_MULTI_USER_CMDS = {"cgf"}
_GROUP_CMDS      = {"gi", "gm"}

_GREEDY_FLAGS = {"f", "q"}

def _parse_args(text: str) -> dict:
    """
    Разбирает командную строку .fs.

    Ключевые правила:
    - Флаги вида -X начинают новый ключ.
    - Числа вида -123 НЕ считаются флагами (это отрицательные ID).
    - Флаги из _GREEDY_FLAGS (-f, -q) захватывают все последующие слова
      вплоть до следующего «настоящего» флага.
    """
    parts  = text.strip().split()
    i      = 1  
    cmd    = parts[i] if i < len(parts) and not parts[i].startswith("-") else ""
    if cmd:
        i += 1
    result: dict = {"command": cmd}
    u_list: list = []

    def _is_flag(s: str) -> bool:
        return s.startswith("-") and not re.fullmatch(r"-\d+", s)

    while i < len(parts):
        part = parts[i]
        if _is_flag(part):
            key = part.lstrip("-")
            i  += 1
            if key in _GREEDY_FLAGS:
                words = []
                while i < len(parts) and not _is_flag(parts[i]):
                    words.append(parts[i])
                    i += 1
                result[key] = " ".join(words)
            else:
                if i < len(parts) and not _is_flag(parts[i]):
                    val = parts[i]
                    if key == "u":
                        u_list.append(val)
                    else:
                        result[key] = val
                    i += 1
                else:
                    result[key] = True
        else:
            if cmd in _GROUP_CMDS:
                if "g" not in result:
                    result["g"] = parts[i]
            elif cmd in _MULTI_USER_CMDS:
                u_list.append(parts[i])
            elif cmd == "st":
                existing = result.get("q", "")
                result["q"] = (existing + " " + parts[i]).strip()
            else:
                if not u_list:
                    u_list.append(parts[i])
            i += 1

    if u_list:
        result["u"]      = u_list[0]
        result["u_list"] = u_list
    for k, v in result.items():
        if k not in ("command","u_list","q","f") and isinstance(v,str) and re.fullmatch(r"-?\d+",v):
            result[k] = int(v)
    return result

def _store_key(args: dict) -> str:
    return (f"{args.get('command','')}"
            f"|u={args.get('u','')}"
            f"|g={args.get('g','')}"
            f"|f={args.get('f','')}"
            f"|q={args.get('q','')}")

def _strip_page(text: str) -> str:
    return re.sub(r"\s+-p\s+\d+", "", text).strip()

def dispatch(text: str, fs: FunstatClient, lang: str,
             page_size: int = 20, reset: bool = False,
             on_tv_update=None) -> dict | None:
    args  = _parse_args(text)
    cmd   = args.get("command", "")
    user  = args.get("u")
    group = args.get("g")
    page  = max(1, int(args.get("p", 1)))
    cb    = _strip_page(text)
    log(f"[funstat] dispatch: cmd={cmd!r} user={user!r} group={group!r} page={page} page_size={page_size} reset={reset}")

    _add_to_history(text)

    def _r(txt, pg=1, total=1, paginate=False, sk="", uid=None, gid=None, is_error=False, is_hidden=False):
        log(f"[funstat] dispatch result: cmd={cmd!r} pg={pg}/{total} paginate={paginate} is_error={is_error} is_hidden={is_hidden} text_len={len(txt)}")
        return {"text": txt, "page": pg, "total_pages": total,
                "paginate": paginate, "cmd_base": cb,
                "store_key": sk, "user_id": uid, "group_id": gid,
                "is_error": is_error, "is_hidden": is_hidden}

    def need_u(): return _r(_t(lang,"need_u"), is_error=True)
    def need_g(): return _r(_t(lang,"need_g"), is_error=True)

    def err(msg, uid=None, is_hidden=False):
        msg_s = str(msg)
        if msg_s == "403" or is_hidden:
            txt = _t(lang, "error_403")
            return _r(txt, uid=uid, is_error=True, is_hidden=True)
        if "⏱ timeout" in msg_s or "timed out" in msg_s.lower():
            label = "⏱ Таймаут сервера — попробуй позже" if lang == "ru" else "⏱ Server timeout — try again later"
            txt = f"• {label}\n• cmd: {cmd}"
        else:
            txt = _t(lang, "error", err=msg_s)
        return _r(txt, uid=uid, is_error=True)

    uid: int | None = None
    if user is not None:
        def _on_resolved(resolved_uid, _tv_cb=on_tv_update, _lang=lang):
            if _tv_cb:
                run_on_ui_thread(lambda: _tv_cb(
                    f"ㅤ⏳ {_t(_lang,'resolving_id')}[id{resolved_uid}]"
                ))
        uid = fs.resolve_user(user, on_resolved=_on_resolved)

    def _uid_err(u):
        """Return appropriate error: 403 if hidden, not_found if unknown, generic otherwise."""
        if u is None:
            return _r(_t(lang, "hidden_user"), is_error=True)
        clean = str(u).lstrip("@")
        clean = re.sub(r"^https?://t\.me/", "", clean).split("/")[0]
        if _user_cache.is_hidden(clean):
            return err("403", is_hidden=True)
        if _user_cache.is_not_found(clean):
            return _r(_t(lang, "user_not_found"), is_error=True)
        return _r(_t(lang, "hidden_user"), is_error=True)

    if cmd == "help":    return _r(_build_help(lang))
    if cmd == "ping":
        try:
            return _r(_fmt_ping(fs.ping(), lang))
        except Exception as e:
            msg = f"• ⏱ Таймаут сервера\n• {e}" if lang == "ru" else f"• ⏱ Server timeout\n• {e}"
            return err(msg)
    if cmd == "balance": return _r(_fmt_balance(fs.get_balance(), lang))

    if cmd == "sm":
        if not user: return need_u()
        if uid is None: return _uid_err(user)
        data = fs.stats_min(uid) or {}
        if isinstance(data, dict) and data.get("hidden"):
            return err("403", uid=uid, is_hidden=True)
        d_inner = data.get("data") if isinstance(data.get("data"), dict) else data
        if not (isinstance(d_inner, dict) and d_inner.get("id")):
            return err(_t(lang, "hidden_user"), uid=uid)
        return _r(_fmt_sm(data, lang), uid=uid)

    if cmd == "s":
        if not user: return need_u()
        if uid is None: return _uid_err(user)
        data = fs.stats(uid) or {}
        if isinstance(data, dict) and data.get("hidden"):
            data = fs.stats_min(uid) or {}
            if isinstance(data, dict) and data.get("hidden"):
                return err("403", uid=uid, is_hidden=True)
            d_inner2 = data.get("data") if isinstance(data.get("data"), dict) else data
            if not (isinstance(d_inner2, dict) and d_inner2.get("id")):
                return err("403", uid=uid, is_hidden=True)
            return _r(_fmt_sm(data, lang), uid=uid)
        d_inner = data.get("data") if isinstance(data.get("data"), dict) else data
        if not (isinstance(d_inner, dict) and d_inner.get("id")):
            log(f"[funstat] cmd s: full stats empty, falling back to stats_min")
            data = fs.stats_min(uid) or {}
            if isinstance(data, dict) and data.get("hidden"):
                return err("403", uid=uid, is_hidden=True)
            return _r(_fmt_sm(data, lang), uid=uid)
        return _r(_fmt_s(data, lang), uid=uid)

    if cmd == "names":
        if not user: return need_u()
        if uid is None: return _uid_err(user)
        return _r(_fmt_names(fs.get_names(uid) or {}, lang), uid=uid)

    if cmd == "us":
        if not user: return need_u()
        if uid is None: return _uid_err(user)
        return _r(_fmt_usernames(fs.get_usernames(uid) or {}, lang), uid=uid)

    if cmd == "gc":
        if not user: return need_u()
        if uid is None: return _uid_err(user)
        count = fs.groups_count(uid)
        return _r(_t(lang, "tpl_gc", count=count), uid=uid)

    if cmd == "mc":
        if not user: return need_u()
        if uid is None: return _uid_err(user)
        count = fs.messages_count_by_uid(uid)
        return _r(_t(lang, "tpl_mc", count=count), uid=uid)

    if cmd == "rep":
        if not user: return need_u()
        if uid is None: return _uid_err(user)
        return _r(_fmt_rep(fs.rep(uid) or {}, lang, uid=uid), uid=uid)

    if cmd == "cg":
        if not user: return need_u()
        if uid is None: return _uid_err(user)
        return _r(_fmt_common_groups(fs.common_groups(uid) or {}, lang), uid=uid)

    if cmd == "sticks":
        if not user: return need_u()
        if uid is None: return _uid_err(user)
        return _r(_fmt_stickers(fs.get_stickers(uid) or {}, lang), uid=uid)

    if cmd == "uu":
        if not user: return need_u()
        uname = str(user).lstrip("@")
        return _r(_fmt_usage(fs.username_usage(uname) or {}, uname, lang), uid=uid)

    if cmd == "bi":
        if not user: return need_u()
        items = (fs.basic_info_by_id(uid if uid else user) or {}).get("data") or []
        return _r(_fmt_bi(items, lang) if items else _t(lang,"no_data"), uid=uid)

    if cmd == "cgf":
        u_list = args.get("u_list") or ([user] if user else [])
        if len(u_list) < 2: return need_u()
        resolved_list = []
        for u in u_list:
            rid = u if isinstance(u, int) else fs.resolve_user(u)
            if rid: resolved_list.append(rid)
        if len(resolved_list) < 2: return need_u()
        r = fs.common_groups_for_users(resolved_list)
        return _r(_fmt_cgf(r, u_list, lang) if r else _t(lang,"no_data"))

    if cmd == "gi":
        if not group: return need_g()
        gid_resolved = fs._resolve_group(group)
        if gid_resolved is None: return err("group not found")
        data = fs._get(f"groups/{gid_resolved}") or {}
        if isinstance(data, dict) and "error" in data:
            return err(str(data["error"]))
        return _r(_fmt_group_info(data, lang), gid=gid_resolved)

    if cmd == "chats":
        if not user: return need_u()
        if uid is None: return _uid_err(user)
        skey  = _store_key(args)
        store = _get_store(skey, page_size, reset=reset)
        if not store.is_fresh() or reset:
            raw = fs.fetch_chats(uid)
            if raw is None or (isinstance(raw, dict) and "error" in raw):
                is_h = isinstance(raw, dict) and raw.get("hidden", False)
                return err(str((raw or {}).get("error","fetch failed")), uid=uid, is_hidden=is_h)
            all_items = raw.get("data") or []
            store.reset()
            store.set_total(len(all_items))
            store.add_items(all_items, len(all_items), page=None, is_exhausted=True)
        pg  = max(1, min(page, store.total_pages()))
        txt = _render_page(store, pg, _t(lang,"chats_header"), _render_chat)
        return _r(txt, pg, store.total_pages(), store.total_pages()>1, skey, uid)

    if cmd == "msg":
        if not user: return need_u()
        if uid is None: return _uid_err(user)
        skey  = _store_key(args)
        gid: int | None = None
        if group is not None:
            gid = fs._resolve_group(group)

        store = _get_store(skey, page_size, reset=reset)

        def _msg_fetcher(offset, limit, _uid=uid, _f=args.get("f"), _g=gid):
            return fs.fetch_messages(_uid, offset, limit, _f, _g)

        store.fetcher = _msg_fetcher

        if not store.is_fresh() or reset:
            total_msgs = fs.messages_count_by_uid(uid)
            store.reset()
            store.fetcher = _msg_fetcher
            store.set_total(total_msgs)
            log(f"[funstat] msg: initial load, total_known={total_msgs}")
            raw = fs.fetch_messages(uid, 0, INITIAL_BATCH, args.get("f"), gid)
            if raw is None or (isinstance(raw, dict) and "error" in raw):
                is_h = isinstance(raw, dict) and raw.get("hidden", False)
                return err(str((raw or {}).get("error","fetch failed")), uid=uid, is_hidden=is_h)
            items = _extract_items(raw)
            is_ex = len(items) < INITIAL_BATCH
            store.add_items(items, None, page=None, is_exhausted=is_ex)
        elif not store.has_page_data(page):
            log(f"[funstat] msg: lazy-load page={page}, total_known={store.total_known}")
            result = _fetch_page(store, page, _msg_fetcher)
            if result is None:
                return err("page fetch failed", uid=uid)
        else:
            log(f"[funstat] msg: page={page} served from store (total_known={store.total_known})")

        pg  = max(1, min(page, store.total_pages()))
        txt = _render_page(store, pg, _t(lang,"messages_header"), _render_message)

        if pg < store.total_pages():
            _prefetch_page(store, pg + 1, _msg_fetcher)
        if pg > 1:
            _prefetch_page(store, pg - 1, _msg_fetcher)

        return _r(txt, pg, store.total_pages(), store.total_pages()>1, skey, uid)

    if cmd == "gifts":
        if not user: return need_u()
        if uid is None: return _uid_err(user)
        filter_type = str(args.get("t", "")).lower()
        skey  = _store_key(args)
        store = _get_store(skey, page_size, reset=reset)

        def _gift_fetcher(offset, limit, _uid=uid):
            return fs.fetch_gifts(_uid, offset, limit)

        store.fetcher = _gift_fetcher

        if not store.is_fresh() or reset:
            raw = fs.fetch_gifts(uid, 0, INITIAL_BATCH)
            if raw is None or (isinstance(raw, dict) and "error" in raw):
                is_h = isinstance(raw, dict) and raw.get("hidden", False)
                return err(str((raw or {}).get("error","fetch failed")), uid=uid, is_hidden=is_h)
            items = _extract_items(raw)
            total = _extract_total(raw)
            is_ex = len(items) < INITIAL_BATCH
            store.reset()
            store.add_items(items, total, page=None, is_exhausted=is_ex)
        elif not store.has_page_data(page):
            result = _fetch_page(store, page, _gift_fetcher)
            if result is None:
                return err("page fetch failed", uid=uid)

        all_it    = store.get_all_items_for_sets()
        sent_to   = {i.get("to_user_id")   for i in all_it if i.get("from_user_id") == uid}
        recv_from = {i.get("from_user_id") for i in all_it if i.get("to_user_id")   == uid}

        def gift_r(item, _uid=uid, _st=sent_to, _rf=recv_from, _ft=filter_type):
            fid, tid = item.get("from_user_id"), item.get("to_user_id")
            is_mutual = (fid == _uid and tid in _rf) or (tid == _uid and fid in _st)
            is_sent   = fid == _uid
            is_recv   = tid == _uid
            if _ft == "mutual" and not is_mutual:
                return None
            if _ft == "sent" and not is_sent:
                return None
            if _ft == "recv" and not is_recv:
                return None
            return _render_gift(item, _uid, _st, _rf)

        pg  = max(1, min(page, store.total_pages()))
        filter_label = {"sent": "  ➡️", "recv": "  ⬅️", "mutual": "  ↔️"}.get(filter_type, "")
        hdr = _t(lang,"gifts_header") + filter_label
        txt = _render_page(store, pg, hdr, gift_r)
        if pg < store.total_pages():
            _prefetch_page(store, pg + 1, _gift_fetcher)
        if pg > 1:
            _prefetch_page(store, pg - 1, _gift_fetcher)
        result_d = _r(txt, pg, store.total_pages(), store.total_pages()>1, skey, uid)
        result_d["gift_filter"] = filter_type
        return result_d

    if cmd == "gm":
        if not group: return need_g()
        gid2  = fs._resolve_group(group)
        if gid2 is None: return err("group not found")
        skey  = _store_key(args)
        store = _get_store(skey, page_size, reset=reset)
        if not store.is_fresh() or reset:
            raw = fs.fetch_group_members(gid2)
            if raw is None or (isinstance(raw, dict) and "error" in raw):
                return err(str((raw or {}).get("error","fetch failed")))
            items = raw.get("data") or []
            store.reset()
            store.set_total(len(items))
            store.add_items(items, len(items), page=None, is_exhausted=True)
        pg  = max(1, min(page, store.total_pages()))
        total_members = store.total_known if store.total_known >= 0 else sum(
            len(store.pages.get(p, [])) for p in store.loaded_pages
        )
        offset_start = (pg - 1) * page_size
        counter = [offset_start]
        def _member_renderer(m, _c=counter):
            return _render_member(m, _counter=_c)
        hdr = (f"ㅤУчастники чата\n❌ - аккаунт удалён.\n"
               f"Всего {total_members}, страница {pg} из {store.total_pages()}")
        txt = _render_page(store, pg, hdr, _member_renderer)
        return _r(txt, pg, store.total_pages(), store.total_pages()>1, skey, gid=gid2)

    if cmd == "st":
        q = str(args.get("q") or "")
        if not q: return err(_t(lang,"need_q"))
        skey  = _store_key(args)
        store = _get_store(skey, page_size, reset=reset)

        def _st_fetcher(offset, limit, _q=q):
            return fs.fetch_search(_q, offset, limit)

        store.fetcher = _st_fetcher

        if not store.is_fresh() or reset:
            raw = fs.fetch_search(q, 0, INITIAL_BATCH)
            if raw is None or (isinstance(raw, dict) and "error" in raw):
                return err(str((raw or {}).get("error","fetch failed")))
            items = _extract_items(raw)
            total = _extract_total(raw)
            is_ex = len(items) < INITIAL_BATCH
            store.reset()
            store.add_items(items, total, page=None, is_exhausted=is_ex)
        elif not store.has_page_data(page):
            result = _fetch_page(store, page, _st_fetcher)
            if result is None:
                return err("page fetch failed")

        loaded_item_count = sum(len(store.pages.get(p, [])) for p in store.loaded_pages)
        tot = max(store.total_known, loaded_item_count)
        pg  = max(1, min(page, store.total_pages()))
        hdr = _t(lang,"search_header", q=q, total=tot)
        txt = _render_page(store, pg, hdr, _render_search)
        if pg < store.total_pages():
            _prefetch_page(store, pg + 1, _st_fetcher)
        if pg > 1:
            _prefetch_page(store, pg - 1, _st_fetcher)
        return _r(txt, pg, store.total_pages(), store.total_pages()>1, skey)

    return _r(_t(lang,"unknown_cmd", cmd=cmd or "(empty)"))

class FunstatPlugin(BasePlugin):

    def __init__(self):
        super().__init__()
        self._token: str     = ""
        self._lang: str      = "ru"
        self._page_size: int = 20
        self._fs: FunstatClient | None = None

    def on_plugin_load(self):
        self.add_on_send_message_hook()
        self._token = self.get_setting("token") or ""
        lang_index  = self.get_setting("lang") or 0
        langs       = ["ru", "en"]
        self._lang  = langs[lang_index] if isinstance(lang_index, int) and 0 <= lang_index < len(langs) else "ru"
        ps          = self.get_setting("page_size")
        self._page_size = int(ps) if ps and str(ps).isdigit() and int(ps) > 0 else 20
        cs = self.get_setting("cache_max_size")
        if cs and str(cs).isdigit() and int(cs) > 0:
            _api_cache.set_max_size(int(cs))
        self._fs    = FunstatClient(self._token)
        self._register_menu_items()
        log(f"[funstat] loaded. {_api_cache.stats()}")

    def _rebuild(self, token: str):
        self._token = token; self._fs = FunstatClient(token)

    def _set_lang(self, index: int):
        langs = ["ru","en"]; self._lang = langs[index] if 0 <= index < len(langs) else "ru"

    def _set_page_size(self, value: str):
        try:
            ps = int(value)
            if ps > 0: self._page_size = ps
        except Exception:
            pass

    def _set_cache_size(self, value: str):
        try:
            n = int(value)
            if n > 0:
                _api_cache.set_max_size(n)
                log(f"[funstat] cache max_size set to {n}")
        except Exception:
            pass

    def _clear_cache_setting(self, view=None):
        if self._fs:
            self._fs.clear_all_cache()
        else:
            _api_cache.clear()
            _user_cache.clear()
            with _stores_lock:
                _stores.clear()
        log("[funstat] settings: all cache cleared")

    def _cache_stats_text(self) -> str:
        lang = self._lang
        try:
            users   = _user_cache.size()
            hidden  = _user_cache.hidden_count()
            total   = _api_cache.size()
            cats    = _api_cache.categorized_stats()
            kb      = _api_cache.size_bytes() // 1024
            stores  = len(_stores)
            cleared_dt = datetime.fromtimestamp(_api_cache.last_cleared).strftime("%d.%m %H:%M")
            lines = [
                f"• {_t(lang, 'cache_users',  n=users)} ({_t(lang, 'cache_hidden', n=hidden).strip()})",
                f"• {_t(lang, 'cache_total',  n=total)}",
            ]
            for cat, cnt in sorted(cats.items()):
                if cnt > 0:
                    lines.append(f"  └ {cat}: {cnt}")
            lines += [
                f"• {_t(lang, 'cache_weight',     kb=kb)}",
                f"• {_t(lang, 'cache_stores',     n=stores)}",
                f"• {_t(lang, 'cache_cleared_at', dt=cleared_dt)}",
            ]
            return "\n".join(lines)
        except Exception as e:
            return f"• ⏱ Таймаут / ошибка: {e}" if lang == "ru" else f"• ⏱ Timeout / error: {e}"

    def create_settings(self) -> List[Any]:
        from ui.settings import Text
        lang = self._lang
        return [
            Divider(),
            Header(text="настройки funstat"),
            Input(key="token", text="API Token (funstat)",
                  default="", subtext="Получить: .help",
                  icon="msg_text", on_change=self._rebuild),
            Selector(key="lang", text="Язык / Language",
                     default=0, items=["ru", "en"],
                     icon="msg_text", on_change=self._set_lang),
            Input(key="page_size", text="Размер страницы / Page size",
                  default="20", subtext="Элементов на странице (по умолчанию 20)",
                  icon="msg_text", on_change=self._set_page_size),
            Divider(),
            Header(text="📦 кеш / cache"),
            Input(key="cache_max_size", text="Макс. записей / Max entries",
                  default="2000", subtext="По умолчанию 2000 (без TTL, бессмертный)",
                  icon="msg_text", on_change=self._set_cache_size),
            Text(text=f"📊 {_t(lang, 'cache_stats_title')}", icon="msg_info",
                 on_click=self._show_cache_stats_alert),
            Text(text="🗑 Очистить весь кеш / Clear all cache", icon="msg_delete",
                 red=True, on_click=self._clear_cache_setting),
            Divider(),
            Header(text="🕐 история / history"),
            Text(text="📋 Открыть историю поисков", icon="msg_search",
                 on_click=self._open_history_settings),
        ]

    def _show_cache_stats_alert(self, view=None):
        from client_utils import get_last_fragment
        from org.telegram.messenger import AndroidUtilities
        lang = self._lang

        def build():
            try:
                fragment = get_last_fragment()
                if not fragment: return
                act = fragment.getParentActivity()
                if not act: return
                sw = AndroidUtilities.displaySize.x
                s  = self._build_dialog(act, sw, lang=lang)
                tv = s["tv"]
                title = f"<b>{_t(lang, 'cache_stats_title')}</b>"
                body  = self._cache_stats_text()
                self._set_html(tv, title + "\n" + body)
            except Exception:
                log(f"FunstatPlugin._show_cache_stats_alert: {traceback.format_exc()}")

        run_on_ui_thread(build)

    def _open_history_settings(self, view=None):
        self._show_history_alert()

    def _show_history_alert(self):
        from client_utils import get_last_fragment
        from org.telegram.messenger import AndroidUtilities
        lang = self._lang

        def build():
            try:
                fragment = get_last_fragment()
                if not fragment: return
                act = fragment.getParentActivity()
                if not act: return
                sw = AndroidUtilities.displaySize.x
                s  = self._build_dialog(act, sw, lang=lang)
                tv, root = s["tv"], s["root"]

                title_html = f"<b>{_t(lang,'history_title')}</b>"

                if not _search_history:
                    self._set_html(tv, title_html + "\n" + _t(lang,'history_empty'))
                    return

                self._set_html(tv, title_html)

                from android.widget import LinearLayout, TextView
                from android.graphics.drawable import GradientDrawable
                from android.view import Gravity
                from org.telegram.ui.Components import LayoutHelper
                from org.telegram.messenger import AndroidUtilities as AU
                from org.telegram.ui.ActionBar import Theme
                from android.graphics import Typeface
                from java import dynamic_proxy
                from android.view import View

                blue = Theme.getColor(Theme.key_windowBackgroundWhiteBlueText)

                class Clicker(dynamic_proxy(View.OnClickListener)):
                    def __init__(self, fn):
                        super().__init__(); self.fn = fn
                    def onClick(self, v): self.fn()

                for cmd in _search_history[:30]:
                    bg = GradientDrawable()
                    bg.setColor((blue & 0x00FFFFFF) | 0x12000000)
                    bg.setCornerRadius(float(AU.dp(4)))
                    bg.setStroke(AU.dp(1), (blue & 0x00FFFFFF) | 0x28000000)
                    btn = TextView(act)
                    btn.setText(cmd)
                    btn.setTextColor(blue)
                    btn.setTextSize(1, 11.5)
                    btn.setSingleLine(True)
                    btn.setBackground(bg)
                    btn.setPadding(AU.dp(8), AU.dp(6), AU.dp(8), AU.dp(6))
                    lp = LinearLayout.LayoutParams(-1, -2)
                    lp.setMargins(0, AU.dp(2), 0, 0)
                    btn.setOnClickListener(Clicker(
                        lambda c=cmd: self._open_new_alert(c)
                    ))
                    root.addView(btn, LayoutHelper.createLinear(-1, -2, 0, 2, 0, 0))
            except Exception:
                log(f"FunstatPlugin._show_history_alert: {traceback.format_exc()}")

        run_on_ui_thread(build)
        
    def _register_menu_items(self):
        try:
            from base_plugin import MenuItemData, MenuItemType
            self.add_menu_item(MenuItemData(
                menu_type=MenuItemType.CHAT_ACTION_MENU,
                text=_t(self._lang,"search_in_funstat"),
                icon="msg_search", priority=50,
                on_click=self._on_menu_search_peer,
            ))
        except Exception:
            log(f"FunstatPlugin._register_menu_items: {traceback.format_exc()}")

    def _on_menu_search_peer(self, peer=None):
        try:
            pid = None
            if peer:
                try:
                    entries = {str(k): str(v) for k, v in peer.entrySet()}
                except Exception:
                    log(f"[funstat] _on_menu_search_peer: peer={peer!r}")
                for key in ("chatId", "user_id", "userId", "peer_id", "peerId", "dialog_id", "id", "uid"):
                    try:
                        val = peer.get(key)
                        if val is not None:
                            pid = int(val)
                            break
                    except Exception:
                        pass
                is_group = False
                if pid is not None and pid < 0:
                    is_group = True
                    pid = abs(pid)
                    pid_s = str(pid)
                    if pid_s.startswith("100") and len(pid_s) > 10:
                        pid = int(pid_s[3:])
                elif pid is not None:
                    try:
                        if peer.get("chatFull") is not None or peer.get("chat") is not None:
                            is_group = True
                    except Exception:
                        pass

                if is_group:
                    log(f"[funstat] _on_menu_search_peer: pid={pid} is group/channel")
                    self._open_new_alert(f".fs gi -g {pid}")
                    return

                log(f"[funstat] _on_menu_search_peer: resolved pid={pid}")

            self._open_new_alert(f".fs s {pid}" if pid else ".fs s ")
        except Exception:
            log(f"FunstatPlugin._on_menu_search_peer: {traceback.format_exc()}")

    def _build_dialog(self, act, sw: int, lang: str = "ru") -> dict:
        from android.widget import LinearLayout, TextView, ScrollView
        from android.text import Html
        from android.text.method import LinkMovementMethod
        from org.telegram.ui.Components import LayoutHelper
        from android.view import Gravity
        from java import jclass
        from org.telegram.messenger import AndroidUtilities
        from org.telegram.ui.ActionBar import Theme

        font_size = max(14.0, min(22.0, sw / 24.0)) * 0.8

        root = LinearLayout(act)
        root.setOrientation(LinearLayout.VERTICAL)
        root.setPadding(*[AndroidUtilities.dp(16)] * 4)

        scroll         = ScrollView(act)
        scroll_content = LinearLayout(act)
        scroll_content.setOrientation(LinearLayout.VERTICAL)

        tv = TextView(act)
        tv.setMovementMethod(LinkMovementMethod.getInstance())
        tv.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
        tv.setLinkTextColor(Theme.getColor(Theme.key_windowBackgroundWhiteBlueText))
        tv.setTextSize(1, font_size)
        tv.setGravity(Gravity.START)

        try:
            from android.text.style import URLSpan
            from android.view import MotionEvent
            from android.content import Intent
            from android.net import Uri
            from android.text.method import LinkMovementMethod as LMM

            class TelegramLinkHandler(LMM):
                def onTouchEvent(self, widget, buffer, event):
                    action = event.getAction()
                    if action in (MotionEvent.ACTION_UP, MotionEvent.ACTION_DOWN):
                        x     = int(event.getX()) - widget.getTotalPaddingLeft() + widget.getScrollX()
                        y     = int(event.getY()) - widget.getTotalPaddingTop()  + widget.getScrollY()
                        lay   = widget.getLayout()
                        line  = lay.getLineForVertical(y)
                        off   = lay.getOffsetForHorizontal(line, x)
                        spans = buffer.getSpans(off, off, URLSpan)
                        if spans and action == MotionEvent.ACTION_UP:
                            url    = spans[0].getURL()
                            intent = Intent(Intent.ACTION_VIEW, Uri.parse(url))
                            intent.setPackage(act.getPackageName())
                            try:
                                act.startActivity(intent)
                            except Exception:
                                act.startActivity(Intent(Intent.ACTION_VIEW, Uri.parse(url)))
                            return True
                    return super().onTouchEvent(widget, buffer, event)

            tv.setMovementMethod(TelegramLinkHandler())
        except Exception:
            pass

        scroll_content.addView(tv, LayoutHelper.createLinear(-1, -2))
        scroll.addView(scroll_content)

        root.addView(scroll, LinearLayout.LayoutParams(-1, -2))

        AlertDialog = jclass("org.telegram.ui.ActionBar.AlertDialog")
        builder     = AlertDialog.Builder(act)
        builder.setView(root)
        builder.setPositiveButton(_t(lang, "btn_close"), None)
        dialog = builder.create()
        dialog.setCanceledOnTouchOutside(True)
        dialog.show()

        try:
            window = dialog.getWindow()
            if window:
                lp       = window.getAttributes()
                lp.width = int(sw * 0.92)
                window.setAttributes(lp)
        except Exception:
            pass

        return {"dialog": dialog, "tv": tv, "root": root, "act": act}

    def _set_html(self, tv, html: str):
        from android.text import Html
        tv.setText(Html.fromHtml(html.replace("\n","<br>"), Html.FROM_HTML_MODE_LEGACY))

    def _clear_dynamic(self, root):
        try:
            while root.getChildCount() > 1:
                root.removeViewAt(root.getChildCount() - 1)
        except Exception:
            log(f"FunstatPlugin._clear_dynamic: {traceback.format_exc()}")

    def _add_error_buttons(self, root, act, cmd: str, uid, lang: str,
                       prev_cmd: str | None = None, is_hidden: bool = False):
        try:
            from android.widget import LinearLayout, TextView
            from android.graphics.drawable import GradientDrawable
            from android.view import Gravity
            from org.telegram.ui.Components import LayoutHelper
            from org.telegram.messenger import AndroidUtilities
            from org.telegram.ui.ActionBar import Theme
            from android.graphics import Typeface
            from java import dynamic_proxy
            from android.view import View as _View

            class _Clicker(dynamic_proxy(_View.OnClickListener)):
                def __init__(self, fn):
                    super().__init__()
                    self.fn = fn
                def onClick(self, v):
                    self.fn()

            blue = Theme.getColor(Theme.key_windowBackgroundWhiteBlueText)
            red  = Theme.getColor(Theme.key_text_RedRegular)
            grey = Theme.getColor(Theme.key_dialogTextGray3)

            def make_btn(label, color):
                bg = GradientDrawable()
                bg.setColor((color & 0x00FFFFFF) | 0x15000000)
                bg.setCornerRadius(float(AndroidUtilities.dp(4)))
                bg.setStroke(AndroidUtilities.dp(1), (color & 0x00FFFFFF) | 0x35000000)
                b = TextView(act)
                b.setText(label)
                b.setTextColor(color)
                b.setTextSize(1, 12.5)
                b.setTypeface(Typeface.DEFAULT_BOLD)
                b.setGravity(Gravity.CENTER)
                b.setSingleLine(True)
                b.setBackground(bg)
                b.setPadding(AndroidUtilities.dp(4), AndroidUtilities.dp(7),
                             AndroidUtilities.dp(4), AndroidUtilities.dp(7))
                return b

            def add_row(*btns):
                row = LinearLayout(act)
                row.setOrientation(LinearLayout.HORIZONTAL)
                for b in btns:
                    lp = LinearLayout.LayoutParams(0, -2, 1.0)
                    lp.setMargins(AndroidUtilities.dp(2), AndroidUtilities.dp(1),
                                  AndroidUtilities.dp(2), AndroidUtilities.dp(1))
                    row.addView(b, lp)
                root.addView(row, LayoutHelper.createLinear(-1, -2, 0, 2, 0, 0))

            btn_retry = make_btn(_t(lang, "btn_retry"), blue)
            btn_evict = make_btn(_t(lang, "btn_evict_and_retry"), red)
            btn_copy  = make_btn("📋 " + ("Копировать лог" if lang == "ru" else "Copy log"), grey)

            btn_retry.setOnClickListener(_Clicker(
                lambda: self._update_dialog(root, act, cmd, btn_view=btn_retry)
            ))

            def _do_evict():
                btn_evict.setText("⏳")
                def _work():
                    if self._fs:
                        if uid:
                            self._fs.evict_user_cache(uid)
                        else:
                            self._fs.clear_all_cache()
                    run_on_ui_thread(lambda: self._update_dialog(root, act, cmd))
                threading.Thread(target=_work, daemon=True).start()

            btn_evict.setOnClickListener(_Clicker(_do_evict))

            def _do_copy():
                try:
                    tv_ref = self._find_tv(root)
                    plain  = re.sub(r"<[^>]+>", "",
                                    f"cmd: {cmd}\n{str(tv_ref.getText()) if tv_ref else ''}")
                    from android.content import ClipData
                    act.getSystemService(act.CLIPBOARD_SERVICE).setPrimaryClip(
                        ClipData.newPlainText("funstat_log", plain)
                    )
                except Exception:
                    log(f"[funstat] copy_log: {traceback.format_exc()}")

            btn_copy.setOnClickListener(_Clicker(_do_copy))

            add_row(btn_retry, btn_evict)
            add_row(btn_copy)

            if prev_cmd:
                btn_back = make_btn(_t(lang, "btn_back"), grey)
                btn_back.setOnClickListener(_Clicker(
                    lambda: self._update_dialog(root, act, prev_cmd, btn_view=btn_back)
                ))
                add_row(btn_back)

        except Exception:
            log(f"[funstat] _add_error_buttons EXCEPTION: {traceback.format_exc()}")

    def _add_back_to_profile_btn(self, root, act, uid: int, lang: str):
        try:
            from android.widget import LinearLayout, TextView
            from android.graphics.drawable import GradientDrawable
            from android.view import Gravity
            from org.telegram.ui.Components import LayoutHelper
            from org.telegram.messenger import AndroidUtilities
            from org.telegram.ui.ActionBar import Theme
            from android.graphics import Typeface
            from java import dynamic_proxy
            from android.view import View

            blue = Theme.getColor(Theme.key_windowBackgroundWhiteBlueText)
            bg   = GradientDrawable()
            bg.setColor((blue & 0x00FFFFFF) | 0x18000000)
            bg.setCornerRadius(float(AndroidUtilities.dp(4)))
            bg.setStroke(AndroidUtilities.dp(1), (blue & 0x00FFFFFF) | 0x40000000)

            class Clicker(dynamic_proxy(View.OnClickListener)):
                def __init__(self, fn):
                    super().__init__(); self.fn = fn
                def onClick(self, v): self.fn()

            btn = TextView(act)
            btn.setText(_t(lang, "evicted_back_profile"))
            btn.setTextColor(blue)
            btn.setTextSize(1, 13.0)
            btn.setTypeface(Typeface.DEFAULT_BOLD)
            btn.setGravity(Gravity.CENTER)
            btn.setBackground(bg)
            btn.setPadding(AndroidUtilities.dp(8), AndroidUtilities.dp(10),
                           AndroidUtilities.dp(8), AndroidUtilities.dp(10))

            def go_back(_u=uid, _r=root, _a=act):
                self._update_dialog(_r, _a, f".fs s {_u}")

            btn.setOnClickListener(Clicker(go_back))
            row = LinearLayout(act)
            row.setOrientation(LinearLayout.HORIZONTAL)
            lp  = LinearLayout.LayoutParams(-1, -2)
            lp.setMargins(AndroidUtilities.dp(2), AndroidUtilities.dp(6),
                          AndroidUtilities.dp(2), AndroidUtilities.dp(2))
            row.addView(btn, lp)
            root.addView(row, LayoutHelper.createLinear(-1, -2, 0, 4, 0, 0))
        except Exception:
            log(f"FunstatPlugin._add_back_to_profile_btn: {traceback.format_exc()}")

    def _add_names_action_btns(self, root, act, names_data: dict, usernames_data: dict, lang: str):
        pass

    def _make_bar_ctx(self, act):
        from android.widget import LinearLayout, TextView
        from android.graphics.drawable import GradientDrawable
        from android.view import Gravity
        from org.telegram.ui.Components import LayoutHelper
        from org.telegram.messenger import AndroidUtilities
        from org.telegram.ui.ActionBar import Theme
        from android.graphics import Typeface
        from java import dynamic_proxy
        from android.view import View

        blue = Theme.getColor(Theme.key_windowBackgroundWhiteBlueText)
        grey = Theme.getColor(Theme.key_dialogTextGray3)

        def make_bg(color=None):
            c = color if color is not None else blue
            bg = GradientDrawable()
            bg.setColor((c & 0x00FFFFFF) | 0x15000000)
            bg.setCornerRadius(float(AndroidUtilities.dp(4)))
            bg.setStroke(AndroidUtilities.dp(1), (c & 0x00FFFFFF) | 0x30000000)
            return bg

        class Clicker(dynamic_proxy(View.OnClickListener)):
            def __init__(self, fn):
                super().__init__(); self.fn = fn
            def onClick(self, v): self.fn()

        def make_btn(label, color=None, size=12.0):
            c = color if color is not None else blue
            b = TextView(act)
            b.setText(label); b.setTextColor(c)
            b.setTextSize(1, size); b.setTypeface(Typeface.DEFAULT_BOLD)
            b.setGravity(Gravity.CENTER); b.setSingleLine(True)
            b.setBackground(make_bg(c))
            b.setPadding(AndroidUtilities.dp(4), AndroidUtilities.dp(7),
                         AndroidUtilities.dp(4), AndroidUtilities.dp(7))
            return b

        def make_row(root, btns, weight=True):
            row = LinearLayout(act)
            row.setOrientation(LinearLayout.HORIZONTAL)
            for b in btns:
                lp = (LinearLayout.LayoutParams(0, -2, 1.0) if weight
                      else LinearLayout.LayoutParams(-1, -2))
                lp.setMargins(AndroidUtilities.dp(2), AndroidUtilities.dp(1),
                              AndroidUtilities.dp(2), AndroidUtilities.dp(1))
                row.addView(b, lp)
            root.addView(row, LayoutHelper.createLinear(-1, -2, 0, 2, 0, 0))
            return row

        return dict(
            blue=blue, grey=grey,
            make_bg=make_bg, Clicker=Clicker,
            make_btn=make_btn, make_row=make_row,
            AU=AndroidUtilities, LayoutHelper=LayoutHelper,
            LinearLayout=LinearLayout, TextView=TextView,
            Gravity=Gravity, Typeface=Typeface,
        )

    def _add_bottom_bar(self, root, act, uid: int, lang: str, current_cmd: str | None = None):
        try:
            ctx = self._make_bar_ctx(act)
            make_btn = ctx["make_btn"]; make_row = ctx["make_row"]
            Clicker  = ctx["Clicker"]; grey = ctx["grey"]
            AU = ctx["AU"]; LayoutHelper = ctx["LayoutHelper"]
            LinearLayout = ctx["LinearLayout"]

            def run(cmd, btn, _prev=current_cmd):
                self._update_dialog(root, act, cmd, btn_view=btn, prev_cmd=_prev)

            def names_action(btn, u=uid):
                try: btn.setText("⏳")
                except Exception: pass
                def work():
                    nd  = self._fs.get_names(u) or {}
                    usd = self._fs.get_usernames(u) or {}
                    txt = _fmt_names_and_usernames(nd, usd, lang)
                    def done():
                        self._apply_result(root, act, txt, 1, 1, False, "", "")
                        self._add_bottom_bar(root, act, u, lang, current_cmd=f".fs s {u}")
                        self._add_names_action_btns(root, act, nd, usd, lang)
                    run_on_ui_thread(done)
                threading.Thread(target=work, daemon=True).start()

            b_prof  = make_btn(_t(lang,"btn_profile"))
            b_names = make_btn(_t(lang,"btn_names"))
            b_prof.setOnClickListener(Clicker(lambda _b=b_prof: run(f".fs s {uid}", _b)))
            b_names.setOnClickListener(Clicker(lambda _b=b_names: names_action(_b)))
            make_row(root, [b_prof, b_names])

            b_grp = make_btn(_t(lang,"btn_groups"))
            b_msg = make_btn(_t(lang,"btn_messages"))
            b_grp.setOnClickListener(Clicker(lambda _b=b_grp: run(f".fs chats -u {uid}", _b)))
            b_msg.setOnClickListener(Clicker(lambda _b=b_msg: run(f".fs msg -u {uid}", _b)))
            make_row(root, [b_grp, b_msg])

            b_rep = make_btn(_t(lang,"btn_reputation"))
            b_cg  = make_btn(_t(lang,"btn_common"))
            b_gif = make_btn(_t(lang,"btn_gifts"))
            b_rep.setOnClickListener(Clicker(lambda _b=b_rep: run(f".fs rep -u {uid}", _b)))
            b_cg.setOnClickListener(Clicker(lambda _b=b_cg:  run(f".fs cg -u {uid}", _b)))
            b_gif.setOnClickListener(Clicker(lambda _b=b_gif: run(f".fs gifts -u {uid}", _b)))
            make_row(root, [b_rep, b_cg, b_gif])

            b_copy = make_btn("📋 " + ("Копировать" if lang == "ru" else "Copy"), size=11.5)
            b_copy.setOnClickListener(Clicker(lambda: self._do_copy(root, act)))
            cp_lp = LinearLayout.LayoutParams(-1, -2)
            cp_lp.setMargins(AU.dp(2), AU.dp(1), AU.dp(2), AU.dp(1))
            cp_row = LinearLayout(act)
            cp_row.setOrientation(LinearLayout.HORIZONTAL)
            cp_row.addView(b_copy, cp_lp)
            root.addView(cp_row, LayoutHelper.createLinear(-1, -2, 0, 1, 0, 0))

            b_evict = make_btn(_t(lang, "btn_evict_cache"), color=grey, size=11.5)

            def do_evict(_b=b_evict):
                try: _b.setText("⏳")
                except Exception: pass
                def work():
                    if self._fs: self._fs.evict_user_cache(uid)
                    msg = _t(lang, "cache_evicted", uid=uid)
                    def done():
                        self._set_html(self._find_tv(root), msg)
                        self._clear_dynamic(root)
                        self._add_back_to_profile_btn(root, act, uid, lang)
                    run_on_ui_thread(done)
                threading.Thread(target=work, daemon=True).start()

            b_evict.setOnClickListener(Clicker(do_evict))
            ev_lp = LinearLayout.LayoutParams(-1, -2)
            ev_lp.setMargins(AU.dp(2), AU.dp(2), AU.dp(2), AU.dp(2))
            ev_row = LinearLayout(act)
            ev_row.setOrientation(LinearLayout.HORIZONTAL)
            ev_row.addView(b_evict, ev_lp)
            root.addView(ev_row, LayoutHelper.createLinear(-1, -2, 0, 1, 0, 0))

        except Exception:
            log(f"FunstatPlugin._add_bottom_bar: {traceback.format_exc()}")

    def _add_group_bar(self, root, act, gid: int, lang: str, current_cmd: str | None = None):
        try:
            ctx = self._make_bar_ctx(act)
            make_btn = ctx["make_btn"]; Clicker = ctx["Clicker"]
            grey = ctx["grey"]; AU = ctx["AU"]
            LayoutHelper = ctx["LayoutHelper"]
            LinearLayout = ctx["LinearLayout"]

            def run(cmd, btn, _prev=current_cmd):
                self._update_dialog(root, act, cmd, btn_view=btn, prev_cmd=_prev)

            b_gi = make_btn("🏠 " + ("Группа"    if lang == "ru" else "Group"))
            b_gm = make_btn("👥 " + ("Участники" if lang == "ru" else "Members"))
            b_gi.setOnClickListener(Clicker(lambda _b=b_gi: run(f".fs gi -g {gid}", _b)))
            b_gm.setOnClickListener(Clicker(lambda _b=b_gm: run(f".fs gm -g {gid}", _b)))
            ctx["make_row"](root, [b_gi, b_gm])

            b_copy = make_btn("📋 " + ("Копировать" if lang == "ru" else "Copy"), size=11.5)
            b_copy.setOnClickListener(Clicker(lambda: self._do_copy(root, act)))
            cp_lp = LinearLayout.LayoutParams(-1, -2)
            cp_lp.setMargins(AU.dp(2), AU.dp(1), AU.dp(2), AU.dp(1))
            cp_row = LinearLayout(act)
            cp_row.setOrientation(LinearLayout.HORIZONTAL)
            cp_row.addView(b_copy, cp_lp)
            root.addView(cp_row, LayoutHelper.createLinear(-1, -2, 0, 1, 0, 0))

            b_evict = make_btn(_t(lang, "btn_evict_cache"), color=grey, size=11.5)

            def do_evict_group(_b=b_evict):
                try: _b.setText("⏳")
                except Exception: pass
                def work():
                    if self._fs: self._fs.evict_group_cache(gid)
                    msg = (f"✅ Кеш группы {gid} очищен" if lang == "ru"
                           else f"✅ Cache for group {gid} cleared")
                    def done():
                        self._set_html(self._find_tv(root), msg)
                        self._clear_dynamic(root)
                        self._add_group_bar(root, act, gid, lang,
                                            current_cmd=f".fs gi -g {gid}")
                    run_on_ui_thread(done)
                threading.Thread(target=work, daemon=True).start()

            b_evict.setOnClickListener(Clicker(do_evict_group))
            ev_lp = LinearLayout.LayoutParams(-1, -2)
            ev_lp.setMargins(AU.dp(2), AU.dp(2), AU.dp(2), AU.dp(2))
            ev_row = LinearLayout(act)
            ev_row.setOrientation(LinearLayout.HORIZONTAL)
            ev_row.addView(b_evict, ev_lp)
            root.addView(ev_row, LayoutHelper.createLinear(-1, -2, 0, 1, 0, 0))

        except Exception:
            log(f"FunstatPlugin._add_group_bar: {traceback.format_exc()}")

    def _rebuild_pagination(self, root, act, tv,
                             cur_pg: int, tot_pg: int,
                             cmd_base: str, lang: str, store_key: str,
                             uid, extra: dict | None = None,
                             step_holder: list | None = None,
                             gid: int | None = None):
        log(f"[funstat] _rebuild_pagination: pg={cur_pg}/{tot_pg} uid={uid} gid={gid}")
        if gid:
            self._add_group_bar(root, act, gid, lang, current_cmd=cmd_base)
        elif uid:
            self._add_bottom_bar(root, act, uid, lang, current_cmd=cmd_base)
        if "gifts" in cmd_base:
            self._add_gift_filters(root, act, tv, cmd_base, lang, store_key, uid,
                                   (extra or {}).get("gift_filter", ""))
        self._add_pag_row(root, act, tv, cur_pg, tot_pg, cmd_base, lang,
                          store_key, uid, step_holder=step_holder)

    def _add_gift_filters(self, root, act, tv,
                           cmd_base: str, lang: str, store_key: str,
                           uid, active_filter: str):
        try:
            from android.widget import LinearLayout, TextView
            from android.graphics.drawable import GradientDrawable
            from android.view import Gravity
            from org.telegram.ui.Components import LayoutHelper
            from org.telegram.messenger import AndroidUtilities
            from org.telegram.ui.ActionBar import Theme
            from android.graphics import Typeface
            from java import dynamic_proxy
            from android.view import View

            blue = Theme.getColor(Theme.key_windowBackgroundWhiteBlueText)
            grey = Theme.getColor(Theme.key_dialogTextGray3)

            class Clicker(dynamic_proxy(View.OnClickListener)):
                def __init__(self, fn):
                    super().__init__(); self.fn = fn
                def onClick(self, v): self.fn()

            row = LinearLayout(act)
            row.setOrientation(LinearLayout.HORIZONTAL)
            row.setGravity(Gravity.CENTER)
            row.setPadding(0, AndroidUtilities.dp(4), 0, AndroidUtilities.dp(2))

            filters = [
                ("",       _t(lang, "gifts_filter_all")),
                ("sent",   _t(lang, "gifts_filter_sent")),
                ("recv",   _t(lang, "gifts_filter_recv")),
                ("mutual", _t(lang, "gifts_filter_mutual")),
            ]
            for ft, label in filters:
                is_active = (ft == active_filter)
                col = blue if is_active else grey
                bg  = GradientDrawable()
                bg.setColor((col & 0x00FFFFFF) | (0x30000000 if is_active else 0x10000000))
                bg.setCornerRadius(float(AndroidUtilities.dp(4)))
                bg.setStroke(AndroidUtilities.dp(1), (col & 0x00FFFFFF) | 0x40000000)
                btn = TextView(act)
                btn.setText(label); btn.setTextColor(col)
                btn.setTextSize(1, 11.0)
                btn.setGravity(Gravity.CENTER); btn.setSingleLine(True)
                btn.setBackground(bg)
                btn.setPadding(AndroidUtilities.dp(6), AndroidUtilities.dp(5),
                               AndroidUtilities.dp(6), AndroidUtilities.dp(5))
                if not is_active:
                    base = re.sub(r"\s+-t\s+\S+", "", cmd_base).strip()
                    new_cmd = f"{base} -t {ft}" if ft else base
                    btn.setOnClickListener(Clicker(
                        lambda c=new_cmd, _b=btn:
                        self._update_dialog(root, act, c, btn_view=_b)
                    ))
                lp = LinearLayout.LayoutParams(0, -2, 1.0)
                lp.setMargins(AndroidUtilities.dp(2), 0, AndroidUtilities.dp(2), 0)
                row.addView(btn, lp)

            root.addView(row, LayoutHelper.createLinear(-1, -2, 0, 2, 0, 0))
        except Exception:
            log(f"FunstatPlugin._add_gift_filters: {traceback.format_exc()}")

    def _add_pag_row(self, root, act, tv,
                      cur_pg: int, tot_pg: int,
                      cmd_base: str, lang: str, store_key: str,
                      uid, step_holder: list | None = None):
        try:
            from android.widget import LinearLayout, TextView
            from android.graphics.drawable import GradientDrawable
            from android.view import Gravity
            from org.telegram.ui.Components import LayoutHelper
            from org.telegram.messenger import AndroidUtilities
            from org.telegram.ui.ActionBar import Theme
            from android.graphics import Typeface
            from java import dynamic_proxy
            from android.view import View

            blue = Theme.getColor(Theme.key_windowBackgroundWhiteBlueText)
            grey = Theme.getColor(Theme.key_dialogTextGray3)

            def make_bg(enabled: bool):
                col = blue if enabled else grey
                bg  = GradientDrawable()
                bg.setColor((col & 0x00FFFFFF) | 0x18000000)
                bg.setStroke(AndroidUtilities.dp(1), (col & 0x00FFFFFF) | 0x40000000)
                bg.setCornerRadius(float(AndroidUtilities.dp(4)))
                return bg

            class Clicker(dynamic_proxy(View.OnClickListener)):
                def __init__(self, fn):
                    super().__init__(); self.fn = fn
                def onClick(self, v): self.fn()

            row = LinearLayout(act)
            row.setOrientation(LinearLayout.HORIZONTAL)
            row.setGravity(Gravity.CENTER)
            row.setPadding(0, AndroidUtilities.dp(8), 0, AndroidUtilities.dp(4))

            _STEPS = [1, 10, 100, 1000]
            if step_holder is None:
                step_holder = [0]

            step_btn = TextView(act)
            step_btn.setText(f"×{_STEPS[step_holder[0]]}")
            step_btn.setTextSize(1, 11.0)
            step_btn.setGravity(Gravity.CENTER)
            step_btn.setTextColor(blue)
            step_btn.setBackground(make_bg(True))
            step_btn.setPadding(AndroidUtilities.dp(7), AndroidUtilities.dp(8),
                                AndroidUtilities.dp(7), AndroidUtilities.dp(8))

            def cycle_step(_b=step_btn, _sh=step_holder, _steps=_STEPS):
                _sh[0] = (_sh[0] + 1) % len(_steps)
                _b.setText(f"×{_steps[_sh[0]]}")

            step_btn.setOnClickListener(Clicker(cycle_step))

            def make_nav(label: str, delta, abs_target, enabled: bool):
                b = TextView(act)
                b.setText(label); b.setTextSize(1, 16.0)
                b.setGravity(Gravity.CENTER); b.setTypeface(Typeface.DEFAULT_BOLD)
                b.setTextColor(blue if enabled else grey)
                b.setBackground(make_bg(enabled))
                b.setPadding(AndroidUtilities.dp(10), AndroidUtilities.dp(8),
                             AndroidUtilities.dp(10), AndroidUtilities.dp(8))
                if enabled:
                    if delta is not None:
                        def on_click_step(_d=delta, _sh=step_holder, _steps=_STEPS,
                                          _cb=cmd_base, _sk=store_key, _u=uid, _b=b):
                            step   = _steps[_sh[0]]
                            target = max(1, min(cur_pg + _d * step, tot_pg))
                            self._goto_page(target, _cb, lang, _sk, tv, root, act, _u,
                                            btn_view=_b, step_holder=_sh)
                        b.setOnClickListener(Clicker(on_click_step))
                    else:
                        b.setOnClickListener(Clicker(
                            lambda p=abs_target, cb=cmd_base, sk=store_key, u=uid,
                                   _b=b, _sh=step_holder:
                            self._goto_page(p, cb, lang, sk, tv, root, act, u,
                                            btn_view=_b, step_holder=_sh)
                        ))
                lp = LinearLayout.LayoutParams(-2, -2)
                lp.setMargins(AndroidUtilities.dp(3), 0, AndroidUtilities.dp(3), 0)
                row.addView(b, lp)

            make_nav("⏮", None, 1,        cur_pg > 1)
            make_nav("◀",  -1,  None,     cur_pg > 1)

            loaded_pg_count = len(_stores.get(store_key, PaginatedStore("",1)).loaded_pages) if store_key else 0
            page_col = LinearLayout(act)
            page_col.setOrientation(LinearLayout.VERTICAL)
            page_col.setGravity(Gravity.CENTER)

            page_tv = TextView(act)
            page_tv.setText(_t(lang,"page_info", page=cur_pg, total=tot_pg))
            page_tv.setTextColor(Theme.getColor(Theme.key_dialogTextBlack))
            page_tv.setTextSize(1, 13.0); page_tv.setGravity(Gravity.CENTER)
            page_col.addView(page_tv, LayoutHelper.createLinear(-2, -2))

            if loaded_pg_count > 0 and loaded_pg_count < tot_pg:
                loaded_tv = TextView(act)
                loaded_tv.setText(_t(lang, "pages_loaded",
                                     loaded=loaded_pg_count, total_pg=tot_pg))
                loaded_tv.setTextColor(Theme.getColor(Theme.key_dialogTextGray3))
                loaded_tv.setTextSize(1, 10.0); loaded_tv.setGravity(Gravity.CENTER)
                page_col.addView(loaded_tv, LayoutHelper.createLinear(-2, -2))

            lp_center = LinearLayout.LayoutParams(-2, -2)
            lp_center.setMargins(AndroidUtilities.dp(6), 0, AndroidUtilities.dp(6), 0)
            row.addView(page_col, lp_center)

            make_nav("▶",  +1,  None,     cur_pg < tot_pg)
            make_nav("⏭", None, tot_pg,   cur_pg < tot_pg)

            lp_step = LinearLayout.LayoutParams(-2, -2)
            lp_step.setMargins(AndroidUtilities.dp(6), 0, AndroidUtilities.dp(3), 0)
            row.addView(step_btn, lp_step)

            root.addView(row, LayoutHelper.createLinear(-1, -2))
        except Exception:
            log(f"FunstatPlugin._add_pag_row: {traceback.format_exc()}")

    def _goto_page(self, target: int, cmd_base: str, lang: str,
                   store_key: str, tv, root, act, uid,
                   reset: bool = False, btn_view=None,
                   step_holder: list | None = None):
        original_label_holder = [None]
        if btn_view is not None:
            try:
                original_label_holder[0] = btn_view.getText()
                run_on_ui_thread(lambda b=btn_view: b.setText("⏳"))
            except Exception:
                pass

        def restore_btn(b=btn_view, orig=original_label_holder):
            if b is not None and orig[0] is not None:
                try:
                    b.setText(orig[0])
                except Exception:
                    pass

        _sh = step_holder

        def work():
            try:
                full_cmd = f"{cmd_base} -p {target}"
                log(f"[funstat] _goto_page: target={target} reset={reset} cmd={full_cmd!r}")
                result = dispatch(full_cmd, self._fs, lang,
                                  page_size=self._page_size, reset=reset)
                if result is None:
                    log("[funstat] _goto_page: dispatch returned None")
                    run_on_ui_thread(restore_btn)
                    return
                txt = result.get("text","")
                pg  = result.get("page", target)
                tot = result.get("total_pages", 1)
                pag = result.get("paginate", False)
                cb2 = result.get("cmd_base", cmd_base)
                sk2 = result.get("store_key", store_key)
                u2  = result.get("user_id") or uid
                g2  = result.get("group_id")
                is_error  = result.get("is_error", False)
                is_hidden = result.get("is_hidden", False)

                def update():
                    self._set_html(tv, txt)
                    self._clear_dynamic(root)
                    if is_error:
                        prev = cmd_base if cmd_base != full_cmd else None
                        self._add_error_buttons(root, act, full_cmd, u2, lang,
                                                prev_cmd=prev, is_hidden=is_hidden)
                    elif pag:
                        extra = {"gift_filter": result.get("gift_filter", "")} if result.get("gift_filter") is not None else None
                        self._rebuild_pagination(root, act, tv, pg, tot, cb2, lang, sk2, u2,
                                                 extra=extra, step_holder=_sh, gid=g2)
                    elif g2:
                        self._add_group_bar(root, act, g2, lang, current_cmd=cb2)
                    elif u2:
                        self._add_bottom_bar(root, act, u2, lang, current_cmd=cb2)

                run_on_ui_thread(update)

            except Exception:
                log(f"[funstat] _goto_page EXCEPTION: {traceback.format_exc()}")
                run_on_ui_thread(restore_btn)

        threading.Thread(target=work, daemon=True).start()

    def _update_dialog(self, root, act, cmd: str, btn_view=None,
                       prev_cmd: str | None = None):
        tv = self._find_tv(root)

        orig_label_holder = [None]
        if btn_view is not None:
            try:
                orig_label_holder[0] = btn_view.getText()
                run_on_ui_thread(lambda b=btn_view: b.setText("⏳"))
            except Exception:
                pass

        def restore_btn():
            if btn_view is not None and orig_label_holder[0] is not None:
                try:
                    run_on_ui_thread(lambda b=btn_view, t=orig_label_holder[0]: b.setText(t))
                except Exception:
                    pass

        def work():
            try:
                log(f"[funstat] _update_dialog: dispatching cmd={cmd!r}")
                def _tv_upd(html):
                    if tv: run_on_ui_thread(lambda: self._set_html(tv, html))
                result = dispatch(cmd, self._fs, self._lang, page_size=self._page_size,
                                  on_tv_update=_tv_upd)
                if result is None:
                    log("[funstat] _update_dialog: dispatch returned None")
                    restore_btn()
                    return
                txt = result.get("text","")
                pg  = result.get("page", 1)
                tot = result.get("total_pages", 1)
                pag = result.get("paginate", False)
                cb  = result.get("cmd_base", cmd)
                sk  = result.get("store_key","")
                uid = result.get("user_id")
                gid = result.get("group_id")
                is_error  = result.get("is_error", False)
                is_hidden = result.get("is_hidden", False)

                def update():
                    nonlocal tv
                    if tv is None:
                        tv = self._find_tv(root)
                    if tv:
                        self._set_html(tv, txt)
                    self._clear_dynamic(root)
                    if is_error:
                        self._add_error_buttons(root, act, cmd, uid, self._lang,
                                                prev_cmd=prev_cmd, is_hidden=is_hidden)
                    elif pag and tv:
                        extra = {"gift_filter": result.get("gift_filter", "")} if result.get("gift_filter") is not None else None
                        self._rebuild_pagination(root, act, tv, pg, tot, cb, self._lang, sk, uid,
                                                 extra=extra, step_holder=[0], gid=gid)
                    elif gid:
                        self._add_group_bar(root, act, gid, self._lang, current_cmd=cb)
                    elif uid:
                        self._add_bottom_bar(root, act, uid, self._lang, current_cmd=cb)

                run_on_ui_thread(update)

            except Exception:
                log(f"[funstat] _update_dialog EXCEPTION: {traceback.format_exc()}")
                restore_btn()

        threading.Thread(target=work, daemon=True).start()

    def _apply_result(self, root, act, txt: str,
                       pg: int, tot: int, pag: bool,
                       cmd_base: str, store_key: str,
                       uid=None, gid=None):
        tv = self._find_tv(root)
        if tv:
            self._set_html(tv, txt)
        self._clear_dynamic(root)
        if pag and tv:
            self._rebuild_pagination(root, act, tv, pg, tot, cmd_base, self._lang,
                                     store_key, uid, step_holder=[0], gid=gid)
        elif gid:
            self._add_group_bar(root, act, gid, self._lang, current_cmd=cmd_base)
        elif uid:
            self._add_bottom_bar(root, act, uid, self._lang, current_cmd=cmd_base)

    def _do_copy(self, root, act):
        try:
            tv_ref = self._find_tv(root)
            if tv_ref is None:
                return
            import re as _re
            plain = _re.sub(r"<[^>]+>", "", str(tv_ref.getText()))
            from android.content import ClipData
            act.getSystemService(act.CLIPBOARD_SERVICE).setPrimaryClip(
                ClipData.newPlainText("funstat", plain))
        except Exception:
            log(f"FunstatPlugin._do_copy: {traceback.format_exc()}")

    def _find_tv(self, root):
        try:
            from android.widget import ScrollView, LinearLayout, TextView
            scroll = root.getChildAt(0)
            if isinstance(scroll, ScrollView):
                sc = scroll.getChildAt(0)
                if sc and isinstance(sc, LinearLayout):
                    for j in range(sc.getChildCount()):
                        child = sc.getChildAt(j)
                        if isinstance(child, TextView):
                            return child
        except Exception:
            pass
        return None

    def _open_new_alert(self, cmd: str, prev_cmd: str | None = None):
        from client_utils import get_last_fragment
        from org.telegram.messenger import AndroidUtilities

        lang      = self._lang
        page_size = self._page_size
        state: dict = {}
        ready = threading.Event()

        def show_loading():
            try:
                fragment = get_last_fragment()
                if not fragment:
                    log("[funstat] show_loading: no fragment")
                    ready.set()
                    return
                act = fragment.getParentActivity()
                if not act:
                    log("[funstat] show_loading: no activity")
                    ready.set()
                    return
                sw  = AndroidUtilities.displaySize.x
                s   = self._build_dialog(act, sw, lang=lang)
                self._set_html(s["tv"], _t(lang, "loading_init"))
                state.update(s)
                log(f"[funstat] show_loading: state filled, keys={list(state.keys())}")
            except Exception:
                log(f"FunstatPlugin show_loading EXCEPTION: {traceback.format_exc()}")
            finally:
                ready.set()

        def work():
            try:
                log(f"[funstat] _open_new_alert: dispatching cmd={cmd!r}")
                run_on_ui_thread(show_loading)
                ready.wait(timeout=5.0)
                log(f"[funstat] _open_new_alert: ready.wait done, state keys={list(state.keys())}")

                def _tv_update(html):
                    tv = state.get("tv")
                    if tv: run_on_ui_thread(lambda: self._set_html(tv, html))

                result = dispatch(cmd, self._fs, lang, page_size=page_size,
                                  on_tv_update=_tv_update)
                if result is None:
                    log(f"[funstat] _open_new_alert: dispatch returned None, dismissing")
                    d = state.get("dialog")
                    if d: run_on_ui_thread(d.dismiss)
                    return
                txt = result.get("text","")
                pg  = result.get("page", 1)
                tot = result.get("total_pages", 1)
                pag = result.get("paginate", False)
                cb  = result.get("cmd_base", cmd)
                sk  = result.get("store_key","")
                uid = result.get("user_id")
                gid = result.get("group_id")
                is_error  = result.get("is_error", False)
                is_hidden = result.get("is_hidden", False)

                def update():
                    tv   = state.get("tv")
                    root = state.get("root")
                    act  = state.get("act")
                    log(f"[funstat] update(): tv={tv} root={root} act={act}")
                    if not (tv and root and act):
                        log("[funstat] _open_new_alert: state incomplete after wait, skipping update")
                        return
                    self._set_html(tv, txt)
                    if is_error:
                        self._add_error_buttons(root, act, cmd, uid, lang,
                                                prev_cmd=prev_cmd, is_hidden=is_hidden)
                    elif pag:
                        extra = {"gift_filter": result.get("gift_filter", "")} if result.get("gift_filter") is not None else None
                        self._rebuild_pagination(root, act, tv, pg, tot, cb, lang, sk, uid,
                                                extra=extra, step_holder=[0], gid=gid)
                    elif gid:
                        self._add_group_bar(root, act, gid, lang, current_cmd=cb)
                    elif uid:
                        self._add_bottom_bar(root, act, uid, lang, current_cmd=cb)

                run_on_ui_thread(update)
            except Exception as e:
                log(f"[funstat] _open_new_alert EXCEPTION: {traceback.format_exc()}")
                def show_err():
                    tv   = state.get("tv")
                    root = state.get("root")
                    act  = state.get("act")
                    if tv:
                        self._set_html(tv, _t(lang,"error",err=str(e)))
                    if root and act:
                        self._add_error_buttons(root, act, cmd, None, lang,
                                                prev_cmd=prev_cmd)
                run_on_ui_thread(show_err)

        threading.Thread(target=work, daemon=True).start()

    def on_send_message_hook(self, account: int, params: Any) -> HookResult:
        msg_text = getattr(params, "message", None)
        if not (msg_text and msg_text.startswith(".fs")):
            return HookResult(strategy=HookStrategy.PASS)

        if "-s" in msg_text:
            try:
                peer      = getattr(params, "peer",       None)
                reply_to  = getattr(params, "replyToMsg", None)
                acct      = account
                cmd_text  = msg_text
                lang      = self._lang
                page_size = self._page_size

                def work():
                    try:
                        result = dispatch(cmd_text, self._fs, lang, page_size=page_size)
                        if result is None:
                            log("[funstat] send_hook (-s): dispatch returned None")
                            return
                        plain, ents = _html_to_entities(result.get("text", ""))

                        def send_msg():
                            try:
                                from org.telegram.messenger import SendMessagesHelper
                                send_params = SendMessagesHelper.SendMessageParams()
                                send_params.peer       = peer
                                send_params.message    = plain
                                send_params.replyToMsg = reply_to
                                if ents:
                                    java_ents = ArrayList()
                                    for ent in ents:
                                        java_ents.add(ent)
                                    send_params.entities = java_ents
                                SendMessagesHelper.getInstance(acct).sendMessage(send_params)
                            except Exception:
                                log(f"[funstat] send_hook (-s) send_msg: {traceback.format_exc()}")

                        run_on_ui_thread(send_msg)
                    except Exception:
                        log(f"[funstat] send_hook (-s) work: {traceback.format_exc()}")

                threading.Thread(target=work, daemon=True).start()
            except Exception:
                log(f"[funstat] send_hook (-s) setup: {traceback.format_exc()}")
            return HookResult(strategy=HookStrategy.CANCEL)

        log(f"[funstat] send_hook: opening alert for {msg_text!r}")
        self._open_new_alert(msg_text)
        return HookResult(strategy=HookStrategy.CANCEL)