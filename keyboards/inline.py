from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def menu_buttons():
    buttons=[
        [
            InlineKeyboardButton(text="вики", callback_data='wiki')
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)