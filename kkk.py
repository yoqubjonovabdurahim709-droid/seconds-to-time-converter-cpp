import asyncio
import wikipedia
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

TOKEN = "8665831420:AAGRq1mIbPdvTPf0PXctDKH_wPW9fMyZp5U"
wikipedia.set_lang('uz')

dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")

@dp.message()
async def send_info(message: Message) -> None:
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)  # ✅ TO'G'RI
    except wikipedia.exceptions.DisambiguationError:
        await message.answer("Bu so'z bir nechta maqolaga mos keladi, aniqroq yozing.")
    except wikipedia.exceptions.PageError:
        await message.answer("Bu mavzuga oid maqola topilmadi 😕")
    except Exception as e:
        await message.answer("Xatolik yuz berdi, qayta urinib ko'ring.")

async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())