from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_menu_inline_metal_nb_global():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2

    nb_metal_nb_price = InlineKeyboardButton(text='Учетные цены', callback_data='nb_metal_nb_price')
    nb_metal_nb_ingot = InlineKeyboardButton(text='Мерные слитки', callback_data='nb_metal_nb_ingot')

    markup.add(
        nb_metal_nb_price,
        nb_metal_nb_ingot,
    )

    return markup