from aiogram import Bot, Dispatcher
import asyncio
import logging
from config import BOT_TOKEN
from router import router
import sys

dp = Dispatcher()

async def main() -> None:
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    bot = Bot(token=BOT_TOKEN)

    dp.include_router(router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())