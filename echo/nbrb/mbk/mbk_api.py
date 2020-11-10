from requests import Session
from requests.adapters import HTTPAdapter
import unicodedata
import re
import datetime as dt
import pymysql as pm
import echo.config as cf
from bs4 import BeautifulSoup


date_satrt = dt.date(2019, 10, 1)
# date_satrt = date_satrt + + dt.timedelta(days=1)


# Блок подключения к БД MySQL
connection = pm.connect(host=cf.host,
                        user=cf.user,
                        password=cf.password,
                        db=cf.db)

# запрос к MySQL - максимальная дата
# mbk = connection.cursor()
# mbk.execute("select max(date) from mbk")
# max_date_mbk_bd = mbk.fetchone()
# connection.commit()


# проверяем время последнего обновления информации
# time_bd = connection.cursor()
# time_bd.execute('select max(ts) as max_ts from stavki_nb_oper')
# max_ts_mbk = time_bd.fetchone()


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
                            data={'date': str(date_satrt)},
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
        return '0'+x
    else:
        return x

# выбираем правильную дату данных из скрипта
date_prepare = soop.find('script', text=re.compile('setDate')).extract()
date_prepare = str(date_prepare).split()
date_prepare_ = []
date_prepare_.append(date_prepare)

yy = date_prepare_[0][11][6:-2]
dd = date_len(date_prepare_[0][13][1:-4])
mm = date_len(date_prepare_[0][12][10:-5])

date = yy + '.' + mm + '.' + dd
date = dt.datetime.strptime(date, '%Y.%m.%d').date()

time_stamp = dt.datetime.now()
data_mbk = {
    'date': date,
    'mbk_sum': mbk_sum,
    'mbk_stavka': mbk_stavka
}


mbk = connection.cursor()
mbk.execute(
    "INSERT INTO mbk (date, mbk_sum, mbk_stavka, time_stamp)"
    " VALUES (%s, %s, %s, %s)",
    (data_mbk['date'], data_mbk['mbk_sum'], data_mbk['mbk_stavka'], time_stamp))
connection.commit()

print('записано')