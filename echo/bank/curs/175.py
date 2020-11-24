from requests import Session
from requests.adapters import HTTPAdapter
import datetime as dt
import pymysql as pm
import echo.config as cf

import xml.etree.ElementTree as etree

url = f'https://www.bsb.by/xml.php?service=4&trader=7&charset=UTF-8'

# делаем стабильное подключение с реконектом = 10 раз
adapter = HTTPAdapter(max_retries=10)
with Session() as session:
    session.mount(url, adapter)
    response = session.get(url)

data_curs = response.text
tree = etree.ElementTree(etree.fromstring(data_curs))

data = []
data_all_prepare = {}
data_all = {}
root = tree.iter('item')

t = -1

for i in root:
    t = t + 1
    data_all_prepare[t] = {
        'name': i.find('buy_good_name').text,
        'in': i.find('buy_amount').text,
        'out': i.find('sell_amount').text
    }

# print(data_all_prepare)

for i in range(len(data_all_prepare))[:3]:
    if data_all_prepare[i]['name'] == 'USD':
        data_all[0] = {
            'usd_in': data_all_prepare[i]['in'],
            'usd_out': data_all_prepare[i]['out']
        }
    if data_all_prepare[i]['name'] == 'EUR':
        data_all[1] = {
            'eur_in': data_all_prepare[i]['in'],
            'eur_out': data_all_prepare[i]['out']
        }
    if data_all_prepare[i]['name'] == 'RUB':
        data_all[2] = {
            'rub_in': float(data_all_prepare[i]['in'])*100,
            'rub_out': float(data_all_prepare[i]['out'])*100
        }

# print(data_all)


date = dt.datetime.date(dt.datetime.now()).__str__()
bank_id = 175
bank_name = 'БСБ Банк'
usd_in = float(data_all[0]['usd_in'])
usd_in = float('{:.4f}'.format(usd_in))

usd_out = float(data_all[0]['usd_out'])
usd_out = float('{:.4f}'.format(usd_out))


eur_in = float(data_all[1]['eur_in'])
eur_in = float('{:.4f}'.format(eur_in))

eur_out = float(data_all[1]['eur_out'])
eur_out = float('{:.4f}'.format(eur_out))


rub_in = float(data_all[2]['rub_in'])
rub_in = float('{:.4f}'.format(rub_in))


rub_out = float(data_all[2]['rub_out'])
rub_out = float('{:.4f}'.format(rub_out))
time_stamp = dt.datetime.now()

# Блок подключения к БД MySQL
connection = pm.connect(host=cf.host,
                        user=cf.user,
                        password=cf.password,
                        db=cf.db)

# запись данных в MySQL
curs = connection.cursor()
curs.execute('delete from curs where bank_id = 175')
curs.execute(
    "INSERT INTO curs (date, bank_id, bank_name, usd_in, usd_out, eur_in, eur_out, rub_in, rub_out, time_stamp)"
    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
    (date, bank_id, bank_name, usd_in, usd_out, eur_in, eur_out, rub_in, rub_out, time_stamp))
connection.commit()
