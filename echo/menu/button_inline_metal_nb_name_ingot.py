from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_menu_inline_metal_nb_ignot_all():
    markup = InlineKeyboardMarkup()
    markup.row_width = 1

    nb_gold_ignot = InlineKeyboardButton(text='🥇 Золото', callback_data='nb_gold_ignot')
    nb_silver_ignot = InlineKeyboardButton(text='🥈 Серебро', callback_data='nb_silver_ignot')
    nb_platinum_ignot = InlineKeyboardButton(text='📏 Платина', callback_data='nb_platinum_ignot')
    nb_metal_nb_back_price_all = InlineKeyboardButton(text='⬅️ Назад', callback_data='nb_metal_nb_back_price_all')

    markup.add(
        nb_gold_ignot,
        nb_silver_ignot,
        nb_platinum_ignot,
        nb_metal_nb_back_price_all,

    )

    return markup