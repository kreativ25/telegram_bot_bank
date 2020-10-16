import telebot
from echo import config, analitica
from telebot import types
import api_nbrb_curs
from echo.nbrb.news import news_nbrb

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start'])
def send_welcom(message):
    send_text = 'Добро пожаловать! Бот Нацбанка готов к работе :)'
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Курсы Нацбанка', 'Новости Нацбанка', 'Ставка реф.')
    if message.text == '/start':
        bot.send_message(message.chat.id, send_text, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def all_messages(message):
    # if message.text != '/start':
    #     bot.send_message(message.chat.id, message.text)

    send_usd_text = 'На {} курс usd: {}'.format(api_nbrb_curs.get_usd_data(), api_nbrb_curs.get_usd_curs())

    if message.text == 'Курсы Нацбанка':
        bot.send_message(message.chat.id, send_usd_text)
    if message.text == 'Новости Нацбанка':
        bot.send_message(message.chat.id, news_nbrb.get_news(), parse_mode='HTML', disable_web_page_preview=True)
    if message.text == 'Ставка реф.':
        # bot.send_photo(message.chat.id, stavka_ref.get_sr())
        bot.send_photo(message.chat.id, analitica.get_plot())

    #
    # markup = telebot.types.ReplyKeyboardMarkup()
    # markup.row('Курсы Нацбанка', 'Курсы банков')
    # bot.send_message(message.chat.id, 'Курс не установлен!!!', reply_markup=markup)
    #
    # keyboard = telebot.types.InlineKeyboardMarkup()
    # url_button = telebot.types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
    # keyboard.add(url_button)
    # bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)


if __name__ == '__main__':
    bot.polling(none_stop=True)
