import asyncio
from datetime import datetime
import pytz
import os
from dotenv import load_dotenv

load_dotenv()
chat_id = os.getenv("CHAT_ID")


async def math_handler(bot):
    await bot.send_message(chat_id=chat_id, text="Я РАБОТАЮ!!!")
    alma_ata_tz = pytz.timezone('Asia/Almaty')

    members = await bot.get_chat_administrators(chat_id=chat_id)
    all_usernames = [member.user.username for member in members if member.user.username]

    usernames = [f"@{username}" for username in all_usernames]
    usernames.pop(0)
    bot_msg = " ".join(usernames)

    async def send_math_message():
        await bot.send_message(chat_id=chat_id, text=f"Джиги, матан!\n{bot_msg}")

    async def scheduler():
        while True:
            now = datetime.now(alma_ata_tz).strftime("%H:%M")
            if now == "19:25":
                await send_math_message()
                await asyncio.sleep(60)
            await asyncio.sleep(10)

    await asyncio.create_task(scheduler())
