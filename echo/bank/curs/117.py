from requests import Session
from requests.adapters import HTTPAdapter
import datetime as dt
import pymysql as pm
import echo.config as cf

import xml.etree.ElementTree as etree

url = f'https://www.mtbank.by/currxml.php?ver=2'

# делаем стабильное подключение с реконектом = 10 раз
adapter = HTTPAdapter(max_retries=10)
with Session() as session:
    session.mount(url, adapter)
    response = session.get(url)

data_curs = response.text
tree = etree.ElementTree(etree.fromstring(data_curs))

data_all = {}
root = tree.iter('currency')

x = -1

for i in root:
    x = x + 1
    if x < 5:
        data_all[x] = {
            'code': i.find('code').text,
            'purchase': i.find('purchase').text,
            'sale': i.find('sale').text
        }
    else:
        break

date = dt.datetime.date(dt.datetime.now()).__str__()
bank_id = 117
bank_name = 'МТБанк'
usd_in = float(data_all[1]['purchase'])
usd_in = float('{:.4f}'.format(usd_in))

usd_out = float(data_all[1]['sale'])
usd_out = float('{:.4f}'.format(usd_out))


eur_in = float(data_all[4]['purchase'])
eur_in = float('{:.4f}'.format(eur_in))

eur_out = float(data_all[4]['sale'])
eur_out = float('{:.4f}'.format(eur_out))


rub_in = float(data_all[0]['purchase'])
rub_in = float('{:.4f}'.format(rub_in))


rub_out = float(data_all[0]['sale'])
rub_out = float('{:.4f}'.format(rub_out))
time_stamp = dt.datetime.now()

try:
    # Блок подключения к БД MySQL
    connection = pm.connect(host=cf.host,
                            user=cf.user,
                            password=cf.password,
                            db=cf.db)

    # запись данных в MySQL
    curs = connection.cursor()
    curs.execute('delete LOW_PRIORITY from curs where bank_id = 117')
    curs.execute(
        "INSERT LOW_PRIORITY INTO curs (date, bank_id, bank_name, usd_in, usd_out, eur_in, eur_out, rub_in, rub_out, time_stamp)"
        " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (date, bank_id, bank_name, usd_in, usd_out, eur_in, eur_out, rub_in, rub_out, time_stamp))
    connection.commit()
finally:
    connection.close()