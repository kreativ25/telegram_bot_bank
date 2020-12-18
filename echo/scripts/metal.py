from requests import Session
from requests.adapters import HTTPAdapter
import datetime as dt
import pymysql as pm
import echo.config as cf


try:
    connection = pm.connect(host=cf.host,
                            user=cf.user,
                            password=cf.password,
                            db=cf.db)

    # запрос к MySQL - максимальная дата
    max_date = connection.cursor()
    max_date.execute("select max(date) from metal")
    max_date_bd_prepare = max_date.fetchone()
    connection.commit()

finally:
    connection.close()


date = dt.datetime.now().date()
delta = (date - max_date_bd_prepare[0]).days

if date != max_date_bd_prepare[0]:

    date_start = (dt.datetime.date(dt.datetime.now()) - dt.timedelta(days=delta)).__str__()
    date_end = dt.datetime.date(dt.datetime.now()).__str__()
    url = f'https://www.nbrb.by/api/bankingots/prices/?startdate={date_start}&enddate={date_end}'

    adapter = HTTPAdapter(max_retries=10)
    with Session() as session:
        session.mount(url, adapter)
        response = session.get(url)

    price_metal_all = response.json()


    def metal_dict(dict, cod):
        x = -1
        for i in range(len(price_metal_all)):
            if price_metal_all[i]['MetalId'] == cod:
                x = x + 1
                dict[x] = {
                    'date': price_metal_all[i]['Date'],
                    'value': price_metal_all[i]['Value']
                }
        return dict


    gold = {}
    silver = {}
    platinum = {}
    palladium = {}

    gold = metal_dict(gold, 0)
    silver = metal_dict(silver, 1)
    platinum = metal_dict(platinum, 2)
    palladium = metal_dict(palladium, 3)
    time_stamp = dt.datetime.now()

    for i in range(len(gold)):
        _i = i + 1
        data_record = max_date_bd_prepare[0] + dt.timedelta(days=_i)

        try:
            connection = pm.connect(host=cf.host,
                                    user=cf.user,
                                    password=cf.password,
                                    db=cf.db)

            # запрос к MySQL - максимальная дата
            max_date = connection.cursor()
            max_date.execute("select max(date) from metal")
            max_date_bd = max_date.fetchone()
            connection.commit()

        finally:
            connection.close()

        data_record_ = gold[i]['date'][:10].replace('-', '.')
        data_record_ = dt.datetime.strptime(data_record_, '%Y.%m.%d').date()

        if data_record_ != max_date_bd[0]:

            try:
                connection = pm.connect(host=cf.host,
                                        user=cf.user,
                                        password=cf.password,
                                        db=cf.db)

                metal_con = connection.cursor()
                metal_con.execute(
                    "INSERT LOW_PRIORITY INTO metal (date, gold, silver, platinum, palladium, time_stamp)"
                    " VALUES (%s, %s, %s, %s, %s, %s)",
                    (gold[i]['date'],
                     gold[i]['value'],
                     silver[i]['value'],
                     platinum[i]['value'],
                     palladium[i]['value'],
                     time_stamp))
                connection.commit()

            finally:
                connection.close()
