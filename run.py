import asyncio
from aiogram import Bot , Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from config import TOKEN
from handlers.start import router as start_router
from handlers.wiki import router as wiki_router

bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(start_router)
dp.include_router(wiki_router)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())