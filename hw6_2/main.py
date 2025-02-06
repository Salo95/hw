import asyncio
from aiogram import Bot, Dispatcher
from config import TOKEN
from handlers import inline
from handlers import commands
from handlers import states

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(inline.router)
dp.include_router(commands.router)
dp.include_router(states.router)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())