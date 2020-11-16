from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_inline_nb_mbk():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2

    button_mbk = InlineKeyboardButton(text='📈 Текущая ставка', callback_data='button_mbk')
    button_mbk_dinamiq = InlineKeyboardButton(text='📊 Динамика МБК', callback_data='button_mbk_dinamiq')

    markup.add(
        button_mbk,
        button_mbk_dinamiq
    )

    return markup