import telebot

from telebot import types
import api_nbrb_curs
# import echo.stavka_ref as stavka_ref
import news_nbrb
import echo.analitica as analitica
import echo.cofig as cofig

bot = telebot.TeleBot(cofig.token)

CALLBACK_BUTTON_1_MENU_NB = 'nb_menu'
CALLBACK_BUTTON_2_MENU_KB = 'kb_menu'
CALLBACK_BUTTON_STAVKI_NB = 'stavki_nb'
CALLBACK_BUTTON_CURS_NB = 'curs_nb'
CALLBACK_BUTTON_LIQ_NB = 'liq_nb'
CALLBACK_BUTTON_MBK_NB = 'mbk_nb'
CALLBACK_BUTTON_NEWS_NB = 'news_nb'
CALLBACK_BUTTON_METALL_NB = 'metall_nb'
CALLBACK_BUTTON_BACK_NB = 'back_nb'

TITLES = {
    CALLBACK_BUTTON_1_MENU_NB: 'Национальный банк',
    CALLBACK_BUTTON_2_MENU_KB: 'Банки',
    CALLBACK_BUTTON_STAVKI_NB: 'Ставки НБ',
    CALLBACK_BUTTON_CURS_NB: 'Курсы валют НБ',
    CALLBACK_BUTTON_LIQ_NB: 'Ликвидность',
    CALLBACK_BUTTON_MBK_NB: 'МБК',
    CALLBACK_BUTTON_NEWS_NB: 'Новости',
    CALLBACK_BUTTON_METALL_NB: 'Драг. металлы',
    CALLBACK_BUTTON_BACK_NB: '⬅️ Назад'
}



@bot.message_handler(commands=['start'])
def send_welcom(call):
    msg = bot.send_message(call.chat.id, 'Добро пожаловать!')
    key = types. InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton(text='Национальный банк', callback_data=CALLBACK_BUTTON_1_MENU_NB)
    button_2 = types.InlineKeyboardButton(text='Банки', callback_data=CALLBACK_BUTTON_2_MENU_KB)
    key.add(button_1, button_2)
    bot.send_message(call.chat.id, 'Выберете интересующий раздел!', reply_markup=key)
    bot.register_next_step_handler(msg, name)


@bot.callback_query_handler(func=lambda call_nb: True)
def name(call_nb):
    # if call_nb.text == 'Национальный банк':
    #     key = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     button_1_1 = types.InlineKeyboardButton(text='Ставки НБ', callback_data=CALLBACK_BUTTON_STAVKI_NB)
    #     button_1_2 = types.InlineKeyboardButton(text='Курсы валют НБ', callback_data=CALLBACK_BUTTON_CURS_NB)
    #     button_1_3 = types.InlineKeyboardButton(text='Ликвидность', callback_data=CALLBACK_BUTTON_LIQ_NB)
    #     button_1_4 = types.InlineKeyboardButton(text='МБК', callback_data=CALLBACK_BUTTON_MBK_NB)
    #     button_1_5 = types.InlineKeyboardButton(text='Новости', callback_data=CALLBACK_BUTTON_NEWS_NB)
    #     button_1_6 = types.InlineKeyboardButton(text='Драг. металлы', callback_data=CALLBACK_BUTTON_METALL_NB)
    #     button_1_7 = types.InlineKeyboardButton(text='⬅️ Назад', callback_data=CALLBACK_BUTTON_BACK_NB)
    #     key.add(button_1_1, button_1_2, button_1_3, button_1_4, button_1_5, button_1_6, button_1_7)
    #     bot.send_message(call_nb.chat.id, 'Какая информация вас интересует?', reply_markup=key)
    #
    # elif call_nb.data == 'back_nb':
    #     key_back = types.ReplyKeyboardMarkup(resize_keyboard=True)
    #     button_1_back = types.InlineKeyboardButton(text='Национальный банк', callback_data=CALLBACK_BUTTON_1_MENU_NB)
    #     button_2_back = types.InlineKeyboardButton(text='Банки', callback_data=CALLBACK_BUTTON_2_MENU_KB)
    #     key_back.add(button_1_back, button_2_back)
    #     bot.edit_message_text(chat_id=call_nb.message.chat.id, message_id=call_nb.message_id, text='sdfs',
    #                           reply_markup=key_back)

    if call_nb.data == 'nb_menu':
        bot.send_photo(chat_id=call_nb.message.chat.id, photo=analitica.get_plot())


    # send_text = 'Добро пожаловать! Бот Нацбанка готов к работе :)'
    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    # markup.row('Курсы Нацбанка', 'Новости Нацбанка', 'Ставка реф.')
    # if message.text == '/start':
    #     bot.send_message(message.chat.id, send_text, reply_markup=markup)


@bot.message_handler(content_types=['text'])
def all_messages(message):
    # if message.text != '/start':
    #     bot.send_message(message.chat.id, message.text)

    send_usd_text = 'На {} курс usd: {}'.format(api_nbrb_curs.get_usd_data(), api_nbrb_curs.get_usd_curs())

    if message.text == 'Курсы Нацбанка':
        bot.send_message(message.chat.id, send_usd_text)
    if message.text == 'Новости Нацбанка':
        bot.send_message(message.chat.id, news_nbrb.get_news(), parse_mode='HTML', disable_web_page_preview=True)
    # if message.text == 'Ставки НБ':
        # bot.send_photo(message.chat.id, stavka_ref.get_sr())
        # bot.send_photo(message.chat.id, analitica.get_plot())



if __name__ == '__main__':
    bot.polling(none_stop=True)
