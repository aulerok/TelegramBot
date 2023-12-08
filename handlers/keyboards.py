from aiogram.utils.keyboard import (InlineKeyboardBuilder, ReplyKeyboardMarkup, ReplyKeyboardBuilder,
                                    InlineKeyboardButton, InlineKeyboardMarkup)




# главная клавиатура меню
def get_main_keyboard():
    keyboard_builer = InlineKeyboardBuilder()
    keyboard_builer.button(text='купить курс', callback_data='get_course_keyboard')
    keyboard_builer.button(text='продлить курс', callback_data='get_cont_course_keyboard')
    keyboard_builer.button(text='Есть проблема!', callback_data='get_problem_keyboard')
    keyboard_builer.button(text='спросить у бота', callback_data='hold4')

    keyboard_builer.adjust(2, 2)
    return keyboard_builer.as_markup()


# клавиатура выбора курса на покупку
def get_course_keyboard():
    keyboard_builer = InlineKeyboardBuilder()
    keyboard_builer.button(text='Тариф ПРОСТОЙ ', url='http://lk.soldatova-school.ru/tarif1_1')
    keyboard_builer.button(text='Тариф МАСТЕР', url='http://lk.soldatova-school.ru/tarif2_2')
    keyboard_builer.button(text='Тариф ПРЕПОДАВАТЕЛЬ', url='http://lk.soldatova-school.ru/tarif3_3')
    keyboard_builer.button(text='НАЗАД', callback_data='back_main')

    keyboard_builer.adjust(3, 1),
    selective = True,
    resize_keyboard = True
    return keyboard_builer.as_markup()

    # клавиатура выбора курса на продление
def get_cont_course_keyboard():
    keyboard_builer = InlineKeyboardBuilder()
    keyboard_builer.button(text='Тариф ПРОСТОЙ ', url='http://lk.soldatova-school.ru/tarif1_1')
    keyboard_builer.button(text='Тариф МААСТЕР', url='http://lk.soldatova-school.ru/tarif2_2')
    keyboard_builer.button(text='Тариф ПРЕПОДАВАТЕЛЬ', url='http://lk.soldatova-school.ru/tarif3_3')
    keyboard_builer.button(text='НАЗАД', callback_data='back_main')

    keyboard_builer.adjust(3, 1)
    return keyboard_builer.as_markup()

def get_problem_keyboard():
    keyboard_builer = InlineKeyboardBuilder()
    keyboard_builer.button(text='Не могу войти в личный кабинет', callback_data='answer_login')
    keyboard_builer.button(text='Нет звука в уроках!!!', callback_data='answer_sound')
    keyboard_builer.button(text='НАЗАД', callback_data='back_main')

    keyboard_builer.adjust(1, 1)
    return keyboard_builer.as_markup()