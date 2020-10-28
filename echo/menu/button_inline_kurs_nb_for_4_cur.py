from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


def get_menu_inline_kurs_nb_for_4_cur(cur):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2

    nb_kurs_1w = InlineKeyboardButton(text='1 неделя', callback_data='nb_kurs_1w_' + cur)
    nb_kurs_2w = InlineKeyboardButton(text='2 недели', callback_data='nb_kurs_2w_' + cur)
    nb_kurs_1m = InlineKeyboardButton(text='1 месяц', callback_data='nb_kurs_1m_' + cur)
    nb_kurs_3m = InlineKeyboardButton(text='3 месяца', callback_data='nb_kurs_3m_' + cur)
    nb_kurs_6m = InlineKeyboardButton(text='6 месяцев', callback_data='nb_kurs_6m_' + cur)
    nb_kurs_12m = InlineKeyboardButton(text='1 год', callback_data='nb_kurs_12m_' + cur)
    nb_kurs_nb_cur_back_all = InlineKeyboardButton(text='⬅️ Назад', callback_data='nb_kurs_nb_cur_back_all')

    markup.add(
        nb_kurs_1w,
        nb_kurs_2w,
        nb_kurs_1m,
        nb_kurs_3m,
        nb_kurs_6m,
        nb_kurs_12m,
        nb_kurs_nb_cur_back_all

    )

    return markup