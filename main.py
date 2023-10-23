from conf import TELEGRAM_BOT_TOKEN, OPENAI_API_KEY
import openai
import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram import types
from aiogram import F
from aiogram.utils.markdown import hbold

# Инициализация бота и диспетчера
bot = Bot(token=TELEGRAM_BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)
openai.api_key = OPENAI_API_KEY


# Обработчик события присоединения новых пользователей к чату
@dp.message(F.new_chat_members)
async def somebody_added(message: types.Message):
    for user in message.new_chat_members:
        # проперти full_name берёт сразу имя И фамилию
        # (на скриншоте выше у юзеров нет фамилии)
        await message.reply(
            f"Привет, {hbold(message.from_user.full_name)}. Добро пожаловать в Чат заботы Солдатовой Татьяны. \n "
            f"Я бот консультант этого чата."
            f"\n Я могу ответить на наиболее частые ваши вопросы.\n Просто обратитесь ко мне "
            f"упоминув мое имя @curlszabot_bot и делее Ваше сообщение \n Я постараюсь очень оперативно ответить вам."
            f"\n Наиболее частые вопросы вы можете увидеть под моим сообщением в кнопки МЕНЮ")


# Обработка команды /start
@dp.message(Command("start"))
async def on_start(message: types.Message) -> None:
    await message.answer(
        f"Привет {hbold(message.from_user.full_name)} ! \n Добро пожаловать в Чат заботы Солдатовой Татьяны."
        f" \n Я бот консультант этого чата."
        f"\n Я могу ответить на наиболее частые ваши вопросы.\n Просто обратитесь ко мне "
        f"упоминув мое имя @curlszabot_bot и делее Ваше сообщение \n Я постараюсь очень оперативно ответить вам."
        f"\n Наиболее частые вопросы вы можете увидеть под моим сообщением в кнопки МЕНЮ")


# Обработчик всех текстовых сообщений
@dp.message()
async def on_message(message: types.Message):
    # Получаем информацию о боте
    bot_info = await bot.get_me()
    bot_username = bot_info.username

    if f"@{bot_username}" in message.text:
        # Используем GPT-3 для генерации ответа
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=message.text,
            max_tokens=1000
        )
        await message.reply(response.choices[0].text)
    else:
        # Если бот не упомянут, не отвечаем
        pass

# Сообщение по команде /menu с кнопками
@dp.message(Command("menu"))
async def cmd_menu(message: types.Message):
    kb = [
        [
            types.KeyboardButton(text="продлить доступ к курсу"),
            types.KeyboardButton(text="Востановить доступ к курсу"),
            types.KeyboardButton(text="Востановить доступ к курсу")
        ],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
        input_field_placeholder="текст1"
    )
    await message.answer("текст2", reply_markup=keyboard)

async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TELEGRAM_BOT_TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
