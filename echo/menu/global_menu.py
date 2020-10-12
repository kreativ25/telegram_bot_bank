from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup

CALLBACK_BUTTON_MENU_NB = 'nb_menu'
CALLBACK_BUTTON_MENU_KB = 'kb_menu'

TITLES_GLOBAL = {
    CALLBACK_BUTTON_MENU_NB: 'Национальный банк',
    CALLBACK_BUTTON_MENU_KB: 'Банки',
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
