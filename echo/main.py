from echo.main_libraries import *
import matplotlib
bot = telebot.TeleBot(conf.token)


@bot.message_handler(commands=['start'])
# выводим глобальное меню
def send_welcom(message):
    bot.send_message(
        message.chat.id,
        'Добро пожаловать! 👋\n'
        'Выберите интересующий раздел!',
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
    if message.text == 'Курсы валют НБ':
        bot.send_message(
            chat_id=message.chat.id,
            text='Пожалуйста, сделайте выбор!',
            reply_markup=kurs_nb_global()
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

    # блок кнопок ставок по операциям НБ
    if message.data == 'nb_stavki_oper':
        bot.edit_message_text(
            text='Пожалуйста, сделайте выбор!',
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
            reply_markup=get_menu_inline_stavki_oper_nb()
        )

    # отправляем фото текущих ставок НБ
    if message.data == 'nb_stavki_oper_nb_1d':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=stavki_oper_nb_one(),
            reply_markup=get_menu_inline_stavki_oper_nb()
        )

    # отправка графика динамики ставок по операциям НБ
    if message.data == 'nb_satvki_oper_nb_all':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=stavki_oper_nb_all(),
            reply_markup=get_menu_inline_stavki_oper_nb()
        )

    # возвращаемся в предыдущее меню ставок НБ, удаляя сообщение
    if message.data == 'nb_stavki_oper_back':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_message(
            chat_id=message.message.chat.id,
            text='Пожалуйста, сделайте выбор',
            reply_markup=button_nb_stavki()
        )

    # отправляем фото текущих курсов валют НБ
    if message.data == 'nb_kurs_nb_1d':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=kurs_nb_one(),
            reply_markup=kurs_nb_global()
        )

    # меню выбора валюты - курсы НБ
    if message.data == 'nb_kurs_nb_all':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_message(
            chat_id=message.message.chat.id,
            text='Выберите валюту 👇',
            reply_markup=kurs_nb_cur_all()
        )

    # возвращаемся в предыдущее меню курсов НБ, удаляя сообщение
    if message.data == 'nb_kurs_nb_back_all':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_message(
            chat_id=message.message.chat.id,
            text='Пожалуйста, сделайте выбор',
            reply_markup=kurs_nb_global()
        )

    # показываем меню сроков курсов валют НБ для USD
    if message.data == 'nb_kurs_nb_usd_all':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_message(
            chat_id=message.message.chat.id,
            text='Пожалуйста, выберите период 👇',
            reply_markup=kurs_nb_for_4_cur('usd')
        )

    # возвращаемся в предыдущее меню выбора валюты курсов НБ, удаляя сообщение
    if message.data == 'nb_kurs_nb_cur_back_all':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_message(
            chat_id=message.message.chat.id,
            text='Пожалуйста, сделайте выбор',
            reply_markup=kurs_nb_cur_all()
        )

    # -------------------USD---------------------
    # отправляем фото динамики курса USD за неделю
    if message.data == 'nb_kurs_1w_usd':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=kurs_nb_all('usd', 7),
            reply_markup=kurs_nb_for_4_cur('usd')
        )

    # отправляем фото динамики курса USD за 2 недели
    if message.data == 'nb_kurs_2w_usd':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=kurs_nb_all('usd', 14),
            reply_markup=kurs_nb_for_4_cur('usd')
        )

    # отправляем фото динамики курса USD за 1 месяц
    if message.data == 'nb_kurs_1m_usd':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=kurs_nb_all('usd', 30),
            reply_markup=kurs_nb_for_4_cur('usd')
        )

    # отправляем фото динамики курса USD за 3 месяца
    if message.data == 'nb_kurs_3m_usd':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=kurs_nb_all('usd', 90),
            reply_markup=kurs_nb_for_4_cur('usd')
        )

    # отправляем фото динамики курса USD за 6 месяца
    if message.data == 'nb_kurs_6m_usd':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=kurs_nb_all('usd', 180),
            reply_markup=kurs_nb_for_4_cur('usd')
        )

    # отправляем фото динамики курса USD за 1 год
    if message.data == 'nb_kurs_12m_usd':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=kurs_nb_all('usd', 365),
            reply_markup=kurs_nb_for_4_cur('usd')
        )

    # -------------------EUR---------------------
    # показываем меню сроков курсов валют НБ для EUR
    if message.data == 'nb_kurs_nb_eur_all':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_message(
            chat_id=message.message.chat.id,
            text='Пожалуйста, выберите период 👇',
            reply_markup=kurs_nb_for_4_cur('eur')
        )

    # отправляем фото динамики курса EUR за неделю
    if message.data == 'nb_kurs_1w_eur':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=kurs_nb_all('eur', 7),
            reply_markup=kurs_nb_for_4_cur('eur')
        )

    # отправляем фото динамики курса EUR за 2 недели
    if message.data == 'nb_kurs_2w_eur':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=kurs_nb_all('eur', 14),
            reply_markup=kurs_nb_for_4_cur('eur')
        )

    # отправляем фото динамики курса EUR за 1 месяц
    if message.data == 'nb_kurs_1m_eur':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=kurs_nb_all('eur', 30),
            reply_markup=kurs_nb_for_4_cur('eur')
        )

    # отправляем фото динамики курса EUR за 3 месяца
    if message.data == 'nb_kurs_3m_eur':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=kurs_nb_all('eur', 90),
            reply_markup=kurs_nb_for_4_cur('eur')
        )

    # отправляем фото динамики курса EUR за 6 месяца
    if message.data == 'nb_kurs_6m_eur':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=kurs_nb_all('eur', 180),
            reply_markup=kurs_nb_for_4_cur('eur')
        )

    # отправляем фото динамики курса EUR за 1 год
    if message.data == 'nb_kurs_12m_eur':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=kurs_nb_all('eur', 365),
            reply_markup=kurs_nb_for_4_cur('eur')
        )

    # -------------------RUB---------------------
    # показываем меню сроков курсов валют НБ для RUB
    if message.data == 'nb_kurs_nb_rub_all':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_message(
            chat_id=message.message.chat.id,
            text='Пожалуйста, выберите период 👇',
            reply_markup=kurs_nb_for_4_cur('rub')
        )

    # отправляем фото динамики курса RUB за неделю
    if message.data == 'nb_kurs_1w_rub':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=kurs_nb_all('rub', 7),
            reply_markup=kurs_nb_for_4_cur('rub')
        )

    # отправляем фото динамики курса RUB за 2 недели
    if message.data == 'nb_kurs_2w_rub':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=kurs_nb_all('rub', 14),
            reply_markup=kurs_nb_for_4_cur('rub')
        )

    # отправляем фото динамики курса RUB за 1 месяц
    if message.data == 'nb_kurs_1m_rub':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=kurs_nb_all('rub', 30),
            reply_markup=kurs_nb_for_4_cur('rub')
        )

    # отправляем фото динамики курса RUB за 3 месяца
    if message.data == 'nb_kurs_3m_rub':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=kurs_nb_all('rub', 90),
            reply_markup=kurs_nb_for_4_cur('rub')
        )

    # отправляем фото динамики курса RUB за 6 месяца
    if message.data == 'nb_kurs_6m_rub':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=kurs_nb_all('rub', 180),
            reply_markup=kurs_nb_for_4_cur('rub')
        )

    # отправляем фото динамики курса RUB за 1 год
    if message.data == 'nb_kurs_12m_rub':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=kurs_nb_all('rub', 365),
            reply_markup=kurs_nb_for_4_cur('rub')
        )

    # -------------------PLN---------------------
    # показываем меню сроков курсов валют НБ для PLN
    if message.data == 'nb_kurs_nb_pln_all':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_message(
            chat_id=message.message.chat.id,
            text='Пожалуйста, выберите период 👇',
            reply_markup=kurs_nb_for_4_cur('pln')
        )

    # отправляем фото динамики курса PLN за неделю
    if message.data == 'nb_kurs_1w_pln':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=kurs_nb_all('pln', 7),
            reply_markup=kurs_nb_for_4_cur('pln')
        )

    # отправляем фото динамики курса PLN за 2 недели
    if message.data == 'nb_kurs_2w_pln':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=kurs_nb_all('pln', 14),
            reply_markup=kurs_nb_for_4_cur('pln')
        )

    # отправляем фото динамики курса PLN за 1 месяц
    if message.data == 'nb_kurs_1m_pln':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=kurs_nb_all('pln', 30),
            reply_markup=kurs_nb_for_4_cur('pln')
        )

    # отправляем фото динамики курса PLN за 3 месяца
    if message.data == 'nb_kurs_3m_pln':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=kurs_nb_all('pln', 90),
            reply_markup=kurs_nb_for_4_cur('pln')
        )

    # отправляем фото динамики курса PLN за 6 месяца
    if message.data == 'nb_kurs_6m_pln':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=kurs_nb_all('pln', 180),
            reply_markup=kurs_nb_for_4_cur('pln')
        )

    # отправляем фото динамики курса PLN за 1 год
    if message.data == 'nb_kurs_12m_pln':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=kurs_nb_all('pln', 365),
            reply_markup=kurs_nb_for_4_cur('pln')
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
