from echo.main_libraries import *

bot = telebot.TeleBot(conf.token)


@bot.message_handler(commands=['start'])
# выводим глобальное меню
def send_welcom(message):
    bot.send_message(
        message.chat.id,
        'Добро пожаловать! 👋\n'
        'Выбирите интересующий раздел!',
        reply_markup=global_menu()
    )


@bot.message_handler(content_types=['text'])
# выводим меню НБ
def send_menu_nb(message):
    if message.text == 'Национальный банк':
        bot.send_message(
            chat_id=message.chat.id,
            text='Какая информация Вас интересует?',
            reply_markup=button_menu_nb()
        )
    if message.text == '⬅️ Назад':
        bot.send_message(
            chat_id=message.chat.id,
            text='Выбирите интересующий раздел!',
            reply_markup=global_menu()
        )
    if message.text == 'Ставки НБ':
        bot.send_message(
            chat_id=message.chat.id,
            text='Пожалуйста, сделайте выбор!',
            reply_markup=button_nb_stavki()
        )
    if message.text == 'Новости':
        bot.send_message(
            chat_id=message.chat.id,
            text='Пожалуйста, сделайте выбор!',
            reply_markup=button_nb_news()
        )


@bot.callback_query_handler(func=lambda message: True)
def send_menu_nb_sr(message):
    # меню ставки СР
    if message.data == 'nb_stavki_sr':
        bot.edit_message_text(
            text='Пожалуйста, сделайте выбор!',
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
            reply_markup=button_nb_sr()
        )

    # кнопка назад в меню ставок НБ
    if message.data == 'nb_stavka_sr_back':
        bot.edit_message_text(
            text='Пожалуйста, сделайте выбор!',
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
            reply_markup=button_nb_stavki()
        )

    # отправляем фото однодневной ставки СР
    if message.data == 'nb_stavka_sr_1d':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=get_sr_1d(),
            reply_markup=button_nb_sr_2()
        )

    # возвращаемся в предыдущее инлайн меню, удаляя сообщение
    if message.data == 'nb_inline_stavka_sr_back':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_message(
            chat_id=message.message.chat.id,
            text='Пожалуйста, сделайте выбор',
            reply_markup=button_nb_stavki()
        )

    # отправка графика динамики ставки рефинансирования
    if message.data == 'nb_satvka_sr_all':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=button_nb_sr_all(),
            reply_markup=button_nb_sr_2()
        )

    # отправляем новости НБ - раздел "Новости"
    if message.data == 'nb_news_news':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_message(
            chat_id=message.message.chat.id,
            text=news_nb(),
            parse_mode='HTML',
            disable_web_page_preview=True,
            reply_markup=button_nb_news()
        )

    # отправляем новости НБ - раздел "Пресс-релизы"
    if message.data == 'nb_news_press':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_message(
            chat_id=message.message.chat.id,
            text=news_press(),
            parse_mode='HTML',
            disable_web_page_preview=True,
            reply_markup=button_nb_news()
        )

    # отправляем новости НБ - раздел "Аналитика"
    if message.data == 'nb_news_analitic':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_message(
            chat_id=message.message.chat.id,
            text=news_analitic(),
            parse_mode='HTML',
            disable_web_page_preview=True,
            reply_markup=button_nb_news()
        )

    # отправляем новости НБ - раздел "Статистика"
    if message.data == 'nb_news_stat':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_message(
            chat_id=message.message.chat.id,
            text=news_statistic(),
            parse_mode='HTML',
            disable_web_page_preview=True,
            reply_markup=button_nb_news()
        )


if __name__ == '__main__':
    bot.polling(none_stop=True)














# from telegram import Bot
# from telegram import Update
# from telegram import ParseMode
# from telegram.ext import Updater
# from telegram.ext import CommandHandler
# from telegram.ext import MessageHandler
# from telegram.ext import Filters
# from telegram.ext import CallbackContext
# from telegram.ext import CallbackQueryHandler
# from echo.cofig import token
#
# import echo.menu.button_inline_nb_stavki as bl_nb_stavki
# import echo.menu.button_nb_sr as bl_nb_stavki_sr
# import echo.menu.global_menu as global_menu
# import echo.menu.button_menu_nb as menu_nb
#
#
# # функция обрабатывает комманду start
# def do_start(update: Update, context: CallbackContext):
#     update.message.reply_text(
#         text='Добро пожаловать! :)',
#         reply_markup=global_menu.get_base_menu(),
#     )
#
#
# # функция обрабатывает все входящие сообщения не КОММАНДЫ
# def do_echo(update: Update, context: CallbackContext):
#     if update.message.text == global_menu.TITLES_GLOBAL[global_menu.CALLBACK_BUTTON_MENU_NB]:
#         update.message.reply_text(
#             text='Это меню НБ',
#             reply_markup=menu_nb.get_menu_nb()
#         )
#     if update.message.text == global_menu.TITLES_GLOBAL[global_menu.CALLBACK_BUTTON_MENU_KB]:
#         update.message.reply_text(
#             text='Это меню банков',
#             reply_markup=global_menu.get_base_menu(),
#         )
#     if update.message.text == menu_nb.TITLES_NB[menu_nb.CALLBACK_BUTTON_BACK_NB]:
#         update.message.reply_text(
#             text='Главное меню',
#             reply_markup=global_menu.get_base_menu()
#         )
#     if update.message.text == menu_nb.TITLES_NB[menu_nb.CALLBACK_BUTTON_STAVKI_NB]:
#         update.message.reply_text(
#             text='Какая?',
#             reply_markup=bl_nb_stavki.get_inline_nb_stavki()
#         )
#
#
# def do_menu(up: Update, context: CallbackContext):
#     query = up.callback_query
#     data = query.data
#     chat_id = up.effective_message.chat_id
#     current_text = up.effective_message.text
#
#     if data == bl_nb_stavki.CALLBACK_BUTTON_STAVKI_SR:
#         query.edit_message_text(
#             text=current_text,
#             parse_mode=ParseMode.MARKDOWN,
#             reply_markup=bl_nb_stavki_sr.get_menu_inline_stavka_sr(),
#         )
#     if data == bl_nb_stavki_sr.CALLBACK_BUTTON_STAVKI_SR_BACK:
#         query.edit_message_text(
#             text=current_text,
#             parse_mode=ParseMode.MARKDOWN,
#             reply_markup=bl_nb_stavki.get_inline_nb_stavki()
#         )
#
#
# def main():
#     bot = Bot(
#         token=token,
#     )
#     updater = Updater(
#         bot=bot,
#     )
#     start_handler = CommandHandler('start', do_start)  # добавляем обработчик комманды start
#     echo_handler = MessageHandler(Filters.text, do_echo)  # обработчик любых текствоых сообщений - НЕ КОММАНД
#     buttons_handler = CallbackQueryHandler(callback=do_menu, )
#
#     # регистрируем обработчики
#     updater.dispatcher.add_handler(start_handler)
#     updater.dispatcher.add_handler(echo_handler)
#     updater.dispatcher.add_handler(buttons_handler)
#
#     # запускаем скачивание обновлений
#     updater.start_polling()
#     updater.idle()  # чтобы обработчик не завершался пока не доработают все апдейты
#
#
# if __name__ == '__main__':
#     main()
