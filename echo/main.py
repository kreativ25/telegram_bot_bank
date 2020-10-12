from telegram import Bot
from telegram import Update
from telegram import ParseMode
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CallbackContext
from telegram.ext import CallbackQueryHandler
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
    if update.message.text == menu_nb.TITLES_NB[menu_nb.CALLBACK_BUTTON_STAVKI_NB]:
        update.message.reply_text(
            text='Какая?',
            reply_markup=bl_nb_stavki.get_inline_nb_stavki()
        )


def do_menu(up: Update, context: CallbackContext):
    query = up.callback_query
    data = query.data
    chat_id = up.effective_message.chat_id
    current_text = up.effective_message.text

    if data == bl_nb_stavki.CALLBACK_BUTTON_STAVKI_SR:
        query.edit_message_text(
            text=current_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=bl_nb_stavki_sr.get_menu_inline_stavka_sr(),
        )
    if data == bl_nb_stavki_sr.CALLBACK_BUTTON_STAVKI_SR_BACK:
        query.edit_message_text(
            text=current_text,
            parse_mode=ParseMode.MARKDOWN,
            reply_markup=bl_nb_stavki.get_inline_nb_stavki()
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
    buttons_handler = CallbackQueryHandler(callback=do_menu, )

    # регистрируем обработчики
    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(echo_handler)
    updater.dispatcher.add_handler(buttons_handler)

    # запускаем скачивание обновлений
    updater.start_polling()
    updater.idle()  # чтобы обработчик не завершался пока не доработают все апдейты


if __name__ == '__main__':
    main()
