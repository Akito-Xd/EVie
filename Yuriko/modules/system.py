import asyncio
import os
import subprocess
import time

import psutil
import Yuriko.modules.sql.users_sql as sql
from pyrogram import filters

from Yuriko import (DEV_USERS, pbot)
from Yuriko.utils import formatter

# Stats Module

async def bot_sys_stats():
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    stats = f"""
root@im_bb:~$ EvieXBot:
------------------
•📟BOT: {round(process.memory_info()[0] / 1024 ** 2)} MB
•🔋CPU: {cpu}%
•🖲RAM: {mem}%
•💾DISK: {disk}%
•⚡️USERS: {sql.num_users()} users.
•⚙️GROUPS: {sql.num_chats()} groups.
"""
    return stats
