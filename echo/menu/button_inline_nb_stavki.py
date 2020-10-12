from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup

# меню ставки Национального банка
CALLBACK_BUTTON_STAVKI_SR = 'nb_stavki_sr'
CALLBACK_BUTTON_STAVKI_OPER = 'nb_stavki_oper'


TITLES_STAVKI_NB = {
    CALLBACK_BUTTON_STAVKI_SR: 'Ставка рефинансирования',
    CALLBACK_BUTTON_STAVKI_OPER: 'Ставки по операциям НБ',
}


def get_inline_nb_stavki():
    keyboard = [
        [
            InlineKeyboardButton(TITLES_STAVKI_NB[CALLBACK_BUTTON_STAVKI_SR], callback_data=CALLBACK_BUTTON_STAVKI_SR),
            InlineKeyboardButton(TITLES_STAVKI_NB[CALLBACK_BUTTON_STAVKI_OPER],
                                 callback_data=CALLBACK_BUTTON_STAVKI_OPER)
        ]
    ]
    return InlineKeyboardMarkup(keyboard, row_width=2)
