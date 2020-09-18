import telebot
import cofig

bot = telebot.TeleBot(cofig.token)


@bot.message_handler(content_types=['text'])
def all_messages(message):
    if message.text != '/start':
        bot.send_message(message.chat.id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)

