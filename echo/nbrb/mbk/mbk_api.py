from requests import Session
from requests.adapters import HTTPAdapter
import unicodedata
import re
import datetime as dt
import pymysql as pm
import echo.config as cf

from bs4 import BeautifulSoup

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
                            data={'date': '06.11.2020'},
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



