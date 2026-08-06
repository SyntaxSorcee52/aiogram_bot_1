import asyncio
import aiogram
from aiogram import Bot , Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer('hello ')



async def main():
    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())