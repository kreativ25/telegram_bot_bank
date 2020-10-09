from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup

# меню ставки по операциям Национального банка
CALLBACK_BUTTON_STAVKI_OPER_1D = 'nb_stavka_sr_1d'
CALLBACK_BUTTON_STAVKI_OPER_ALL = 'nb_satvka_sr_all'
CALLBACK_BUTTON_STAVKI_OPER_BACK = 'nb_satvka_sr_back'
CALLBACK_BUTTON_STAVKI_OPER_BACK_MENU = 'nb_satvka_sr_back_menu'

TITLES_STAVKI_NB_OPER = {
    CALLBACK_BUTTON_STAVKI_OPER_1D: 'Текущие ставки по операциям НБ',
    CALLBACK_BUTTON_STAVKI_OPER_ALL: 'Динамика ставок по операциям НБ',
    CALLBACK_BUTTON_STAVKI_OPER_BACK: '⬅️ Назад в раздел ставок НБ',
    CALLBACK_BUTTON_STAVKI_OPER_BACK_MENU: '⬅️ Назад в раздел Нацбанк'
}


# меню ставки рефинансирования
def get_menu_stavki_oper():
    keyboard = [
        [
            KeyboardButton(TITLES_STAVKI_NB_OPER[CALLBACK_BUTTON_STAVKI_OPER_1D]),
            KeyboardButton(TITLES_STAVKI_NB_OPER[CALLBACK_BUTTON_STAVKI_OPER_ALL])
        ],
        [
            KeyboardButton(TITLES_STAVKI_NB_OPER[CALLBACK_BUTTON_STAVKI_OPER_BACK]),
            KeyboardButton(TITLES_STAVKI_NB_OPER[CALLBACK_BUTTON_STAVKI_OPER_BACK_MENU])
        ]
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )
