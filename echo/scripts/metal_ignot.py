from requests import Session
from requests.adapters import HTTPAdapter
import datetime as dt
import pymysql as pm
import echo.config as cf

date = dt.datetime.date(dt.datetime.now()).__str__()
time_stamp = dt.datetime.now()


def get_metal_ignot(kod_metal, date):

    url = f'https://www.nbrb.by/api/ingots/prices/{kod_metal}?ondate={date}'
    adapter = HTTPAdapter(max_retries=10)
    with Session() as session:
        session.mount(url, adapter)
        response = session.get(url)

    metal_data = response.json()
    return metal_data


# золото
data_gold = get_metal_ignot(0, date)

try:
    connection = pm.connect(host=cf.host,
                            user=cf.user,
                            password=cf.password,
                            db=cf.db)

    metal_con = connection.cursor()
    metal_con.execute('truncate table gold_ignot')
    metal_con.execute(
        "INSERT LOW_PRIORITY INTO gold_ignot (date, nominal_1_in, nominal_1_out, nominal_5_in, nominal_5_out, "
        "nominal_10_in, nominal_10_out, nominal_20_in, nominal_20_out, nominal_50_in, nominal_50_out, "
        "nominal_100_in, nominal_100_out, nominal_250_in, nominal_250_out, nominal_500_in, nominal_500_out, "
        "nominal_1000_in, nominal_1000_out, time_stamp)"
        " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (data_gold[0]['Date'],
         data_gold[0]['CertificateRubles'],
         data_gold[0]['EntitiesRubles'],
         data_gold[1]['CertificateRubles'],  #5
         data_gold[1]['EntitiesRubles'],

         data_gold[2]['CertificateRubles'],  # 10
         data_gold[2]['EntitiesRubles'],

         data_gold[3]['CertificateRubles'],  # 20
         data_gold[3]['EntitiesRubles'],

         data_gold[4]['CertificateRubles'],  # 50
         data_gold[4]['EntitiesRubles'],

         data_gold[5]['CertificateRubles'],  # 100
         data_gold[5]['EntitiesRubles'],

         data_gold[6]['CertificateRubles'],  # 250
         data_gold[6]['EntitiesRubles'],

         data_gold[7]['CertificateRubles'],  # 500
         data_gold[7]['EntitiesRubles'],

         data_gold[8]['CertificateRubles'],  # 100
         data_gold[8]['EntitiesRubles'],

         time_stamp))
    connection.commit()

finally:
    connection.close()


# серебро
data_silver = get_metal_ignot(1, date)

try:
    connection = pm.connect(host=cf.host,
                            user=cf.user,
                            password=cf.password,
                            db=cf.db)

    metal_con = connection.cursor()
    metal_con.execute('truncate table silver_ignot')
    metal_con.execute(
        "INSERT LOW_PRIORITY INTO silver_ignot (date,"
        "nominal_10_in, nominal_10_out, nominal_20_in, nominal_20_out, nominal_50_in, nominal_50_out, "
        "nominal_100_in, nominal_100_out, nominal_250_in, nominal_250_out, nominal_500_in, nominal_500_out, "
        "nominal_1000_in, nominal_1000_out, time_stamp)"
        " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (data_silver[0]['Date'],

         data_silver[0]['CertificateRubles'],  # 10
         data_silver[0]['EntitiesRubles'],

         data_silver[1]['CertificateRubles'],  # 20
         data_silver[1]['EntitiesRubles'],

         data_silver[2]['CertificateRubles'],  # 50
         data_silver[2]['EntitiesRubles'],

         data_silver[3]['CertificateRubles'],  # 100
         data_silver[3]['EntitiesRubles'],

         data_silver[4]['CertificateRubles'],  # 250
         data_silver[4]['EntitiesRubles'],

         data_silver[5]['CertificateRubles'],  # 500
         data_silver[5]['EntitiesRubles'],

         data_silver[6]['CertificateRubles'],  # 100
         data_silver[6]['EntitiesRubles'],

         time_stamp))
    connection.commit()

finally:
    connection.close()


# платина
data_platinum = get_metal_ignot(2, date)

try:
    connection = pm.connect(host=cf.host,
                            user=cf.user,
                            password=cf.password,
                            db=cf.db)

    metal_con = connection.cursor()
    metal_con.execute('truncate table platinum_ignot')
    metal_con.execute(
        "INSERT LOW_PRIORITY INTO platinum_ignot (date, nominal_1_in, nominal_1_out, nominal_5_in, nominal_5_out, "
        "nominal_10_in, nominal_10_out, nominal_20_in, nominal_20_out, nominal_50_in, nominal_50_out, "
        "nominal_100_in, nominal_100_out, nominal_250_in, nominal_250_out, nominal_500_in, nominal_500_out, "
        "time_stamp)"
        " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
        (data_platinum[0]['Date'],
         data_platinum[0]['CertificateRubles'],
         data_platinum[0]['EntitiesRubles'],
         data_platinum[1]['CertificateRubles'],  #5
         data_platinum[1]['EntitiesRubles'],

         data_platinum[2]['CertificateRubles'],  # 10
         data_platinum[2]['EntitiesRubles'],

         data_platinum[3]['CertificateRubles'],  # 20
         data_platinum[3]['EntitiesRubles'],

         data_platinum[4]['CertificateRubles'],  # 50
         data_platinum[4]['EntitiesRubles'],

         data_platinum[5]['CertificateRubles'],  # 100
         data_platinum[5]['EntitiesRubles'],

         data_platinum[6]['CertificateRubles'],  # 250
         data_platinum[6]['EntitiesRubles'],

         data_platinum[7]['CertificateRubles'],  # 500
         data_platinum[7]['EntitiesRubles'],

         time_stamp))
    connection.commit()

finally:
    connection.close()
