from telegram import InlineKeyboardButton
from telegram import InlineKeyboardMarkup

# меню ставки рефинансирования
CALLBACK_BUTTON_STAVKI_SR_1D = 'nb_stavka_sr_1d'
CALLBACK_BUTTON_STAVKI_SR_ALL = 'nb_satvka_sr_all'
CALLBACK_BUTTON_STAVKI_SR_BACK = 'nb_stavka_sr_back'


TITLES_STAVKI_NB_SR = {
    CALLBACK_BUTTON_STAVKI_SR_1D: 'Текущая ставка реф-я',
    CALLBACK_BUTTON_STAVKI_SR_ALL: 'Динамика ставки реф-я',
    CALLBACK_BUTTON_STAVKI_SR_BACK: '⬅️ Назад'
}


# меню ставки рефинансирования
def get_menu_inline_stavka_sr():
    keyboard = [
        [
            InlineKeyboardButton(TITLES_STAVKI_NB_SR[CALLBACK_BUTTON_STAVKI_SR_1D], callback_data=CALLBACK_BUTTON_STAVKI_SR_1D),
            InlineKeyboardButton(TITLES_STAVKI_NB_SR[CALLBACK_BUTTON_STAVKI_SR_ALL], callback_data=CALLBACK_BUTTON_STAVKI_SR_ALL)
        ],
        [
            InlineKeyboardButton(TITLES_STAVKI_NB_SR[CALLBACK_BUTTON_STAVKI_SR_BACK], callback_data=CALLBACK_BUTTON_STAVKI_SR_BACK)
        ]
    ]
    return InlineKeyboardMarkup(keyboard, row_width=2)