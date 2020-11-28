from requests.adapters import HTTPAdapter
import datetime as dt
import requests as rq
import pymysql as pm
import echo.config as cf

# делаем стабильное подключение с реконектом = 7 раз
url = 'https://www.nbrb.by/api/refinancingrate'
adapter = HTTPAdapter(max_retries=7)
with rq.Session() as session:
    session.mount(url, adapter)
    response = session.get(url)

sr_all_result = response.json()
print(sr_all_result)