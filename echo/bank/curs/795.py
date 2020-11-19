from requests import Session
from requests.adapters import HTTPAdapter
import datetime as dt
import pymysql as pm
import echo.config as cf

city = 'Минск'
url = f'https://belarusbank.by/api/kursExchange?city={city}'

# делаем стабильное подключение с реконектом = 10 раз
adapter = HTTPAdapter(max_retries=10)
with Session() as session:
    session.mount(url, adapter)
    response = session.get(url)

data_curs = response.json()

date = dt.datetime.date(dt.datetime.now()).__str__()
bank_id = 795
bank_name = 'Беларусбанк'
usd_in = data_curs[1]['USD_in']
usd_out = data_curs[1]['USD_out']
eur_in = data_curs[1]['EUR_in']
eur_out = data_curs[1]['EUR_out']
rub_in = data_curs[1]['RUB_in']
rub_out = data_curs[1]['RUB_out']
time_stamp = dt.datetime.now()

# Блок подключения к БД MySQL
connection = pm.connect(host=cf.host,
                        user=cf.user,
                        password=cf.password,
                        db=cf.db)

# запись данных в MySQL
curs = connection.cursor()
curs.execute('delete from curs where bank_id = 795')
curs.execute(
    "INSERT INTO curs (date, bank_id, bank_name, usd_in, usd_out, eur_in, eur_out, rub_in, rub_out, time_stamp)"
    " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
    (date, bank_id, bank_name, usd_in, usd_out, eur_in, eur_out, rub_in, rub_out, time_stamp))
connection.commit()


# # обновление данных
# mbk_up_date = connection.cursor()
# mbk_up_date.execute(
#     "UPDATE curs SET date = %s, bank_id = %s, bank_name = %s, usd_in = %s, usd_out = %s, eur_in = %s, eur_out = %s, rub_in = %s, rub_out = %s, time_stamp = %s",
#     date, bank_id, bank_name, usd_in, usd_out, eur_in, eur_out, rub_in, rub_out, time_stamp)
# connection.commit()


# "UPDATE mbk SET time_stamp = %s  order by date(date) desc limit 1",