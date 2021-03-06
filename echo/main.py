# -*- coding: utf-8 -*-
from echo.main_libraries import *

bot = telebot.TeleBot(conf.token)
from echo.nbrb.kurs.api_nbrb_curs import get_kurs_nb

import re


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
    if message.text == 'Банки':
        bot.send_message(
            chat_id=message.chat.id,
            text='Какая информация Вас интересует?',
            reply_markup=get_base_menu_kb()
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
    if message.text == 'Драг. металлы':
        bot.send_message(
            chat_id=message.chat.id,
            text='Пожалуйста, сделайте выбор!',
            reply_markup=menu_metal()
        )
    if message.text == 'Ликвидность':
        bot.send_message(
            chat_id=message.chat.id,
            text='Пожалуйста, сделайте выбор!',
            reply_markup=get_inline_nb_liq()
        )

    if message.text == 'МБК':
        bot.send_message(
            chat_id=message.chat.id,
            text='Пожалуйста, сделайте выбор!',
            reply_markup=get_inline_nb_mbk()
        )

    if message.text == 'Курсы валют':
        bot.send_message(
            chat_id=message.chat.id,
            text='Пожалуйста, сделайте выбор!\nПринцип сортировки - курс продажи по возрастанию!',
            reply_markup=get_menu_inline_kurs_kb()
        )

    if message.text == 'Конвертер валют':
        text_converter = 'Привет! 👋\n\n' \
                         'Я конвертирую белорусские рубли в доллары США, евро, российские рубли, гривны,' \
                         ' польские злотые и обратно.\n\n' \
                         'Примеры запросов:\n' \
                         '🇺🇸 Доллары США: 7 usd, 7 долларов;\n' \
                         '🇪🇺 Евро: 14 eur, 14 евро;\n' \
                         '🇷🇺 Российские рубли: 5 rub, 5 россии;\n' \
                         '🇺🇦 Гривны: 10 uah, 10 гривен;\n' \
                         '🇵🇱 Злотые: 20 pln, 20 злотых. '

        bot.send_message(
            chat_id=message.chat.id,
            parse_mode='HTML',
            text=text_converter,
        )

    if message.text == 'Обратная связь':
        text_mail = 'Привет! 👋\n\n' \
                         'Мне можно написать любой вопрос, отправив сообщение в Telegram:\n' \
                         'https://t.me/Bel_bot_bank' \


        bot.send_message(
            chat_id=message.chat.id,
            parse_mode='HTML',
            disable_web_page_preview=True,
            text=text_mail,
        )








    # конвертер валют
    if converter(message.text):
        bot.send_message(
            chat_id=message.chat.id,
            parse_mode='HTML',
            disable_web_page_preview=True,
            text=converter(message.text),

        )


    if message.text == 'Новости гос. органов':
        bot.send_message(
            chat_id=message.chat.id,
            text='Пожалуйста, сделайте выбор!',
            reply_markup=get_inline_gos_news()
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

    # отправляем фото динамики курса USD за год
    if message.data == 'nb_kurs_nb_usd_all':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=get_curs_all('usd', 'Доллара США'),
            reply_markup=kurs_nb_cur_all()
        )

    # отправляем фото динамики курса EUR за год
    if message.data == 'nb_kurs_nb_eur_all':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=get_curs_all('eur', 'Евро'),
            reply_markup=kurs_nb_cur_all()
        )

    # отправляем фото динамики курса RUB за год
    if message.data == 'nb_kurs_nb_rub_all':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=get_curs_all('rub', 'Российского рубля'),
            reply_markup=kurs_nb_cur_all()
        )

    # отправляем фото динамики курса PLN за год
    if message.data == 'nb_kurs_nb_pln_all':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=get_curs_all('pln', 'Польского злотого'),
            reply_markup=kurs_nb_cur_all()
        )

    # список металлов в разделе учетные цены НБ
    if message.data == 'nb_metal_nb_price':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_message(
            chat_id=message.message.chat.id,
            text='Пожалуйста, сделайте выбор',
            reply_markup=menu_metal_price()
        )

    # список металлов в разделе цены на мерные слитки НБ
    if message.data == 'nb_metal_nb_ingot':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_message(
            chat_id=message.message.chat.id,
            text='Пожалуйста, сделайте выбор',
            reply_markup=menu_metal_ignot()
        )
    # кнопка назад в разделе металлов
    if message.data == 'nb_metal_nb_back_price_all':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_message(
            chat_id=message.message.chat.id,
            text='Пожалуйста, сделайте выбор',
            reply_markup=menu_metal()
        )

    # отправляем фото динамики золота
    if message.data == 'nb_gold_price':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=get_nb_photo_metal_price_all('gold', 'ЗОЛОТО'),
            reply_markup=menu_metal_price()
        )

    # отправляем фото динамики серебра
    if message.data == 'nb_silver_price':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=get_nb_photo_metal_price_all('silver', 'СЕРЕБРО'),
            reply_markup=menu_metal_price()
        )

    # отправляем фото динамики платины
    if message.data == 'nb_platinum_price':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=get_nb_photo_metal_price_all('platinum', 'ПЛАТИНУ'),
            reply_markup=menu_metal_price()
        )

    # отправляем фото динамики палладия
    if message.data == 'nb_palladium_price':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=get_nb_photo_metal_price_all('palladium', 'ПАЛЛАДИЙ'),
            reply_markup=menu_metal_price()
        )

    # отправляем фото цен золотых мерных слитков
    if message.data == 'nb_gold_ignot':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=get_gold_ignot(),
            reply_markup=menu_metal_ignot()
        )

    # отправляем фото цен серебренных мерных слитков
    if message.data == 'nb_silver_ignot':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=get_silver_ignot(),
            reply_markup=menu_metal_ignot()
        )

    # отправляем фото цен платиновых мерных слитков
    if message.data == 'nb_platinum_ignot':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=get_platinum_ignot(),
            reply_markup=menu_metal_ignot()
        )

    # отправка графика динамики ликвидности
    if message.data == 'nb_liq_dinamiq':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=get_liq_all(),
            reply_markup=get_inline_nb_liq()
        )

    # отправка текущей ликвидности
    if message.data == 'nb_liq':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=get_img_liq_one(),
            reply_markup=get_inline_nb_liq()
        )

    # отправка текущей ставки МБК
    if message.data == 'button_mbk':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=get_img_mbk_one(),
            reply_markup=get_inline_nb_mbk()
        )
    # отправка динамики МБК
    if message.data == 'button_mbk_dinamiq':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=get_mbk(),
            reply_markup=get_inline_nb_mbk()
        )

    # отправка текущих курсов банков  - Доллар США
    if message.data == 'kurs_kb_usd':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=curs('usd_in', 'usd_out'),
            reply_markup=get_menu_inline_kurs_kb()
        )

    # отправка текущих курсов банков  - Евро
    if message.data == 'kurs_nb_eur':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=curs('eur_in', 'eur_out'),
            reply_markup=get_menu_inline_kurs_kb()
        )
    # отправка текущих курсов банков  - Российские рубли
    if message.data == 'kurs_kb_rub':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_photo(
            chat_id=message.message.chat.id,
            photo=curs('rub_in', 'rub_out'),
            reply_markup=get_menu_inline_kurs_kb()
        )

    # отправляем новости госорганов - Минэкономики
    if message.data == 'button_news_economy':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_message(
            chat_id=message.message.chat.id,
            text=get_economy(),
            parse_mode='HTML',
            disable_web_page_preview=True,
            reply_markup=get_inline_gos_news()
        )
    # отправляем новости госорганов - Минфин
    if message.data == 'button_news_minfin':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_message(
            chat_id=message.message.chat.id,
            text=get_minfin(),
            parse_mode='HTML',
            disable_web_page_preview=True,
            reply_markup=get_inline_gos_news()
        )

    # отправляем новости госорганов - Мингорисполком
    if message.data == 'button_news_migorispolcom':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_message(
            chat_id=message.message.chat.id,
            text=get_mingor(),
            parse_mode='HTML',
            disable_web_page_preview=True,
            reply_markup=get_inline_gos_news()
        )

    # отправляем новости госорганов - Налоговая
    if message.data == 'button_news_nalog':
        bot.delete_message(
            chat_id=message.message.chat.id,
            message_id=message.message.message_id,
        )
        bot.send_message(
            chat_id=message.message.chat.id,
            text=get_nalog(),
            parse_mode='HTML',
            disable_web_page_preview=True,
            reply_markup=get_inline_gos_news()
        )


if __name__ == '__main__':
    # infinity_polling(True) нужен для обхода падения бота путем перезапуска его
    bot.infinity_polling(none_stop=True, timeout=120)

    # bot.polling(
    #     none_stop=True,
    #     timeout=60
    #
    # )
