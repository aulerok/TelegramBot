import asyncio
import logging
import sys
import openai
from aiogram import Bot, Dispatcher
from aiogram import F
from aiogram import types
from aiogram.enums import ParseMode
from aiogram.filters import Command
from aiogram.utils.markdown import hbold
from handlers.keyboards import get_main_keyboard, get_course_keyboard, get_cont_course_keyboard, get_problem_keyboard



from conf import TELEGRAM_BOT_TOKEN, OPENAI_API_KEY

# Инициализация бота и диспетчера
bot = Bot(token=TELEGRAM_BOT_TOKEN, parse_mode="HTML")
dp = Dispatcher()
logging.basicConfig(level=logging.INFO)
openai.api_key = OPENAI_API_KEY
user_data = {}


# Обработчик события присоединения новых пользователей к чату
@dp.message(F.new_chat_members)
async def somebody_added(message: types.Message) -> None:
    # Получаем информацию о боте
    bot_info = await bot.get_me()
    bot_username = bot_info.username
    for user in message.new_chat_members:
        # проперти full_name берёт сразу имя И фамилию
        # (на скриншоте выше у юзеров нет фамилии)
        await message.reply(
            f"Привет, {hbold(message.from_user.full_name)}. Добро пожаловать в Чат заботы Солдатовой Татьяны. \n "
            f"Я бот консультант этого чата."
            f"\n Я могу ответить на наиболее частые ваши вопросы.\n Просто обратитесь ко мне "
            f"упоминув мое имя {bot_username} и делее Ваше сообщение \n Я постараюсь очень оперативно ответить вам."
            f"\n Наиболее частые вопросы вы можете увидеть под моим сообщением в кнопки МЕНЮ")


# Обработка команды /start
@dp.message(Command("start"))
async def on_start(message: types.Message) -> None:

    await message.answer(
        f"Привет {hbold(message.from_user.full_name)} ! \n Добро пожаловать в Чат заботы Солдатовой Татьяны."
        f" \n Я бот консультант этого чата."
        f"\n Я могу ответить на наиболее частые ваши вопросы.\n Просто обратитесь ко мне "
        f"упоминув мое имя @curlszabot_bot и делее Ваше сообщение \n Я постараюсь очень оперативно ответить вам."
        f"\n Наиболее частые вопросы вы можете увидеть под моим сообщением", reply_markup=get_main_keyboard())

# вызов клавиатуры покупки курсов
@dp.callback_query(F.data == 'get_course_keyboard')
async def get_course(callback: types.CallbackQuery):
    await callback.message.edit_text(f"Выбeрите курс курс для покупки", reply_markup=get_course_keyboard())


# вызов клавиатуры продления курсов
@dp.callback_query(F.data == 'get_cont_course_keyboard')
async def get_cont_course(callback: types.CallbackQuery):
    await callback.message.edit_text(f"Выберите курс для продления", reply_markup=get_cont_course_keyboard())

# вызов клавиатуры проблем
@dp.callback_query(F.data == 'get_problem_keyboard')
async def get_cont_course(callback: types.CallbackQuery):
    await callback.message.edit_text(f"Наиболее часто встречающиеся проблемы", reply_markup=get_problem_keyboard())


#кнопка купить hold4
@dp.callback_query(F.data == 'hold4')
async def answer_bot(callback: types.CallbackQuery):
    await callback.message.answer(f"Если вы хотите у меня что нибудь спросить,"
                                     f" \n Скопируйте мое имя @curlszabot_bot и вставьте в ответном сообщении перед "
                                     f"своим вопросом.")

#кнопка купить get_problem

@dp.callback_query(F.data == 'answer_login')
async def answer_login(callback: types.CallbackQuery):
    await callback.message.answer(f"Если у вас возникают проблемы при входе в личный кабинет академии. \n"
                                     f" Вам необходимо востановить пароль,\n"
                                     f"Для этого пнажмите на ссылку \n"
                                     f"http://lk.soldatova-school.ru/cms/system/login?required=trueи \n"
                                     f"Нажмите кнопку 'востановить пароль',\n"
                                     f"введите свою электронную почту которую указывали при покупки курса.\n"
                                     f"После чего вам на почту придет ссылка для востановления пароля к личному кабинету академии.\n"
                                     f"Если у вас так и не получилось решить проблему со входом в личный кабинет. \n"
                                     f"Напишите нашему специалисту @aulerok мы постараемся сделать все чтоб ваша проблема была решена." )

@dp.callback_query(F.data == 'answer_sound')
async def answer_sound(callback: types.CallbackQuery):
    await callback.message.answer(f"Если у вас возникают проблемы при которых в некоторых уроках отсутствует звук."
                                     f" А конкретнее, голос преподавателя не слышно, но звуки заставки есть.\n"
                                     f"Это связано с тем что на вашем устройстве происходит конфликт звукового устройства\n"
                                     f"(Обычно это один моно динамик, один наушник или колонка.) К сожалению мы не можем исправить\n"
                                     f"данную ошибку, потому что она происходит конкретно на вашем устройстве.\n"
                                     f"Вы можете пропробовать использовать другое устройство для просмотра уроков.\n"
                                     f"(Это может быть, персональный компьютер, планшет или другой телефон со стереодинамиками.)\n"
                                     f"Еще помогает подключить к проблемнону устройству блютуз колонку или наушники\n"
                                     f" Если у вас так и не получилось решить проблему со звуком на ваших устройствах \n"
                                     f"Напишите нашему специалисту @aulerok мы постараемся сделать все чтоб ваша проблема была решена." )


# Кнопка назад
@dp.callback_query(F.data == 'back_main')
async def back_main(callback: types.CallbackQuery):
    await callback.message.edit_text(f'_______________меню_______________', reply_markup=get_main_keyboard())



# Обработчик всех текстовых сообщений с ЧАТДЖПТ3
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


async def main() -> None:
    # Initialize Bot instance with a default parse mode which will be passed to all API calls
    bot = Bot(TELEGRAM_BOT_TOKEN, parse_mode=ParseMode.HTML)
    # And the run events dispatching
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
