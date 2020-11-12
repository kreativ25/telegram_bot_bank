from requests import Session
from requests.adapters import HTTPAdapter
import unicodedata
import re
import datetime as dt
import pymysql as pm
import echo.config as cf
from bs4 import BeautifulSoup

date_satrt = dt.date(2019, 10, 1)

date = dt.datetime.now().date()
date_yesterday = dt.datetime.now().date() - dt.timedelta(days=1)

print(date)

# Блок подключения к БД MySQL
connection = pm.connect(host=cf.host,
                        user=cf.user,
                        password=cf.password,
                        db=cf.db)

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

# запись спарсеных данных в MySQL
# mbk_pars = connection.cursor()
# mbk_pars.execute(
#     "INSERT INTO mbk (date, mbk_sum, mbk_stavka, time_stamp)"
#     " VALUES (%s, %s, %s, %s)",
#     (data_mbk['date'], data_mbk['mbk_sum'], data_mbk['mbk_stavka'], time_stamp))
# connection.commit()
#
# print('Новые данные МБК записаны в MySQL')


# обновление последней даты записи time_stamp
# mbk_up_date = connection.cursor()
# mbk_up_date.execute(
#     "UPDATE mbk SET time_stamp = %s  order by date(date) desc limit 1",
#     time_stamp)
# connection.commit()
#
# print('time_stamp максимальной даты МБК обновлен!')




# расчет времени последнего подключения к сайту
# mbk_max_ts = connection.cursor()
# mbk_max_ts.execute(
#     "select max(time_stamp) as max_ts from mbk")
# mbk_max_ts = mbk_max_ts.fetchone()
# connection.commit()
#
# print('максимальная ts БД: ', mbk_max_ts[0])
#
# diff = time_stamp - mbk_max_ts[0]
# delta_hours = int(diff.seconds // (60*60))
# delta_mins = int((diff.seconds // 60) % 60)


# запрос к MySQL - максимальная дата
# mbk_max_date = connection.cursor()
# mbk_max_date.execute("select max(date) from mbk")
# max_date_mbk_bd = mbk_max_date.fetchone()
# connection.commit()
#
# print(max_date_mbk_bd[0])





# ==========================================================================
# блок пополнения БД
date_satrt = dt.date(2019, 10, 15)
date_satrt = date_satrt + dt.timedelta(days=1)

