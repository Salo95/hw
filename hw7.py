import asyncio
from datetime import datetime, timedelta
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from aiogram import Bot, Dispatcher, Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

BOT_TOKEN = "7661380231:AAGExxSF4W650C2A7Y9OJR3ViGe0ieCqOz8"

class ReminderStates(StatesGroup):
    waiting_for_text = State()
    waiting_for_time = State()

router = Router()

bot_instance: Bot = None
scheduler: AsyncIOScheduler = None

@router.message(Command("remind"))
async def set_reminder(message: types.Message, state: FSMContext):
    await message.answer("Введите текст напоминания:")
    await state.set_state(ReminderStates.waiting_for_text)

@router.message(ReminderStates.waiting_for_text)
async def get_text(message: types.Message, state: FSMContext):
    await state.update_data(reminder_text=message.text)
    await message.answer("Введите время (в секундах):")
    await state.set_state(ReminderStates.waiting_for_time)

@router.message(ReminderStates.waiting_for_time, F.text.isdigit())
async def get_reminder_time(message: types.Message, state: FSMContext):
    user_data = await state.get_data()
    reminder_text = user_data.get("reminder_text")
    delay = int(message.text)

    run_time = datetime.now().astimezone() + timedelta(seconds=delay)

    scheduler.add_job(
        send_reminder,
        'date',
        run_date=run_time,
        args=[message.chat.id, reminder_text, bot_instance]
    )

    await message.answer(f"Напоминание установлено на {delay} секунд!")
    await state.clear()

@router.message(ReminderStates.waiting_for_time)
async def invalid_time_input(message: types.Message):
    await message.answer("Пожалуйста, введите число секунд")

async def send_reminder(chat_id: int, text: str, bot: Bot):
    print("Отправка напоминания")
    await bot.send_message(chat_id=chat_id, text=f"Напоминание: {text}")

async def main():
    global bot_instance, scheduler
    bot_instance = Bot(token=BOT_TOKEN)

    loop = asyncio.get_running_loop()

    scheduler = AsyncIOScheduler(event_loop=loop)
    scheduler.start()

    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot_instance)

if __name__ == '__main__':
    asyncio.run(main())