import asyncio
from aiogram import Bot, Dispatcher
from app.handlers import router



async def main():
    bot = Bot(token = '')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
