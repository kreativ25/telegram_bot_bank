from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_inline_nb_news():
    markup = InlineKeyboardMarkup()
    markup.row_width = 2

    button_news_news = InlineKeyboardButton(text='Новости', callback_data='nb_news_news')
    button_news_press = InlineKeyboardButton(text='Пресс-релизы', callback_data='nb_news_press')
    button_news_stat = InlineKeyboardButton(text='Cтатистика', callback_data='nb_news_stat')
    button_news_analitic = InlineKeyboardButton(text='Аналитика', callback_data='nb_news_analitic')

    markup.add(
        button_news_press,
        button_news_news,
        button_news_stat,
        button_news_analitic
    )

    return markup