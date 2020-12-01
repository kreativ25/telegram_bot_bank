import requests as rq
from requests.adapters import HTTPAdapter
import datetime as dt
import pymysql as pm
import echo.config as cf

# Блок подключения к БД MySQL
connection = pm.connect(host=cf.host,
                        user=cf.user,
                        password=cf.password,
                        db=cf.db)

# запрос к MySQL - максимальная дата
cur = connection.cursor()
cur.execute("select max(date) from curs_nb")
max_date_mysql = cur.fetchone()
connection.commit()

date_now = dt.datetime.now().date()

term = (date_now - max_date_mysql[0]).days



kurs_nb_list = {
    'usd': 145,
    'eur': 292,
    'rub': 298,
    'uah': 290,
    'pln': 293,

}

usd = {}
eur = {}
rub = {}
uah = {}
pln = {}


def curs_api(kod_cur, term, dict):
    date_start = (dt.datetime.date(dt.datetime.now()) - dt.timedelta(days=term)).__str__()
    date_end = dt.datetime.date(dt.datetime.now()).__str__()
    url = f'https://www.nbrb.by/api/exrates/rates/dynamics/{kod_cur}?startdate={date_start}&enddate={date_end}'

    # делаем стабильное подключение с реконектом = 10 раз
    adapter = HTTPAdapter(max_retries=10)
    with rq.Session() as session:
        session.mount(url, adapter)
        response = session.get(url)

    data = response.json()
    for i in range(len(data)):
        date = data[i]['Date'][:10]
        date = date.replace('-', '.')

        dict[i] = {
            'date': date,
            'value': data[i]['Cur_OfficialRate']
        }

    return dict


if max_date_mysql[0] != date_now:

    curs_api(kurs_nb_list['usd'], term, usd)
    curs_api(kurs_nb_list['eur'], term, eur)
    curs_api(kurs_nb_list['rub'], term, rub)
    curs_api(kurs_nb_list['uah'], term, uah)
    curs_api(kurs_nb_list['pln'], term, pln)

    if date_now != dt.datetime.strptime(usd[0]['date'], '%Y.%m.%d').date():

        for i in range(len(usd)):
            time_stamp = dt.datetime.now()

            if max_date_mysql[0] < dt.datetime.strptime(usd[i]['date'], '%Y.%m.%d').date():

                cur = connection.cursor()
                cur.execute("INSERT LOW_PRIORITY INTO curs_nb (date, usd, eur, rub, uah, pln, time_stamp) "
                            "VALUES (%s, %s, %s, %s, %s, %s, %s)",
                            (dt.datetime.strptime(usd[i]['date'], '%Y.%m.%d').date(),
                             usd[i]['value'],
                             eur[i]['value'],
                             rub[i]['value'],
                             uah[i]['value'],
                             pln[i]['value'],
                             time_stamp))
                connection.commit()
