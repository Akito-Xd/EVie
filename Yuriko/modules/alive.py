# Taken From https://github.com/AASFCYBERKING/SerenaRobot/blob/Aasf/SerenaRobot/modules/alive.py
import asyncio
import os
import requests
import datetime
import time
from PIL import Image
from io import BytesIO
from datetime import datetime
import random
from telethon import events, Button, custom, version
from Yuriko.events import register
from Yuriko import telethn as borg
from Yuriko import StartTime, dispatcher
from telethon.tl.types import ChannelParticipantsAdmins

edit_time = 5
""" =======================EvieX====================== """
file1 = "https://telegra.ph/file/5820ee6c948bcaf82dbec.jpg"
file2 = "https://telegra.ph/file/8da11336779e87582e36a.jpg"
file3 = "https://telegra.ph/file/863218f1bbda29ae26104.jpg"
file4 = "https://telegra.ph/file/503f0f8897ce693c0d935.jpg"
file5 = "https://telegra.ph/file/d1df93a4e47f3691cffdc.jpg"
""" =======================Eviex====================== """

BUTTON = [[Button.url("Sopport 👮‍♂️", "https://t.me/EvieXSupport"), Button.url("Updates 🆕", "https://t.me/EvieXUpdates")]]


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)

@register(pattern=("/alive"))
async def hmm(yes):
    chat = await yes.get_chat()
    await yes.delete()
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    pm_caption = "**✨ Hey I'm EvieX**\n"
    pm_caption += f"🧑‍💻 Powered By : [TeamEvieX](https://t.me/TeamEvieX)"
    pm_caption += f"🐍 Python Version :** `{y()}`"
    pm_caption += f"📃 Library Version :** `{o}1"
    pm_caption += f"♻️ Telethon Version :** `{s}`"
    pm_caption += f"💥 Pyrogram Version :** `{z}`"
    BUTTON = [[Button.url("Sopport 👮‍♂️", "https://t.me/EvieXSupport"), Button.url("Updates 🆕", "https://t.me/EvieXUpdates")]]
    on = await borg.send_file(yes.chat_id, file=file1,caption=pm_caption, buttons=BUTTON)
    

    await asyncio.sleep(edit_time)
    ok = await borg.edit_message(yes.chat_id, on, file=file2, buttons=BUTTON) 

    await asyncio.sleep(edit_time)
    ok2 = await borg.edit_message(yes.chat_id, ok, file=file3, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok3 = await borg.edit_message(yes.chat_id, ok2, file=file4, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok4 = await borg.edit_message(yes.chat_id, ok3, file=file5, buttons=BUTTON)

    await asyncio.sleep(edit_time)
    ok5 = await borg.edit_message(yes.chat_id, ok4, file=file1, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok6 = await borg.edit_message(yes.chat_id, ok5, file=file2, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok7 = await borg.edit_message(yes.chat_id, ok6, file=file3, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok8 = await borg.edit_message(yes.chat_id, ok7, file=file4, buttons=BUTTON)
    
    await asyncio.sleep(edit_time)
    ok9 = await borg.edit_message(yes.chat_id, ok8, file=file5, buttons=BUTTON)
