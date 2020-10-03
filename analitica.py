from dateutil.parser import *
import datetime as dt
import locale

locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
test = 'Mon, 28 Sep 2020 14:43:00 +0300'
dd = parse(test)

dd = dt.datetime.date(dd).strftime('%d-%b-%Y')

print(dd)
