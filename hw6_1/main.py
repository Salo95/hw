import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import inline_kboard
from handlers import admin

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(inline_kboard.router)
dp.include_router(admin.router)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())