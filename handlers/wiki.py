from aiogram import Router, F, html
from aiogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton, Message
from keyboards.inline import wiki_buttons, wiki_random_article
import aiohttp

router  = Router()

#wiki button
@router.callback_query(F.data == "wiki")
async def main_menu_handler(callback:CallbackQuery):
    await callback.answer(text='wiki в разработке')
    await callback.message.edit_text(text="Выбери категрию",parse_mode="HTML",reply_markup=wiki_buttons())


@router.callback_query(F.data == "random_article")
async def get_random_article(callback:CallbackQuery):
    
    connector = aiohttp.TCPConnector(ssl=False)
    url =  'https://ru.wikipedia.org/api/rest_v1/page/random/summary'
    headers = {"User-Agent": "MyWikiBot/1.0 (contacts: sandw1chmastergg@gmail.com)"}
    try:
        async with aiohttp.ClientSession(connector=connector) as session:
            async with session.get(url, headers=headers) as respons:
                if respons.status == 200:
                    data = await respons.json()
                    title = data.get("title", "Без названия")
                    extract = data.get("extract", "Описание отсутствует.")
                else:
                    title = "Ошибка"
                    extract = "Не удалось загрузить данные с Википедии."

                content_urls = data.get("content_urls", {})
                page_url = content_urls.get("mobile", {}).get("page", "https://ru.wikipedia.org")

        formatted_text = f"📚 <b>{html.quote(title)}</b>\n\n{html.quote(extract)}"

        await callback.message.edit_text(text=formatted_text,parse_mode="HTML",reply_markup=wiki_random_article(page_url))
        await callback.answer()
    except Exception as e:
        print(f'код ебнулся ошибка {respons.status}')
        await callback.answer(text='код ебнулся сорян 😭')