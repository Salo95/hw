from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from config import ADMINS
from .inline_kboard import keyboard

router = Router()

@router.message(Command("admin"))
async def admin_command(message: Message):
    if message.from_user.id in ADMINS:
        await message.answer("Нажми на кнопку:", reply_markup=keyboard)
    else:
        await message.answer("У вас нет доступа к админ-кнопкам! ")