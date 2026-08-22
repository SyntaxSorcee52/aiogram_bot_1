import asyncio
import os
from database.db import init_db
from aiogram import Bot , Dispatcher
from config import TOKEN, ADMIN_ID
from aiogram.types import BotCommand, BotCommandScopeDefault, BotCommandScopeChat
from handlers.start import router as start_router
from handlers.wiki import router as wiki_router
from handlers.admin import router as admin_router
from handlers.monetka import router as monetka_router
from aiogram.fsm.storage.redis import RedisStorage
import logging


storage = RedisStorage.from_url("redis://redis:6379/0")

bot = Bot(token=TOKEN)
dp = Dispatcher(storage=storage)

dp.include_router(admin_router)
dp.include_router(start_router)
dp.include_router(wiki_router)
dp.include_router(monetka_router)


async def set_commands():
    admin_commands = [
        BotCommand(command="admin", description="👑 админ панель")
    ]
    try:
        await bot.set_my_commands(
            admin_commands,
            scope=BotCommandScopeChat(chat_id=ADMIN_ID)
        )
    except Exception as e:
        print(f"Не удалось установить меню админа: {e}")

async def main():
    await init_db()
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')