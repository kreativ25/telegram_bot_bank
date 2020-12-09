from requests.adapters import HTTPAdapter
import datetime as dt
import requests as rq
import pymysql as pm
import echo.config as cf

data = dt.datetime.date(dt.datetime.now()).__str__()
params = {'ondate': data}

url = 'https://www.nbrb.by/api/refinancingrate'
adapter = HTTPAdapter(max_retries=10)
with rq.Session() as session:
    session.mount(url, adapter)
    response = session.get(url, params=params)

sr_value = response.json()
sr_value = sr_value[0]['Value']
time_stamp = dt.datetime.now()

if sr_value is not None:
    connection = pm.connect(host=cf.host,
                            user=cf.user,
                            password=cf.password,
                            db=cf.db)

    sr = connection.cursor()
    sr.execute('truncate table sr_one')
    sr.execute(
        "INSERT HIGH_PRIORITY INTO sr_one (date, sr, time_stamp)"
        " VALUES (%s, %s, %s)",
        (data, sr_value, time_stamp))
    connection.commit()
