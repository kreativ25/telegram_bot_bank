from requests.adapters import HTTPAdapter
import datetime as dt
import requests as rq
import pymysql as pm
import echo.config as cf

# получаем текущую ставку реф
data = dt.datetime.date(dt.datetime.now()).__str__()
params = {'ondate': data}

# получаем максимальную дату api
url = 'https://www.nbrb.by/api/refinancingrate'
adapter = HTTPAdapter(max_retries=10)
with rq.Session() as session:
    session.mount(url, adapter)
    sr_new = session.get(url, params=params)
date_api = dt.datetime.strptime(sr_new.json()[0]['Date'][:-9].replace('-', '.'), '%Y.%m.%d').date()

# получаем максимальную дату БД
try:
    connection = pm.connect(host=cf.host,
                            user=cf.user,
                            password=cf.password,
                            db=cf.db)

    cur = connection.cursor()
    cur.execute("select max(date) from sr_all")
    date_bd = cur.fetchone()
    connection.commit()

finally:
    connection.close()


if date_api != date_bd[0] or date_bd is None:

    # формируем полный список данных
    url = 'https://www.nbrb.by/api/refinancingrate'
    adapter = HTTPAdapter(max_retries=10)
    with rq.Session() as session:
        session.mount(url, adapter)
        response = session.get(url)
    sr_all = response.json()

    sr_all_result = {}
    for i in range(len(sr_all)):
        sr_all_result[i] = {
            'date': sr_all[i]['Date'],
            'value': sr_all[i]['Value']
        }

    # очищаем таблицу
    try:
        connection = pm.connect(host=cf.host,
                                user=cf.user,
                                password=cf.password,
                                db=cf.db)

        sr = connection.cursor()
        sr.execute('truncate table sr_all')
        connection.commit()

    finally:
        connection.close()

    for i in range(len(sr_all_result)):
        time_stamp = dt.datetime.now()

        try:
            connection = pm.connect(host=cf.host,
                                    user=cf.user,
                                    password=cf.password,
                                    db=cf.db)

            sr = connection.cursor()
            sr.execute(
                "INSERT HIGH_PRIORITY INTO sr_all (date, sr, time_stamp)"
                " VALUES (%s, %s, %s)",
                (sr_all_result[i]['date'], sr_all_result[i]['value'], time_stamp))
            connection.commit()

        finally:
            connection.close()
