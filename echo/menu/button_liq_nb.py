from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_inline_nb_liq():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2

    button_liq = InlineKeyboardButton(text='Показатели ликвидности', callback_data='nb_liq')
    button_liq_dinamiq = InlineKeyboardButton(text='Динамика ликвидности', callback_data='nb_liq_dinamiq')

    markup.add(
        button_liq,
        button_liq_dinamiq
    )

    return markup