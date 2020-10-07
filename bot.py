import telebot
import cofig
from telebot import types
import api_nbrb_curs
import stavka_ref
import news_nbrb
import analitica

bot = telebot.TeleBot(cofig.token)


@bot.message_handler(commands=['start'])
def send_welcom(message):
    msg = bot.send_message(message.chat.id, 'Добро пожаловать!')
    key = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button_1 = types.KeyboardButton(text='Национальный банк')
    button_2 = types.KeyboardButton(text='Банки')
    key.add(button_1, button_2)
    bot.send_message(message.chat.id, 'Выберете интересующий раздел!', reply_markup=key)
    bot.register_next_step_handler(msg, name)


@bot.callback_query_handler(func=lambda message: True)
def name(message):
    if message.text == 'Национальный банк':
        key = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1_1 = types.InlineKeyboardButton(text='Ставки НБ', callback_data='stavki_nb')
        button_1_2 = types.InlineKeyboardButton(text='Курсы валют НБ', callback_data='curs_nb')
        button_1_3 = types.InlineKeyboardButton(text='Ликвидность', callback_data='liq_nb')
        button_1_4 = types.InlineKeyboardButton(text='МБК', callback_data='mbk_nb')
        button_1_5 = types.InlineKeyboardButton(text='Новости', callback_data='news_nb')
        button_1_6 = types.InlineKeyboardButton(text='Драг. металлы', callback_data='metall_nb')
        button_1_7 = types.InlineKeyboardButton(text='Назад', callback_data='back_nb')
        key.add(button_1_1, button_1_2, button_1_3, button_1_4, button_1_5, button_1_6, button_1_7)
        bot.send_message(message.chat.id, 'Какая информация вас интересует?', reply_markup=key)

    elif message.data == 'back_nb':
        key_back = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button_1_back = types.InlineKeyboardButton(text='Национальный банк', callback_data='nb')
        button_2_back = types.InlineKeyboardButton(text='Банки', callback_data='banki')
        key_back.add(button_1_back, button_2_back)
        bot.edit_message_text(chat_id=message.message.chat.id, message_id=message.message_id, text='sdfs', reply_markup=key_back)




#     send_text = 'Добро пожаловать! Бот Нацбанка готов к работе :)'
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     markup.row('Курсы Нацбанка', 'Новости Нацбанка', 'Ставка реф.')
#     if message.text == '/start':
#         bot.send_message(message.chat.id, send_text, reply_markup=markup)
#
#
# @bot.message_handler(content_types=['text'])
# def all_messages(message):
#     # if message.text != '/start':
#     #     bot.send_message(message.chat.id, message.text)
#
#     send_usd_text = 'На {} курс usd: {}'.format(api_nbrb_curs.get_usd_data(), api_nbrb_curs.get_usd_curs())
#
#     if message.text == 'Курсы Нацбанка':
#         bot.send_message(message.chat.id, send_usd_text)
#     if message.text == 'Новости Нацбанка':
#         bot.send_message(message.chat.id, news_nbrb.get_news(), parse_mode='HTML', disable_web_page_preview=True)
#     if message.text == 'Ставка реф.':
#         # bot.send_photo(message.chat.id, stavka_ref.get_sr())
#         bot.send_photo(message.chat.id, analitica.get_plot())


if __name__ == '__main__':
    bot.polling(none_stop=True)
