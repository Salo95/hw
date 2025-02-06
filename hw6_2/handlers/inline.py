from aiogram import Bot, types, Router
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from aiogram .fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from .states import Form

router = Router()
keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="Зарегистрироваться", callback_data="start")]
    ]
)

@router.callback_query(lambda call: call.data == "start")
async def button_pressed(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer("Введите ваше имя")
    await state.set_state(Form.name)
    