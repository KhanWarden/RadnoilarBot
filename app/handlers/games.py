import asyncio
import random

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from app.models import Phrases

router = Router()


@router.message(Command("whogay"))
async def who_gay_game(message: Message, bot):
    await message.answer(random.choice(Phrases.who_gay))
    await asyncio.sleep(2)
    members = await bot.get_chat_administrators(chat_id=message.chat.id)
    all_usernames = [member.user.username for member in members if member.user.username]
    usernames = [f"@{username}" for username in all_usernames]

    await message.answer(f"{random.choice(Phrases.is_gay).format(random.choice(usernames))}")
