from aiogram import Router, F
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton\

router  = Router()

@router.callback_query(F.data == "wiki")
async def main_menu_handler(callback:CallbackQuery):
    await callback.answer(text='wiki в разработке')