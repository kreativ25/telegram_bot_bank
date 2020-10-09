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

CALLBACK_BUTTON_MENU_NB = 'nb_menu'
CALLBACK_BUTTON_MENU_KB = 'kb_menu'
CALLBACK_BUTTON_STAVKI_NB = 'stavki_nb'
CALLBACK_BUTTON_CURS_NB = 'curs_nb'
CALLBACK_BUTTON_LIQ_NB = 'liq_nb'
CALLBACK_BUTTON_MBK_NB = 'mbk_nb'
CALLBACK_BUTTON_NEWS_NB = 'news_nb'
CALLBACK_BUTTON_METALL_NB = 'metall_nb'
CALLBACK_BUTTON_BACK_NB = 'back_nb'

TITLES_GLOBAL = {
    CALLBACK_BUTTON_MENU_NB: 'Национальный банк',
    CALLBACK_BUTTON_MENU_KB: 'Банки',
}

TITLES_NB = {
    CALLBACK_BUTTON_STAVKI_NB: 'Ставки НБ',
    CALLBACK_BUTTON_CURS_NB: 'Курсы валют НБ',
    CALLBACK_BUTTON_LIQ_NB: 'Ликвидность',
    CALLBACK_BUTTON_MBK_NB: 'МБК',
    CALLBACK_BUTTON_NEWS_NB: 'Новости',
    CALLBACK_BUTTON_METALL_NB: 'Драг. металлы',
    CALLBACK_BUTTON_BACK_NB: '⬅️ Назад'
}


# главное меню
def get_base_menu():
    keyboard = [
        [
            KeyboardButton(TITLES_GLOBAL[CALLBACK_BUTTON_MENU_NB]),
            KeyboardButton(TITLES_GLOBAL[CALLBACK_BUTTON_MENU_KB])
        ],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )


# меню Нацбанка
def get_menu_nb():
    keyboard = [
        [
            KeyboardButton(TITLES_NB[CALLBACK_BUTTON_STAVKI_NB]),
            KeyboardButton(TITLES_NB[CALLBACK_BUTTON_CURS_NB]),
            KeyboardButton(TITLES_NB[CALLBACK_BUTTON_LIQ_NB])
        ],
        [
            KeyboardButton(TITLES_NB[CALLBACK_BUTTON_MBK_NB]),
            KeyboardButton(TITLES_NB[CALLBACK_BUTTON_NEWS_NB]),
            KeyboardButton(TITLES_NB[CALLBACK_BUTTON_METALL_NB])
        ],
        [
            KeyboardButton(TITLES_NB[CALLBACK_BUTTON_BACK_NB])
        ],
    ]
    return ReplyKeyboardMarkup(
        keyboard=keyboard,
        resize_keyboard=True
    )


# функция обрабатывает комманду start
def do_start(update: Update, context: CallbackContext):
    update.message.reply_text(
        text='Добро пожаловать! :)',
        reply_markup=get_base_menu(),
    )


# функция обрабатывает все входящие сообщения не КОММАНДЫ
def do_echo(update: Update, context: CallbackContext):
    if update.message.text == TITLES_GLOBAL[CALLBACK_BUTTON_MENU_NB]:
        update.message.reply_text(
            text='Это меню НБ',
            reply_markup=get_menu_nb()
        )
    if update.message.text == TITLES_GLOBAL[CALLBACK_BUTTON_MENU_KB]:
        update.message.reply_text(
            text='Это меню банков',
            reply_markup=get_base_menu(),
        )
    if update.message.text == TITLES_NB[CALLBACK_BUTTON_BACK_NB]:
        update.message.reply_text(
            text='Главное меню',
            reply_markup=get_base_menu()
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
