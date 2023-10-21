from conf import *
import openai
import asyncio
import logging
import sys
from os import getenv
import aiogram.utils.markdown as md

from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold

# Замените 'YOUR_TELEGRAM_BOT_TOKEN' на ваш токен бота из BotFather
TELEGRAM_BOT_TOKEN = BOT_TOKEN

# Замените 'YOUR_OPENAI_API_KEY' на ваш ключ API GPT-3
OPENAI_API_KEY = OPENAI_API_KEY

# Инициализация бота и диспетчера
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)
openai.api_key = OPENAI_API_KEY

# Обработка команды /start
@dp.message(CommandStart())
async def command_start_handler(message: types.Message):
    await message.answer(f"Привет! Я бот, который может вам помочь. Просто отправьте мне сообщение, и я отвечу вам.")

# Обработка входящих сообщений
@dp.message()
async def on_message(message: types.Message):
    user_message = message.text

    # Запрос к GPT-3
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=user_message,
        max_tokens=1000  # Максимальная длина ответа
    )

    bot_response = response.choices[0].text

    # Отправка ответа пользователю
    await message.answer(bot_response, parse_mode=ParseMode.MARKDOWN)

async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TELEGRAM_BOT_TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())