from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_menu_inline_kurs_nb_cur_all():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2

    nb_kurs_nb_usd_all = InlineKeyboardButton(text='🇺🇸 USD', callback_data='nb_kurs_nb_usd_all')
    nb_kurs_nb_eur_all = InlineKeyboardButton(text='🇪🇺 EUR', callback_data='nb_kurs_nb_eur_all')

    nb_kurs_nb_rub_all = InlineKeyboardButton(text='🇷🇺 RUB', callback_data='nb_kurs_nb_rub_all')
    nb_kurs_nb_pln_all = InlineKeyboardButton(text='🇵🇱 PLN', callback_data='nb_kurs_nb_pln_all')

    nb_kurs_nb_back_all = InlineKeyboardButton(text='⬅️ Назад в раздел курсов НБ', callback_data='nb_kurs_nb_back_all')

    markup.add(
        nb_kurs_nb_usd_all,
        nb_kurs_nb_eur_all,
        nb_kurs_nb_rub_all,
        nb_kurs_nb_pln_all,
        nb_kurs_nb_back_all,

    )

    return markup