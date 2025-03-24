from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from .tagall import router as tag_router
from .games import router as games_router

router = Router()
router.include_routers(tag_router, games_router)


@router.message(CommandStart())
async def start_command_handler(message: Message):
    await message.answer("Привiт")
