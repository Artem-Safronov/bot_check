import asyncio

from aiogram import Bot, Dispatcher

from app.db.db import Db
from settings import API_TOKEN

bot = Bot(API_TOKEN)
dp = Dispatcher(bot)


async def main():
    db = Db()
    await db.load()
    dp["db"] = db
    await dp.start_polling(dp)


if __name__ == "__main__":
    asyncio.run(main())
