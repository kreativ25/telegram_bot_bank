from requests import Session
from requests.adapters import HTTPAdapter
import datetime as dt
import pymysql as pm
import echo.config as cf

import xml.etree.ElementTree as etree

url = f'https://bankdabrabyt.by/export_courses.php'

# делаем стабильное подключение с реконектом = 10 раз
adapter = HTTPAdapter(max_retries=10)
with Session() as session:
    session.mount(url, adapter)
    response = session.get(url)

data_curs = response.text
tree = etree.ElementTree(etree.fromstring(data_curs))

data_curs = response.text
tree = etree.ElementTree(etree.fromstring(data_curs))

data_all = []
root = tree.iter()
for i in root:
    if len(i.attrib) > 0:
        data_all.append(i.attrib)


date = dt.datetime.date(dt.datetime.now()).__str__()
bank_id = 272
bank_name = 'Банк Дабрабыт'
usd_in = float(data_all[1]['buy'])
usd_in = float('{:.4f}'.format(usd_in))

usd_out = float(data_all[1]['sale'])
usd_out = float('{:.4f}'.format(usd_out))


eur_in = float(data_all[2]['buy'])
eur_in = float('{:.4f}'.format(eur_in))

eur_out = float(data_all[2]['sale'])
eur_out = float('{:.4f}'.format(eur_out))


rub_in = float(data_all[3]['buy'])*100
rub_in = float('{:.4f}'.format(rub_in))


rub_out = float(data_all[3]['sale'])*100
rub_out = float('{:.4f}'.format(rub_out))
time_stamp = dt.datetime.now()


# Блок подключения к БД MySQL
connection = pm.connect(host=cf.host,
                        user=cf.user,
                        password=cf.password,
                        db=cf.db)

# запись данных в MySQL
curs = connection.cursor()
curs.execute('delete from curs where bank_id = 272')
curs.execute(
    "INSERT INTO curs (date, bank_id, bank_name, usd_in, usd_out, eur_in, eur_out, rub_in, rub_out, time_stamp)"
    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
    (date, bank_id, bank_name, usd_in, usd_out, eur_in, eur_out, rub_in, rub_out, time_stamp))
connection.commit()
