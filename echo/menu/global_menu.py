from telebot.types import InlineKeyboardButton, ReplyKeyboardMarkup


def get_base_menu():
    markup = ReplyKeyboardMarkup()
    markup.row_width = 2
    button_nb = InlineKeyboardButton(text='Национальный банк', callback_data='nb_menu')
    button_kb = InlineKeyboardButton(text='Банки', callback_data='kb_menu')
    markup.add(button_nb, button_kb)

    return markup










#
#
# from telegram import KeyboardButton
# from telegram import ReplyKeyboardMarkup
#
# CALLBACK_BUTTON_MENU_NB = 'nb_menu'
# CALLBACK_BUTTON_MENU_KB = 'kb_menu'
#
# TITLES_GLOBAL = {
#     CALLBACK_BUTTON_MENU_NB: 'Национальный банк',
#     CALLBACK_BUTTON_MENU_KB: 'Банки',
# }
#
#
# # главное меню
# def get_base_menu():
#     keyboard = [
#         [
#             KeyboardButton(TITLES_GLOBAL[CALLBACK_BUTTON_MENU_NB]),
#             KeyboardButton(TITLES_GLOBAL[CALLBACK_BUTTON_MENU_KB])
#         ],
#     ]
#     return ReplyKeyboardMarkup(
#         keyboard=keyboard,
#         resize_keyboard=True
#     )
