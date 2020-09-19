import telebot
import cofig

bot = telebot.TeleBot(cofig.token)


@bot.message_handler(content_types=['text'])
def all_messages(message):
    # if message.text != '/start':
    #     bot.send_message(message.chat.id, message.text)

    markup = telebot.types.ReplyKeyboardMarkup()
    markup.row('Курсы Нацбанка', 'Курсы банков')
    bot.send_message(message.chat.id, 'Курс не установлен!!!', reply_markup=markup)

    keyboard = telebot.types.InlineKeyboardMarkup()
    url_button = telebot.types.InlineKeyboardButton(text="Перейти на Яндекс", url="https://ya.ru")
    keyboard.add(url_button)
    bot.send_message(message.chat.id, "Привет! Нажми на кнопку и перейди в поисковик.", reply_markup=keyboard)


if __name__ == '__main__':
    bot.polling(none_stop=True)
