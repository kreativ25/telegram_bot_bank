from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup

# меню ставки рефинансирования
CALLBACK_BUTTON_STAVKI_SR_1D = 'nb_stavka_sr_1d'
CALLBACK_BUTTON_STAVKI_SR_ALL = 'nb_satvka_sr_all'
CALLBACK_BUTTON_STAVKI_SR_BACK = 'nb_satvka_sr_back'
CALLBACK_BUTTON_STAVKI_SR_BACK_MENU = 'nb_satvka_sr_back_menu'

TITLES_STAVKI_NB_SR = {
    CALLBACK_BUTTON_STAVKI_SR_1D: 'Текущая ставка реф-я',
    CALLBACK_BUTTON_STAVKI_SR_ALL: 'Динамика ставки реф-я',
    CALLBACK_BUTTON_STAVKI_SR_BACK: '⬅️ Назад в раздел ставок НБ',
    CALLBACK_BUTTON_STAVKI_SR_BACK_MENU: '⬅️ Назад в раздел Нацбанк'
}


# меню ставки рефинансирования
def get_menu_stavka_sr():
    keyboard = [
        [
            KeyboardButton(TITLES_STAVKI_NB_SR[CALLBACK_BUTTON_STAVKI_SR_1D]),
            KeyboardButton(TITLES_STAVKI_NB_SR[CALLBACK_BUTTON_STAVKI_SR_ALL])
        ],
        [
            KeyboardButton(TITLES_STAVKI_NB_SR[CALLBACK_BUTTON_STAVKI_SR_BACK]),
            KeyboardButton(TITLES_STAVKI_NB_SR[CALLBACK_BUTTON_STAVKI_SR_BACK_MENU])
        ]
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )
