from telebot.types import InlineKeyboardButton, ReplyKeyboardMarkup


def get_base_menu():
    markup = ReplyKeyboardMarkup()
    markup.row_width = 2
    markup.resize_keyboard = True

    button_stavki_nb = InlineKeyboardButton(text='Ставки НБ', callback_data='stavki_nb')
    button_curs_nb = InlineKeyboardButton(text='Курсы валют НБ', callback_data='curs_nb')
    button_liq_nb = InlineKeyboardButton(text='Ликвидность', callback_data='liq_nb')
    button_mbk_nb = InlineKeyboardButton(text='МБК', callback_data='mbk_nb')
    button_news_nb = InlineKeyboardButton(text='Новости', callback_data='news_nb')
    button_matall_nb = InlineKeyboardButton(text='Драг. металлы', callback_data='metall_nb')
    button_back_nb = InlineKeyboardButton(text='⬅️ Назад', callback_data='back_nb')

    markup.add(
        button_stavki_nb,
        button_curs_nb,
        button_liq_nb,
        button_mbk_nb,
        button_news_nb,
        button_matall_nb,
        button_back_nb
    )

    return markup
