from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup

# меню курсы валют НБ
CALLBACK_BUTTON_NB_KURS_1D = 'nb_kurs_1d'
CALLBACK_BUTTON_NB_KURS_ALL = 'nb_kurs_all'
CALLBACK_BUTTON_NB_KURS_BACK = 'nb_kurs_back'
CALLBACK_BUTTON_NB_KURS_BACK_MENU = 'nb_kurs_back_menu'

TITLES_KURS_NB = {
    CALLBACK_BUTTON_NB_KURS_1D: 'Текущие курсы НБ',
    CALLBACK_BUTTON_NB_KURS_ALL: 'Динамика курсов НБ',
    CALLBACK_BUTTON_NB_KURS_BACK: '⬅️ Назад в раздел ставок НБ',
    CALLBACK_BUTTON_NB_KURS_BACK_MENU: '⬅️ Назад в раздел Нацбанк'
}


# меню ставки рефинансирования
def get_menu_nb_kurs():
    keyboard = [
        [
            KeyboardButton(TITLES_KURS_NB[CALLBACK_BUTTON_NB_KURS_1D]),
            KeyboardButton(TITLES_KURS_NB[CALLBACK_BUTTON_NB_KURS_ALL])
        ],
        [
            KeyboardButton(TITLES_KURS_NB[CALLBACK_BUTTON_NB_KURS_BACK]),
            KeyboardButton(TITLES_KURS_NB[CALLBACK_BUTTON_NB_KURS_BACK_MENU])
        ]
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )
