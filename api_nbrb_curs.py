import requests as rq

curs = rq.get('https://www.nbrb.by/api/exrates/rates?periodicity=0', verify=False)
curs_json = curs.json()

for i in curs_json:
    if i['Cur_ID'] == 145:
        usd = i['Cur_OfficialRate']
        data_usd = i['Date'][0:10]


def get_usd_curs():
    return usd


def get_usd_data():
    return data_usd

