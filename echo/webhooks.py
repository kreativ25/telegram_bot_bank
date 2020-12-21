import telebot
from flask import Flask, request

token = ''
secret = ''
url = '' + secret

bot = telebot.TeleBot(token, threaded=False)
bot.remove_webhook()
bot.set_webhook(url=url)

app = Flask(__name__)


@app.route('/' + secret, methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return 'ok', 200

@bot.message_handler(commands=['start'])
# выводим глобальное меню
def send_welcom(message):
    bot.send_message(
        message.chat.id,
        'Добро пожаловать! 👋\n'
        'Выберите интересующий раздел!',
        # reply_markup=global_menu()
    )


# kreativ25.pythonanywhere.com