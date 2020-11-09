from requests import Session
from requests.adapters import HTTPAdapter
import xlrd
import re
import datetime as dt
import pymysql as pm
import echo.config as cf

from bs4 import BeautifulSoup

url = 'https://www.nbrb.by/statistics/financialmarkets/interbankrates'

adapter = HTTPAdapter(max_retries=7)
with Session() as session:
    session.mount(url, adapter)
    response = session.post(url,
                            data={'date': '05.11.2020'}
                            )

soop = BeautifulSoup(response.text, 'lxml')


print(soop)
print('=====================================')

test = soop.find('td', text=re.compile('1 день')).next.next.next.text
test2 = soop.find('td', text=re.compile('1 день')).next.next.next.next.next.next.next.text


# test = soop.find('td', text=re.compile('1 день')).next_element.next_element.next_element.text
# test2 = soop.find('td', text=re.compile('1 день')).next_element.next_element.next_element.next_element.next_element.text

print(test)
print(test2)
