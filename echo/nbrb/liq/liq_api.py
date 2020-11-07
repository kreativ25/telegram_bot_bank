from requests import Session
from requests.adapters import HTTPAdapter
import xlrd
import re
import datetime as dt
import pymysql as pm
import echo.config as cf

# Блок подключения к БД MySQL
connection = pm.connect(host=cf.host,
                        user=cf.user,
                        password=cf.password,
                        db=cf.db)


# запрос к MySQL - максимальная дата
cur = connection.cursor()
cur.execute("select max(date) from liq")
max_date_mysql = cur.fetchone()
connection.commit()
# print('1) ', max_date_mysql, '<-- максимальная дата Mysql')


# проверяем время последнего обновления информации
cur = connection.cursor()
cur.execute('select max(time_stamp) as max_ts from liq')
max_ts_mysql = cur.fetchone()
# print('2) ', max_ts_mysql, '<-- max time_stamp Mysql')


# получаем список дат в БД MySQL
cur = connection.cursor()
cur.execute('select date as date_mysql from liq')
date_list_mysql = cur.fetchall()
# print('3)  список дат mysql -->', date_list_mysql)

list_date_mysql = []
for i in date_list_mysql:
    list_date_prepare = dt.datetime.strftime(i[0], '%Y.%m.%d')
    list_date_mysql.append(list_date_prepare)
# print('4)  список дат mysql  -->', list_date_mysql)


# обновление базы данных MySQL при наличии новых данных на сайте
time_stamp = dt.datetime.now()

if (dt.datetime.now().minute - dt.datetime.time(max_ts_mysql[0]).minute) > 10:
# if 1<2:
    url = 'https://www.nbrb.by/mp/liquidity/arch/liqudity_ru.xlsx'

    adapter = HTTPAdapter(max_retries=7)
    with Session() as session:
        session.mount(url, adapter)
        response = session.get(url)

    wb = xlrd.open_workbook(file_contents=response.content)
    wb_date = xlrd.open_workbook(file_contents=response.content)
    wb_range = max(range(wb.nsheets))  # номер максимальной страницы
    wb = wb.sheet_by_index(wb_range)

    wb_ncols = wb.ncols  # количество столбцов
    wb_nrows = wb.nrows  # количество строк

    date_liq = []
    liq = []
    prt = []
    psi = []

    for row in range(wb_nrows):
        for col in range(wb_ncols):

            # вытягиваем и форматируем массив дат
            if re.search(r'\bОстаток средств на коррсчетах\b', str(wb.cell(row, col).value)):
                for data in range(wb_ncols):
                    if type(wb.cell(row, data).value) == float:
                        seconds = (wb.cell(row-2, data).value - 25569) * 86400.0
                        date_prepare = dt.datetime.utcfromtimestamp(seconds)
                        date_prepare = dt.datetime.date(date_prepare).strftime('%Y.%m.%d')
                        date_liq.append(date_prepare)

            # Ликвидность
            if re.search(r'\bПоказатели ликвидности\b', str(wb.cell(row, col).value)):
                for data in range(wb_ncols):
                    if type(wb.cell(row, data).value) == float:
                        liq.append(wb.cell(row, data).value)

            # ПРТ
            if re.search(r'\bПозиция по резервным требованиям\b', str(wb.cell(row, col).value)):
                for data in range(wb_ncols):
                    if type(wb.cell(row, data).value) == float:
                        prt.append(wb.cell(row, data).value)

            # ПСИ
            if re.search(r'\bПозиция по стандартным инструментам\b', str(wb.cell(row, col).value)):
                for data in range(wb_ncols):
                    if type(wb.cell(row, data).value) == float:
                        psi.append(wb.cell(row, data).value)

    max_date = dt.datetime.strptime(max(date_liq), '%Y.%m.%d').date()

    # проверяем есть ли новые ставки
    if max_date_mysql[0] < max_date:
    # if 1 < 2:

        print('Есть новые данные')

        x = -1
        for i in date_liq:
            if i in list_date_mysql:
                x = x+1
                print(x, i, ' присутствует')
            else:
                x = x + 1
                print(x, i, ' NO')
                cur = connection.cursor()
                cur.execute("INSERT INTO liq (date, liq, prt, psi, time_stamp) VALUES (%s, %s, %s, %s, %s)",
                            (date_liq[x], liq[x], prt[x], psi[x], time_stamp))
                connection.commit()


# получаем данные из MySQL для get функций
cur = connection.cursor()
cur.execute('select date as _date, liq as _liq, prt as _prt, psi as _psi from liq ORDER BY date')
data_mysql = cur.fetchall()

date_liq_mysql = []
liq_mysql = []
prt_mysql = []
psi_mysql = []


# выбираем все даты из MySQL
def get_date_liq_all():
    for i in data_mysql:
        date_liq_mysql_prepare = dt.datetime.strftime(i[0], '%Y.%m.%d')
        date_liq_mysql.append(date_liq_mysql_prepare)

    return date_liq_mysql


# список значений ликвидности
def get_liq_all():
    for i in data_mysql:
        liq_mysql.append(i[1])

    return liq_mysql


# возвращаем данные на последнюю дату в MySQL
def get_liq_data_old():
    return data_mysql[-1]


def get_liq_delta():
    liq_delta = {
        'liq': int(float(data_mysql[-1][1]) - float(data_mysql[-2][1])),
        'prt': int(float(data_mysql[-1][2]) - float(data_mysql[-2][2])),
        'psi': int(float(data_mysql[-1][3]) - float(data_mysql[-2][3])),

    }
    return liq_delta




# cur = connection.cursor()
# cur.execute("INSERT INTO liq (date, liq, prt, psi, time_stamp) VALUES (%s, %s, %s, %s, %s)",
#             (date_liq[0], liq[0], prt[0], psi[0], time_stamp))
# connection.commit()
#
# cur = connection.cursor()
# cur.execute("INSERT INTO liq (date, liq, prt, psi, time_stamp) VALUES (%s, %s, %s, %s, %s)",
#             (date_liq[1], liq[1], prt[1], psi[1], time_stamp))
# connection.commit()