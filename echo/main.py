from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CallbackContext
from telegram import InlineKeyboardMarkup
from telegram import InlineKeyboardButton
from telegram.ext import CallbackQueryHandler
from telegram import KeyboardButton
from telegram import ReplyKeyboardMarkup

from echo.cofig import token
import echo.button as bt

# функция обрабатывает комманду start
def do_start(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Добро пожаловать! :)',
        reply_markup=bt.get_base_menu(),
    )


# функция обрабатывает все входящие сообщения не КОММАНДЫ
def do_echo(update: Update, context: CallbackContext):
    if update.message.text == bt.TITLES_GLOBAL[bt.CALLBACK_BUTTON_MENU_NB]:
        update.message.reply_text(
            text='Это меню НБ',
            reply_markup=bt.get_menu_nb()
        )
    if update.message.text == bt.TITLES_GLOBAL[bt.CALLBACK_BUTTON_MENU_KB]:
        update.message.reply_text(
            text='Это меню банков',
            reply_markup=bt.get_base_menu(),
        )
    if update.message.text == bt.TITLES_NB[bt.CALLBACK_BUTTON_BACK_NB]:
        update.message.reply_text(
            text='Главное меню',
            reply_markup=bt.get_base_menu()
        )

        # update.callback_query.edit_message_reply_markup(
        #     chat_id=update.callback_query.message.chat_id,
        #     mmessage_id=update.callback_query.message.message_id,
        #     reply_markup=get_base_menu2())
        # bot.edit_message_reply_markup(
        #     chat_id=update.callback_query.message.chat_id,
        #     mmessage_id=update.callback_query.message.message_id,
        #     reply_markup=get_base_menu2()
        # )


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
