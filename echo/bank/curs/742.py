from requests import Session
from requests.adapters import HTTPAdapter
import datetime as dt
import pymysql as pm
import echo.config as cf

import xml.etree.ElementTree as etree

url = f'https://belgazprombank.by/upload/courses.xml'

# делаем стабильное подключение с реконектом = 10 раз
adapter = HTTPAdapter(max_retries=10)
with Session() as session:
    session.mount(url, adapter)
    response = session.get(url)

data_curs = response.text
tree = etree.ElementTree(etree.fromstring(data_curs))

data_all = {}
root = tree.iter('branch')

for i in root:
    for x in i.findall(".//range/..[@currency='usd']"):
        for z in x.findall(".//buy/..[@min-amount='0']"):
            data_all[0] = {'usd_in': z.find('buy').text}

    for q in i.findall(".//range/..[@currency='usd']"):
        for w in q.findall(".//sell/..[@min-amount='0']"):
            data_all[1] = {'usd_out': w.find('sell').text}

    for x in i.findall(".//range/..[@currency='eur']"):
        for z in x.findall(".//buy/..[@min-amount='0']"):
            data_all[2] = {'eur_in': z.find('buy').text}

    for q in i.findall(".//range/..[@currency='eur']"):
        for w in q.findall(".//sell/..[@min-amount='0']"):
            data_all[3] = {'eur_out': w.find('sell').text}

    for x in i.findall(".//range/..[@currency='rub']"):
        for z in x.findall(".//buy/..[@min-amount='0']"):
            data_all[4] = {'rub_in': z.find('buy').text}

    for q in i.findall(".//range/..[@currency='rub']"):
        for w in q.findall(".//sell/..[@min-amount='0']"):
            data_all[5] = {'rub_out': w.find('sell').text}


date = dt.datetime.date(dt.datetime.now()).__str__()
bank_id = 742
bank_name = 'Белгазпромбанк'
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

try:
    # Блок подключения к БД MySQL
    connection = pm.connect(host=cf.host,
                            user=cf.user,
                            password=cf.password,
                            db=cf.db)

    # запись данных в MySQL
    curs = connection.cursor()
    curs.execute('delete LOW_PRIORITY from curs where bank_id = 742')
    curs.execute(
        "INSERT LOW_PRIORITY INTO curs (date, bank_id, bank_name, usd_in, usd_out, eur_in, eur_out, rub_in, rub_out, time_stamp)"
        " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (date, bank_id, bank_name, usd_in, usd_out, eur_in, eur_out, rub_in, rub_out, time_stamp))
    connection.commit()
finally:
    connection.close()
