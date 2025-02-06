from aiogram import Bot, types, Router
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

router = Router()
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Статистика", callback_data="statistics")],
        [InlineKeyboardButton(text="Обновить данные", callback_data="update")]
    ]
)

@router.callback_query(lambda call: call.data == "statistics")
async def button_pressed(call: types.CallbackQuery):
    await call.message.answer("Статистика - 100 пользователей")
@router.callback_query(lambda call: call.data == "update")
async def button_pressed(call: types.CallbackQuery):
    await call.message.answer("Данные обновлены")