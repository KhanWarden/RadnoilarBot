from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

router = Router()


@router.message(Command("all"))
async def tag_all_handler(message: Message, bot):
    members = await bot.get_chat_administrators(chat_id=message.chat.id)
    all_usernames = [member.user.username for member in members if member.user.username]

    usernames = [f"@{username}" for username in all_usernames]
    usernames.pop(0)
    bot_msg = " ".join(usernames)
    await message.answer(bot_msg)


@router.message(Command("dota"))
async def tag_doters(message: Message):
    await message.answer("Дотеры, сбор!\n"
                         "@zhsck @NirmanychHimself @Allur51 @mr_irmag @KhanWarden")
