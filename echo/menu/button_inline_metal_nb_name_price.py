from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_menu_inline_metal_nb_price_all():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2

    nb_gold_price = InlineKeyboardButton(text='🥇 Золото', callback_data='nb_gold_price')
    nb_silver_price = InlineKeyboardButton(text='🥈 Серебро', callback_data='nb_silver_price')

    nb_platinum_price = InlineKeyboardButton(text='⛓ Платина', callback_data='nb_platinum_price')
    nb_palladium_price = InlineKeyboardButton(text='📏 Палладий', callback_data='nb_palladium_price')

    nb_metal_nb_back_price_all = InlineKeyboardButton(text='⬅️ Назад', callback_data='nb_metal_nb_back_price_all')

    markup.add(
        nb_gold_price,
        nb_silver_price,
        nb_platinum_price,
        nb_palladium_price,
        nb_metal_nb_back_price_all,

    )

    return markup