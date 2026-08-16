import asyncio

from database.db import init_db
from aiogram import Bot , Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from config import TOKEN
from handlers.start import router as start_router
from handlers.wiki import router as wiki_router
from aiogram.fsm.storage.redis import RedisStorage

storage = RedisStorage.from_url("redis://localhost:6379/0")

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=storage)

dp.include_router(start_router)
dp.include_router(wiki_router)

async def main():
    await init_db()
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())