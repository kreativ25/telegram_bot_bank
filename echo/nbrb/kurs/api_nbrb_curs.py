import requests as rq
from requests.adapters import HTTPAdapter

# делаем стабильное подключение с реконектом = 7 раз
url = 'https://www.nbrb.by/api/exrates/rates?periodicity=0'
adapter = HTTPAdapter(max_retries=7)
with rq.Session() as session:
    session.mount(url, adapter)
    response = session.get(url)


curs_json = response.json()

kurs_nb = {}
kurs_nb_list = {
    'usd': 145,
    'eur': 292,
    'rub': 298,
    'uah': 290,
    'pln': 293,
}

for i in curs_json:
    for x in kurs_nb_list:
        if i['Cur_ID'] == kurs_nb_list[x]:
            kurs_nb[x] = i['Cur_OfficialRate']

        if i['Cur_ID'] == 145:
            date = i['Date']

date = date[:10]


def get_kurs_nb():
    return kurs_nb


def get_date_kurs_nb():
    return date
