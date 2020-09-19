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


# @bot.message_handler(content_types=['text'])
# def curs(message_kb):
#     markup_kb = telebot.types.ReplyKeyboardMarkup()
#     markup_kb.row('Курсы банков')
#     bot.send_message(message_kb.chat.id, 'Курс банков пока не установлен!!!', reply_markup=markup_kb)


if __name__ == '__main__':
    bot.polling(none_stop=True)
