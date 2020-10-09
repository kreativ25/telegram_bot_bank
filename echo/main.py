from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from telegram.ext import CallbackContext

from echo.cofig import token
import echo.menu.button as bt
import echo.menu.button_nb_sr as menu_sr
import echo.menu.button_stavki_oper as menu_oper


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

    if update.message.text == bt.TITLES_NB[bt.CALLBACK_BUTTON_STAVKI_NB]:
        update.message.reply_text(
            text='Раздел ставки Национального банка',
            reply_markup=bt.get_menu_stavki_nb()
        )

    if update.message.text == bt.TITLES_STAVKI_NB[bt.CALLBACK_BUTTON_STAVKI_BACK]:
        update.message.reply_text(
            text='Раздел информации Национального банка',
            reply_markup=bt.get_menu_nb()
        )
    if update.message.text == bt.TITLES_STAVKI_NB[bt.CALLBACK_BUTTON_STAVKI_SR]:
        update.message.reply_text(
            text='Раздел ставка реф-я НБ',
            reply_markup=menu_sr.get_menu_stavka_sr()
        )
    if update.message.text == menu_sr.TITLES_STAVKI_NB_SR[menu_sr.CALLBACK_BUTTON_STAVKI_SR_BACK]:
        update.message.reply_text(
            text='Раздел ставок НБ',
            reply_markup=bt.get_menu_stavki_nb()
        )
    if update.message.text == menu_sr.TITLES_STAVKI_NB_SR[menu_sr.CALLBACK_BUTTON_STAVKI_SR_BACK_MENU]:
        update.message.reply_text(
            text='Раздел информации Национального банка',
            reply_markup=bt.get_menu_nb()
        )
    if update.message.text == bt.TITLES_STAVKI_NB[bt.CALLBACK_BUTTON_STAVKI_OPER]:
        update.message.reply_text(
            text='Раздел ставок Национального банка',
            reply_markup=menu_oper.get_menu_stavki_oper()
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
