from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message
from textwrap import dedent
from database.db import add_user


#кнопки
from keyboards.inline import menu_buttons


router = Router()

@router.message(CommandStart())
async def  cmd_start(message:Message):
    user_name = html.quote(message.from_user.first_name)
    text = dedent(f"""
        <b>👋 Привет, {user_name}</b>
        Я могу помоч тебе с разнми задачами 
        выбери что-то ниже👇
    """).strip()
    await add_user(
        user_id=message.from_user.id,
        user_name=message.from_user.username,
        name=message.from_user.first_name
    )
    
    await message.answer(text, parse_mode="HTML",reply_markup=menu_buttons())
