from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_menu_inline_stavka_sr():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2

    button_sr_1d = InlineKeyboardButton(text='Текущая СР', callback_data='nb_stavka_sr_1d')
    button_sr_all = InlineKeyboardButton(text='Динамика СР', callback_data='nb_satvka_sr_all')
    button_sr_back = InlineKeyboardButton(text='⬅️ Назад в раздел ставок НБ', callback_data='nb_stavka_sr_back')

    markup.add(
        button_sr_1d,
        button_sr_all,
        button_sr_back
    )

    return markup
