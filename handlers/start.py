from aiogram import Router, html
from aiogram.filters import CommandStart
from aiogram.types import Message
from textwrap import dedent


#кнопки
from keyboards.inline import menu_buttons


router = Router()

@router.message(CommandStart())
async def  cmd_start(message:Message):
    user_name = html.quote(message.from_user.first_name)
    text = dedent("""
        <b>👋 Привет, {user_name}</b>
        Я могу помоч тебе с разнми задачами 
        выбери что-то ниже👇
    """).strip()
    
    await message.answer(text, parse_mode="HTML",reply_markup=menu_buttons())