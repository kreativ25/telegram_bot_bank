import requests as rq
import datetime as dt

date_end = dt.datetime.date(dt.datetime.now()).__str__()
kurs_nb_list = {
    'usd': 145,
    'eur': 292,
    'rub': 298,
    'uah': 290,
    'pln': 293,
}


def get_kurs_nb_all(cod_cur, date_end_delta):
    date_start = (dt.datetime.date(dt.datetime.now()) - dt.timedelta(days=date_end_delta)).__str__()
    kurs = rq.get(f'https://www.nbrb.by/api/exrates/rates/dynamics/{cod_cur}?startdate={date_start}&enddate={date_end}',
                  verify=False)
    kurs_json = kurs.json()
    return kurs_json

# print(get_kurs_nb_all(kurs_nb_list['usd'], 10))
