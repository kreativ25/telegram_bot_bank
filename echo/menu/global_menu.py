from telebot.types import InlineKeyboardButton, ReplyKeyboardMarkup


def get_base_menu():
    markup = ReplyKeyboardMarkup()
    markup.row_width = 2
    markup.resize_keyboard = True
    button_nb = InlineKeyboardButton(text='Национальный банк', callback_data='nb_menu')
    button_kb = InlineKeyboardButton(text='Банки', callback_data='kb_menu')
    button_gos = InlineKeyboardButton(text='Новости гос. органов', callback_data='gos')
    button_v = InlineKeyboardButton(text='Обратная связь', callback_data='kb_menu')
    markup.add(button_nb, button_kb, button_gos, button_v)

    return markup
