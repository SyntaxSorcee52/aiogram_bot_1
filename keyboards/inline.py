from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
#кнопки меню
def menu_buttons():
    buttons=[
        [
            InlineKeyboardButton(text="вики", callback_data="wiki")
        ],
        [
            InlineKeyboardButton(text="подбросить монетку", callback_data="monetka")
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

# все кнопки раздела вики
def wiki_buttons():
    buttons=[
        [
            InlineKeyboardButton(text='рандомная статья',callback_data='random_article'),
            InlineKeyboardButton(text='вернуться в меню',callback_data='back_to_menu')
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
def monetka_buttons():
    buttons=[
        [
            InlineKeyboardButton(text='подбросить ещё раз',callback_data='monetka')
        ],
        [
            InlineKeyboardButton(text='вернуться в меню',callback_data='back_to_menu')
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)

def admin_buttons():
    buttons=[
        [
            InlineKeyboardButton(text='Статистика', callback_data='stats')
        ],
        [
            InlineKeyboardButton(text='Рассылка', callback_data='broadkast')
        ],
        [
            InlineKeyboardButton(text='база данных', callback_data='database')
        ]
    ]
    return InlineKeyboardMarkup(inline_keyboard=buttons)