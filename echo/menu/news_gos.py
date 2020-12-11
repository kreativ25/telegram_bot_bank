from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_inline_gos_news():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2

    button_news_minfin = InlineKeyboardButton(text='Минфин', callback_data='button_news_minfin')
    button_news_economy = InlineKeyboardButton(text='Минэкономики', callback_data='button_news_economy')
    button_news_nalog = InlineKeyboardButton(text='МНС', callback_data='button_news_nalog')
    button_news_migorispolcom = InlineKeyboardButton(text='Мингорисполком', callback_data='button_news_migorispolcom')

    markup.add(
        button_news_minfin,
        button_news_economy,
        button_news_nalog,
        button_news_migorispolcom
    )

    return markup