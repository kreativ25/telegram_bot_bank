from telebot.types import InlineKeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove


def get_base_menu_kb():
    markup = ReplyKeyboardMarkup()
    markup.row_width = 2
    markup.resize_keyboard = True
    markup.one_time_keyboard = False

    button_converter = InlineKeyboardButton(text='Конвертер валют', callback_data='converter_kb')
    button_curs = InlineKeyboardButton(text='Курсы валют', callback_data='curs_kb')
    button_back_nb = InlineKeyboardButton(text='⬅️ Назад', callback_data='back_nb')

    markup.add(
        button_converter,
        button_curs,
        button_back_nb,

    )

    return markup

