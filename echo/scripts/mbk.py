from requests import Session
from requests.adapters import HTTPAdapter
import unicodedata
import re
import datetime as dt
import pymysql as pm
import echo.config as cf
from bs4 import BeautifulSoup

date = dt.datetime.now().date()
date_yesterday = dt.datetime.now().date() - dt.timedelta(days=1)
time_stamp = dt.datetime.now()

data_mbk = {}
mbk_all = {}

# Блок подключения к БД MySQL
connection = pm.connect(host=cf.host,
                        user=cf.user,
                        password=cf.password,
                        db=cf.db)

# запрос к MySQL - максимальная дата
max_date = connection.cursor()
max_date.execute("select max(date) from mbk")
max_date_bd_prepare = max_date.fetchone()
connection.commit()

delta = (date_yesterday - max_date_bd_prepare[0]).days


def con_site(date_r):
    url = 'https://www.nbrb.by/statistics/financialmarkets/interbankrates'

    headers = {
        'Accept': 'text/html, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    }

    adapter = HTTPAdapter(max_retries=7)
    with Session() as session:
        session.mount(url, adapter)
        response = session.post(url,
                                data={'date': str(date_r)},
                                headers=headers
                                )

    soop = BeautifulSoup(response.text.encode('utf8'), 'lxml')

    mbk_sum_prepare = soop.find('td', text=re.compile('1 день')).next.next.next.text
    mbk_sum = float(unicodedata.normalize("NFKD", mbk_sum_prepare).replace(' ', '').replace(',', '.'))

    mbk_stavka_prepare = soop.find('td', text=re.compile('1 день')).next.next.next.next.next.next.next.text
    mbk_stavka = float(unicodedata.normalize("NFKD", mbk_stavka_prepare).replace(' ', '').replace(',', '.'))

    # функция добавления нуля для даты
    def date_len(x):
        if len(x) == 1:
            return '0' + x
        else:
            return x

    # выбираем правильную дату данных из скрипта сайта НБ
    date_prepare = soop.find('script', text=re.compile('setDate')).extract()
    date_prepare = str(date_prepare).split()
    date_prepare_ = [date_prepare]

    yy = date_prepare_[0][11][6:-2]
    dd = date_len(date_prepare_[0][13][1:-4])
    mm = date_len(date_prepare_[0][12][10:-5])

    date = yy + '.' + mm + '.' + dd
    date = dt.datetime.strptime(date, '%Y.%m.%d').date()

    data_mbk = {
        'date': date,
        'mbk_sum': mbk_sum,
        'mbk_stavka': mbk_stavka
    }

    return data_mbk


if date_yesterday != max_date_bd_prepare[0]:

    for i in range(delta):
        _i = i + 1
        data_record = max_date_bd_prepare[0] + dt.timedelta(days=_i)

        # запрос к MySQL - максимальная дата
        max_date = connection.cursor()
        max_date.execute("select max(date) from mbk")
        max_date_bd = max_date.fetchone()
        connection.commit()

        data_record_ = dt.datetime.strftime(con_site(data_record)['date'], '%Y.%m.%d')
        max_date_bd_ = dt.datetime.strftime(max_date_bd[0], '%Y.%m.%d')

        get_data_mbk = con_site(data_record)

        if data_record_ != max_date_bd_:
            # запись спарсеных данных в MySQL
            mbk_pars = connection.cursor()
            mbk_pars.execute(
                "INSERT LOW_PRIORITY INTO mbk (date, mbk_sum, mbk_stavka, time_stamp)"
                " VALUES (%s, %s, %s, %s)",
                (get_data_mbk['date'], get_data_mbk['mbk_sum'], get_data_mbk['mbk_stavka'], time_stamp))
            connection.commit()
