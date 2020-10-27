from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_menu_inline_kurs_nb_global():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2

    nb_kurs_nb_1d = InlineKeyboardButton(text='Курсы НБ на сегодня', callback_data='nb_kurs_nb_1d')
    nb_kurs_nb_all = InlineKeyboardButton(text='Динамика курсов НБ', callback_data='nb_kurs_nb_all')

    markup.add(
        nb_kurs_nb_1d,
        nb_kurs_nb_all,
    )

    return markup