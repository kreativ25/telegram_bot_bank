import requests as rq
import xlrd
import datetime as dt
import pymysql as pm
import echo.config as cf

# Блок подключения к БД MySQL
connection = pm.connect(host=cf.host,
                        user=cf.user,
                        password=cf.password,
                        db=cf.db)

# # запрос к MySQL - максимальная дата
# cur = connection.cursor()
# cur.execute("select max(data_stavki) from stavki_nb_oper")
# max_date_stavki_bd = cur.fetchone()
# connection.commit()
#
# # проверяем время последнего обновления информации
# cur = connection.cursor()
# cur.execute('select max(ts) as max_ts from stavki_nb_oper')
# max_ts_stavki_nb_mysql = cur.fetchone()
#
# # получаем список дат в БД MySQL
# cur = connection.cursor()
# cur.execute('select data_stavki as data from stavki_nb_oper')
# date_satavki_nb_mysql = cur.fetchall()
#
# list_date_satavki_nb_mysql = []
# for i in date_satavki_nb_mysql:
#     list_date_prepare = dt.datetime.strftime(i[0], '%Y.%m.%d')
#     list_date_satavki_nb_mysql.append(list_date_prepare)
#
# # обновление базы данных MySQL при наличии новых данных на сайте
# time_stamp = dt.datetime.now()
#
# if (dt.datetime.now().minute - dt.datetime.time(max_ts_stavki_nb_mysql[0]).minute) > 10:
#
#     # подключаем экселевский файл
#     url_nb_oper = 'http://www.nbrb.by/statistics/monetarypolicyinstruments/interestrates/intratesnbrb_archive.xlsx'
#     r = rq.get(url_nb_oper)
#
#     wb = xlrd.open_workbook(file_contents=r.content)
#     wb_date = xlrd.open_workbook(file_contents=r.content)
#     wb_range = max(range(wb.nsheets))  # номер максимальной страницы
#     wb = wb.sheet_by_index(wb_range)
#
#     wb_ncols = wb.ncols  # количество столбцов
#     wb_nrows = wb.nrows  # количество строк
#
#     data_stavki = []
#     kredit_over_stavki = []
#     depozit_over_stavki = []
#     dabl_kredit = []
#
#     # выбираем ставки по кредиту овернайт
#     for row in range(wb_nrows):
#         for col in range(wb_ncols):
#
#             if wb.cell(row, col).value == 'кредит овернайт':
#                 for data in range(wb_ncols):
#                     if type(wb.cell(row, data).value) == float:
#                         kredit_over_stavki.append(wb.cell(row, data).value * 100)
#
#             if wb.cell(row, col).value == 'депозиты овернайт':
#                 for data in range(wb_ncols):
#                     if type(wb.cell(row, data).value) == float:
#                         depozit_over_stavki.append(wb.cell(row, data).value * 100)
#
#             if wb.cell(row, col).value == 'ломбардный кредит по фиксированной ставке':
#                 for data in range(wb_ncols):
#                     if type(wb.cell(row, data).value) == float:
#                         dabl_kredit.append(wb.cell(row, data).value * 100)
#
#             if wb.cell(row, col).value == 'Операции':
#                 for data in range(wb_ncols):
#                     if type(wb.cell(row, data).value) == float:
#                         date_prepare = xlrd.xldate_as_tuple(wb.cell(row, data).value, wb_date.datemode)
#                         date_prepare = dt.datetime(date_prepare[0], date_prepare[1], date_prepare[2])
#                         date_prepare = dt.datetime.date(date_prepare).strftime('%Y.%m.%d')
#                         data_stavki.append(date_prepare)
#
#     max_date_stavki = dt.datetime.strptime(max(data_stavki), '%Y.%m.%d').date()
#
#     # проверяем есть ли новые ставки
#     if max_date_stavki_bd[0] < max_date_stavki:
#         print('Есть новые ставки')
#         x = -1
#         for i in data_stavki:
#             if i in list_date_satavki_nb_mysql:
#                 x = x+1
#                 print(x, i, ' присутствует')
#             else:
#                 x = x + 1
#                 print(x, i, ' NO')
#                 cur = connection.cursor()
#                 cur.execute(
#                     "INSERT LOW_PRIORITY INTO stavki_nb_oper (data_stavki, kredit_over, depozit_over, dabl_kredit, ts)"
#                     " VALUES (%s, %s, %s, %s, %s)",
#                     (data_stavki[x], kredit_over_stavki[x], depozit_over_stavki[x], dabl_kredit[x], time_stamp))
#                 connection.commit()
#

# получаем данные из MySQL для get функций
cur = connection.cursor()
cur.execute('select data_stavki as ds, kredit_over as ko, depozit_over as do, dabl_kredit as dk from stavki_nb_oper')
data_mysql = cur.fetchall()

data_stavki_mysql = []
kredit_over_stavki_mysql = []
depozit_over_stavki_mysql = []
dabl_kredit_mysql = []


# выбираем все даты из MySQL
def get_data_stavki_all():
    for i in data_mysql:
        data_stavki_mysql_prepare = dt.datetime.strftime(i[0], '%Y.%m.%d')
        data_stavki_mysql.append(data_stavki_mysql_prepare)

    return data_stavki_mysql


# выбираем последнюю дату изменения ставок в MySQL
def get_data_stavki_one():
    data_stavki_one = get_data_stavki_all()
    data_stavki_one = data_stavki_one[-1]

    return data_stavki_one


# список ставок по кредиту овернайт
def get_kredit_over_stavki():
    for i in data_mysql:
        kredit_over_stavki_mysql.append(i[1])

    return kredit_over_stavki_mysql


# выбираем последнюю ставку по кредиту овернайт
def get_kredit_over_stavki_one():
    kredit_over_stavki_one = get_kredit_over_stavki()
    kredit_over_stavki_one = kredit_over_stavki_one[-1]

    return kredit_over_stavki_one


# список ставок по депозиту овернайт
def get_depozit_over_stavki():
    for i in data_mysql:
        depozit_over_stavki_mysql.append(i[2])

    return depozit_over_stavki_mysql


# выбираем последнюю ставку по депозиту овернайт
def get_depozit_over_stavki_one():
    depozit_over_stavki_one = get_depozit_over_stavki()
    depozit_over_stavki_one = depozit_over_stavki_one[-1]

    return depozit_over_stavki_one


# список ставок по двусторонним кредитам
def get_dabl_kredit_stavki():
    for i in data_mysql:
        dabl_kredit_mysql.append(i[3])

    return dabl_kredit_mysql


# выбираем последнюю ставку по двусторонним кредитам
def get_dabl_kredit_stavki_one():
    dabl_kredit_stavki_one = get_dabl_kredit_stavki()
    dabl_kredit_stavki_one = dabl_kredit_stavki_one[-1]

    return dabl_kredit_stavki_one
