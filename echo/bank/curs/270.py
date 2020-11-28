from requests import Session
from requests.adapters import HTTPAdapter
import datetime as dt
import pymysql as pm
import echo.config as cf

import xml.etree.ElementTree as etree

url = f'https://www.alfabank.by/personal/currency/'

# делаем стабильное подключение с реконектом = 10 раз
adapter = HTTPAdapter(max_retries=10)
with Session() as session:
    session.mount(url, adapter)
    response = session.get(url)

data_curs = response.text
tree = etree.ElementTree(etree.fromstring(data_curs))

data = []
data_all = {}
root = tree.iter('rates')

for i in root:
    for x in i.findall(".//exch_rate_record/..[@name='Курсы валют']"):
        for y in x.findall('exch_rate_record'):
            data.append(y.attrib)

for i in data:
    if i['mnem'] == 'USD':
        data_all[0] = {
            'usd_in': i['rate_buy'],
            'usd_out': i['rate_sell']
        }
    if i['mnem'] == 'EUR':
        data_all[1] = {
            'eur_in': i['rate_buy'],
            'eur_out': i['rate_sell']
        }

    if i['mnem'] == 'RUB':
        data_all[2] = {
            'rub_in': i['rate_buy'],
            'rub_out': i['rate_sell']
        }

date = dt.datetime.date(dt.datetime.now()).__str__()
bank_id = 270
bank_name = 'Альфа-Банк'
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
curs.execute('delete LOW_PRIORITY from curs where bank_id = 270')
curs.execute(
    "INSERT LOW_PRIORITY INTO curs (date, bank_id, bank_name, usd_in, usd_out, eur_in, eur_out, rub_in, rub_out, time_stamp)"
    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
    (date, bank_id, bank_name, usd_in, usd_out, eur_in, eur_out, rub_in, rub_out, time_stamp))
connection.commit()
