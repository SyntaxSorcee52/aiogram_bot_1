from aiogram import Router, html
from aiogram.types import message
from aiogram.filters import Command
from textwrap import dedent
from database.db import add_user
from keyboards.inline import admin_buttons
from config import ADMIN_ID
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

router = Router()


@router.message(Command("admin"))
async def admin_panel():
    if message.from_user.id != ADMIN_ID:
        await message.answer(text='У вас нет прав для этой команды')
        return
    await message.answer("welcom в админ панель", reply_markup=admin_buttons())
