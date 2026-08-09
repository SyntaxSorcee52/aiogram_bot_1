from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
#кнопки меню
def menu_buttons():
    buttons=[
        [
            InlineKeyboardButton(text="вики", callback_data='wiki')
        ],
        [
            InlineKeyboardButton(text='я хз что делает эта кнопка',callback_data='xz')
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# все кнопки раздела вики
def wiki_buttons():
    buttons=[
        [
            InlineKeyboardButton(text='рандомная статья',callback_data='random_article')
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

#кнопки рандом статьи вики
def wiki_random_article(page_url:str):
    buttons = [
        [
            InlineKeyboardButton(text='еще одна',callback_data='random_article')
        ],
        [
            InlineKeyboardButton(text='вернуться в меню',callback_data='back_to_menu')
        ],
        [
            InlineKeyboardButton(text='открыть полностью',url=page_url)
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)