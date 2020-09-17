import telebot
import token

bot = telebot.TeleBot(token.TOKEN)

bot.polling()
