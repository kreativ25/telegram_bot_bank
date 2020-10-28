from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_menu_inline_stavki_oper_nb():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2

    nb_stavki_oper_nb_1d = InlineKeyboardButton(text='📈 Текущие ставки НБ', callback_data='nb_stavki_oper_nb_1d')
    nb_satvki_oper_nb_all = InlineKeyboardButton(text='📊 Динамика ставок НБ', callback_data='nb_satvki_oper_nb_all')
    nb_stavki_oper_back = InlineKeyboardButton(text='⬅️ Назад в раздел ставок НБ', callback_data='nb_stavki_oper_back')

    markup.add(
        nb_stavki_oper_nb_1d,
        nb_satvki_oper_nb_all,
        nb_stavki_oper_back
    )

    return markup
