from aiogram import Router, types
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from .inline import keyboard

router = Router()

@router.message(Command("start"))
async def start_handler(message: types.Message):
    await message.answer("Здравствуйте", reply_markup=keyboard)