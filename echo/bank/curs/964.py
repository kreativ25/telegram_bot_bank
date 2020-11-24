from requests import Session
from requests.adapters import HTTPAdapter
import datetime as dt
import pymysql as pm
import echo.config as cf

import xml.etree.ElementTree as etree

url = f'https://belapb.by/CashExRatesDaily.php'

# делаем стабильное подключение с реконектом = 10 раз
adapter = HTTPAdapter(max_retries=10)
with Session() as session:
    session.mount(url, adapter)
    response = session.get(url)

data_curs = response.text
tree = etree.ElementTree(etree.fromstring(data_curs))

data_all = {}
root = tree.iter('Currency')

for i in root:
    len_num = 6
    if i.find('NumCode').text == '840':
        if len(data_all) < len_num:
            data_all[0] = {'usd_in': i.find('RateBuy').text}
            data_all[1] = {'usd_out': i.find('RateSell').text}

    if i.find('NumCode').text == '978':
        if len(data_all) < len_num:
            data_all[2] = {'eur_in': i.find('RateBuy').text}
            data_all[3] = {'eur_out': i.find('RateSell').text}

    if i.find('NumCode').text == '643':
        if len(data_all) < len_num:
            data_all[4] = {'rub_in': i.find('RateBuy').text}
            data_all[5] = {'rub_out': i.find('RateSell').text}


date = dt.datetime.date(dt.datetime.now()).__str__()
bank_id = 964
bank_name = 'Белагропромбанк'
usd_in = float(data_all[0]['usd_in'])
usd_in = float('{:.4f}'.format(usd_in))

usd_out = float(data_all[1]['usd_out'])
usd_out = float('{:.4f}'.format(usd_out))


eur_in = float(data_all[2]['eur_in'])
eur_in = float('{:.4f}'.format(eur_in))

eur_out = float(data_all[3]['eur_out'])
eur_out = float('{:.4f}'.format(eur_out))


rub_in = float(data_all[4]['rub_in'])
rub_in = float('{:.4f}'.format(rub_in))


rub_out = float(data_all[5]['rub_out'])
rub_out = float('{:.4f}'.format(rub_out))
time_stamp = dt.datetime.now()

# Блок подключения к БД MySQL
connection = pm.connect(host=cf.host,
                        user=cf.user,
                        password=cf.password,
                        db=cf.db)

# запись данных в MySQL
curs = connection.cursor()
curs.execute('delete from curs where bank_id = 964')
curs.execute(
    "INSERT INTO curs (date, bank_id, bank_name, usd_in, usd_out, eur_in, eur_out, rub_in, rub_out, time_stamp)"
    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
    (date, bank_id, bank_name, usd_in, usd_out, eur_in, eur_out, rub_in, rub_out, time_stamp))
connection.commit()
