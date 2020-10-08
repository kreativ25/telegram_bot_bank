from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CallbackContext

from echo.cofig import token


# функция обрабатывает комманду start
def do_start(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Добро пожаловать! :)'
    )


# функция обрабатывает все входящие сообщения не КОММАНДЫ
def do_echo(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    text = update.message.text
    update.message.reply_text(
        text='Такой комманды не существует'
    )


def main():
    bot = Bot(
        token=token,
    )
    updater = Updater(
        bot=bot,
    )
    start_handler = CommandHandler('start', do_start)  # добавляем обработчик комманды start
    echo_handler = MessageHandler(Filters.text, do_echo)  # обработчик любых текствоых сообщений - НЕ КОММАНД

    # регистрируем обработчики
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(echo_handler)

    # запускаем скачивание обновлений
    updater.start_polling()
    updater.idle()  # чтобы обработчик не завершался пока не доработают все апдейты


if __name__ == '__main__':
    main()
