from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_menu_inline_kurs_kb():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3

    kurs_kb_usd = InlineKeyboardButton(text='🇺🇸 USD', callback_data='kurs_kb_usd')
    kurs_nb_eur = InlineKeyboardButton(text='🇪🇺 EUR', callback_data='kurs_nb_eur')

    kurs_kb_rub = InlineKeyboardButton(text='🇷🇺 RUB', callback_data='kurs_kb_rub')

    markup.add(
        kurs_kb_usd,
        kurs_nb_eur,
        kurs_kb_rub,

    )

    return markup