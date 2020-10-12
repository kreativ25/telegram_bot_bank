# from telegram import KeyboardButton
# from telegram import ReplyKeyboardMarkup
#
# # главное меню
# CALLBACK_BUTTON_MENU_NB = 'nb_menu'
# CALLBACK_BUTTON_MENU_KB = 'kb_menu'
#
# # меню нбрб
# CALLBACK_BUTTON_STAVKI_NB = 'stavki_nb'
# CALLBACK_BUTTON_CURS_NB = 'curs_nb'
# CALLBACK_BUTTON_LIQ_NB = 'liq_nb'
# CALLBACK_BUTTON_MBK_NB = 'mbk_nb'
# CALLBACK_BUTTON_NEWS_NB = 'news_nb'
# CALLBACK_BUTTON_METALL_NB = 'metall_nb'
# CALLBACK_BUTTON_BACK_NB = 'back_nb'
#
# # меню ставки
# CALLBACK_BUTTON_STAVKI_SR = 'nb_stavki_sr'
# CALLBACK_BUTTON_STAVKI_OPER = 'nb_stavki_oper'
# CALLBACK_BUTTON_STAVKI_BACK = 'nb_stavki_back'
#
# TITLES_GLOBAL = {
#     CALLBACK_BUTTON_MENU_NB: 'Национальный банк',
#     CALLBACK_BUTTON_MENU_KB: 'Банки',
# }
#
# TITLES_NB = {
#     CALLBACK_BUTTON_STAVKI_NB: 'Ставки НБ',
#     CALLBACK_BUTTON_CURS_NB: 'Курсы валют НБ',
#     CALLBACK_BUTTON_LIQ_NB: 'Ликвидность',
#     CALLBACK_BUTTON_MBK_NB: 'МБК',
#     CALLBACK_BUTTON_NEWS_NB: 'Новости',
#     CALLBACK_BUTTON_METALL_NB: 'Драг. металлы',
#     CALLBACK_BUTTON_BACK_NB: '⬅️ Назад'
# }
#
# TITLES_STAVKI_NB = {
#     CALLBACK_BUTTON_STAVKI_SR: 'Ставка рефинансирования',
#     CALLBACK_BUTTON_STAVKI_OPER: 'Ставки по операциям НБ',
#     CALLBACK_BUTTON_STAVKI_BACK: '⬅️ Назад в раздел Нацбанка'
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
#
#
# # меню Нацбанка
# def get_menu_nb():
#     keyboard = [
#         [
#             KeyboardButton(TITLES_NB[CALLBACK_BUTTON_STAVKI_NB]),
#             KeyboardButton(TITLES_NB[CALLBACK_BUTTON_CURS_NB]),
#             KeyboardButton(TITLES_NB[CALLBACK_BUTTON_LIQ_NB])
#         ],
#         [
#             KeyboardButton(TITLES_NB[CALLBACK_BUTTON_MBK_NB]),
#             KeyboardButton(TITLES_NB[CALLBACK_BUTTON_NEWS_NB]),
#             KeyboardButton(TITLES_NB[CALLBACK_BUTTON_METALL_NB])
#         ],
#         [
#             KeyboardButton(TITLES_NB[CALLBACK_BUTTON_BACK_NB])
#         ],
#     ]
#     return ReplyKeyboardMarkup(
#         keyboard=keyboard,
#         resize_keyboard=True
#     )
#
#
# # меню ставки НБ
# def get_menu_stavki_nb():
#     keyboard = [
#         [
#             KeyboardButton(TITLES_STAVKI_NB[CALLBACK_BUTTON_STAVKI_SR]),
#             KeyboardButton(TITLES_STAVKI_NB[CALLBACK_BUTTON_STAVKI_OPER])
#         ],
#         [
#             KeyboardButton(TITLES_STAVKI_NB[CALLBACK_BUTTON_STAVKI_BACK])
#         ]
#     ]
#     return ReplyKeyboardMarkup(
#         keyboard=keyboard,
#         resize_keyboard=True
#     )
#
#
#
