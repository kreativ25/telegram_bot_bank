from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_inline_nb_stavki():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2

    button_stavki_sr = InlineKeyboardButton(text='Ставка реф-я', callback_data='nb_stavki_sr')
    button_stavki_oper = InlineKeyboardButton(text='Ставки по операциям НБ', callback_data='nb_stavki_oper')

    markup.add(
        button_stavki_sr,
        button_stavki_oper
    )

    return markup
