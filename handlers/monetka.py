from aiogram import Router, F, html
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message
from keyboards.inline import wiki_buttons, wiki_random_article, menu_buttons, monetka_buttons
from aiogram.exceptions import TelegramBadRequest
from textwrap import dedent
import aiohttp
import random
from redis.asyncio import Redis
import logging

redis_client = Redis(host="redis", port=6379, decode_responses=True)

router  = Router()

@router.callback_query(F.data == "monetka")
async def random_monetka(callback:CallbackQuery, redis: Redis):
    monetka = ('Орёл 🦅', 'Решка 🪙')
    element = random.choice(monetka)
    await callback.answer(text=f"Выпало: {element}", show_alert=False)
    try:
        await callback.message.edit_text(
            text=element,
            parse_mode="HTML",
            reply_markup=monetka_buttons()
        )
    except TelegramBadRequest as e:
        # Игнорируем только дублирование текста при спаме
        if "message is not modified" in e.message:
            pass
        else:
            # Другие ошибки Telegram выводим в консоль
            print(f"Ошибка Telegram API: {e}")
    except Exception as e:
        # Все остальные фатальные ошибки кода пишем в консоль!
        print(f"Критическая ошибка в коде: {e}")