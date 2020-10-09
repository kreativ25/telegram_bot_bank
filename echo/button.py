from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup

CALLBACK_BUTTON_MENU_NB = 'nb_menu'
CALLBACK_BUTTON_MENU_KB = 'kb_menu'
CALLBACK_BUTTON_STAVKI_NB = 'stavki_nb'
CALLBACK_BUTTON_CURS_NB = 'curs_nb'
CALLBACK_BUTTON_LIQ_NB = 'liq_nb'
CALLBACK_BUTTON_MBK_NB = 'mbk_nb'
CALLBACK_BUTTON_NEWS_NB = 'news_nb'
CALLBACK_BUTTON_METALL_NB = 'metall_nb'
CALLBACK_BUTTON_BACK_NB = 'back_nb'

TITLES_GLOBAL = {
    CALLBACK_BUTTON_MENU_NB: 'Национальный банк',
    CALLBACK_BUTTON_MENU_KB: 'Банки',
}

TITLES_NB = {
    CALLBACK_BUTTON_STAVKI_NB: 'Ставки НБ',
    CALLBACK_BUTTON_CURS_NB: 'Курсы валют НБ',
    CALLBACK_BUTTON_LIQ_NB: 'Ликвидность',
    CALLBACK_BUTTON_MBK_NB: 'МБК',
    CALLBACK_BUTTON_NEWS_NB: 'Новости',
    CALLBACK_BUTTON_METALL_NB: 'Драг. металлы',
    CALLBACK_BUTTON_BACK_NB: '⬅️ Назад'
}


# главное меню
def get_base_menu():
    keyboard = [
        [
            KeyboardButton(TITLES_GLOBAL[CALLBACK_BUTTON_MENU_NB]),
            KeyboardButton(TITLES_GLOBAL[CALLBACK_BUTTON_MENU_KB])
        ],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )


# меню Нацбанка
def get_menu_nb():
    keyboard = [
        [
            KeyboardButton(TITLES_NB[CALLBACK_BUTTON_STAVKI_NB]),
            KeyboardButton(TITLES_NB[CALLBACK_BUTTON_CURS_NB]),
            KeyboardButton(TITLES_NB[CALLBACK_BUTTON_LIQ_NB])
        ],
        [
            KeyboardButton(TITLES_NB[CALLBACK_BUTTON_MBK_NB]),
            KeyboardButton(TITLES_NB[CALLBACK_BUTTON_NEWS_NB]),
            KeyboardButton(TITLES_NB[CALLBACK_BUTTON_METALL_NB])
        ],
        [
            KeyboardButton(TITLES_NB[CALLBACK_BUTTON_BACK_NB])
        ],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )
