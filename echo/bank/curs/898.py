from requests import Session
from requests.adapters import HTTPAdapter
import datetime as dt
import pymysql as pm
import echo.config as cf

import xml.etree.ElementTree as etree

url = f'https://absolutbank.by/exchange-rates.xml'

# делаем стабильное подключение с реконектом = 10 раз
adapter = HTTPAdapter(max_retries=10)
with Session() as session:
    session.mount(url, adapter)
    response = session.get(url)

data_curs = response.text
tree = etree.ElementTree(etree.fromstring(data_curs))

data_eur_buy = {}
data_eur_sell = {}
data_usd_buy = {}
data_usd_sell = {}
data_rub_buy = {}
data_rub_sell = {}
root = tree.iter('branches')

a = -1
b = -1
c = -1
f = -1
h = -1
j = -1

for i in root:
    for x in i.findall(".//buy/..[@currency='eur']"):
            for z in x.findall('buy'):
                a = a + 1
                data_eur_buy[a] = {'eur_buy': z.text}
    for q in i.findall(".//sell/..[@currency='eur']"):
            for d in q.findall('sell'):
                b = b + 1
                data_eur_sell[b] = {'eur_sell': d.text}
    for w in i.findall(".//buy/..[@currency='usd']"):
            for e in w.findall('buy'):
                c = c + 1
                data_usd_buy[c] = {'usd_buy': e.text}
    for q in i.findall(".//sell/..[@currency='usd']"):
            for d in q.findall('sell'):
                f = f + 1
                data_usd_sell[f] = {'usd_sell': d.text}
    for y in i.findall(".//buy/..[@currency='rub']"):
            for u in y.findall('buy'):
                h = h + 1
                data_rub_buy[h] = {'rub_buy': u.text}
    for p in i.findall(".//sell/..[@currency='rub']"):
            for l in p.findall('sell'):
                j = j + 1
                data_rub_sell[j] = {'rub_sell': l.text}


date = dt.datetime.date(dt.datetime.now()).__str__()
bank_id = 898
bank_name = 'Абсолютбанк'
usd_in = float(data_usd_buy[0]['usd_buy'])
usd_in = float('{:.4f}'.format(usd_in))

usd_out = float(data_usd_sell[0]['usd_sell'])
usd_out = float('{:.4f}'.format(usd_out))


eur_in = float(data_eur_buy[0]['eur_buy'])
eur_in = float('{:.4f}'.format(eur_in))

eur_out = float(data_eur_sell[0]['eur_sell'])
eur_out = float('{:.4f}'.format(eur_out))


rub_in = float(data_rub_buy[0]['rub_buy'])
rub_in = float('{:.4f}'.format(rub_in))


rub_out = float(data_rub_sell[0]['rub_sell'])
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
    curs.execute('delete LOW_PRIORITY from curs where bank_id = 898')
    curs.execute(
        "INSERT LOW_PRIORITY INTO curs (date, bank_id, bank_name, usd_in, usd_out, eur_in, eur_out, rub_in, rub_out, time_stamp)"
        " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (date, bank_id, bank_name, usd_in, usd_out, eur_in, eur_out, rub_in, rub_out, time_stamp))
    connection.commit()
finally:
    connection.close()
