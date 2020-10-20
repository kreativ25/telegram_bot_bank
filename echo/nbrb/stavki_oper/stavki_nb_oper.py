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


# запрос к MySQL - максимальная дата
cur = connection.cursor()
cur.execute("select max(data_stavki) from stavki_nb_oper")
max_date_stavki_bd = cur.fetchone()
connection.commit()

# print(max_date_stavki_bd)

# подключаем экселевский файл
url_nb_oper = 'http://www.nbrb.by/statistics/monetarypolicyinstruments/interestrates/intratesnbrb_archive.xlsx'
r = rq.get(url_nb_oper)

wb = xlrd.open_workbook(file_contents=r.content)
wb_date = xlrd.open_workbook(file_contents=r.content)
wb_range = max(range(wb.nsheets))  # номер максимальной страницы
wb = wb.sheet_by_index(wb_range)

wb_ncols = wb.ncols  # количество столбцов
wb_nrows = wb.nrows  # количество строк

data_stavki = []
kredit_over_stavki = []
depozit_over_stavki = []
dabl_kredit = []

# выбираем ставки по кредиту овернайт
for row in range(wb_nrows):
    for col in range(wb_ncols):

        if wb.cell(row, col).value == 'кредит овернайт':
            for data in range(wb_ncols):
                if type(wb.cell(row, data).value) == float:
                    kredit_over_stavki.append(wb.cell(row, data).value * 100)

        if wb.cell(row, col).value == 'депозиты овернайт':
            for data in range(wb_ncols):
                if type(wb.cell(row, data).value) == float:
                    depozit_over_stavki.append(wb.cell(row, data).value * 100)

        if wb.cell(row, col).value == 'ломбардный кредит по фиксированной ставке':
            for data in range(wb_ncols):
                if type(wb.cell(row, data).value) == float:
                    dabl_kredit.append(wb.cell(row, data).value * 100)

        if wb.cell(row, col).value == 'Операции':
            for data in range(wb_ncols):
                if type(wb.cell(row, data).value) == float:
                    date_prepare = xlrd.xldate_as_tuple(wb.cell(row, data).value, wb_date.datemode)
                    date_prepare = dt.datetime(date_prepare[0], date_prepare[1], date_prepare[2])
                    date_prepare = dt.datetime.date(date_prepare).strftime('%Y.%m.%d')
                    data_stavki.append(date_prepare)

max_date_stavki = dt.datetime.strptime(max(data_stavki), '%Y.%m.%d').date()

# print(type(max_date_stavki_bd[0]))
# print(type(max_date_stavki))


# проверяем время последнего обновления информации
cur = connection.cursor()
cur.execute('select max(ts) as max_ts from stavki_nb_oper')
max_ts_stavki_nb_mysql = cur.fetchone()

print(max_ts_stavki_nb_mysql[0])
print(dt.datetime.time(max_ts_stavki_nb_mysql[0]).minute)
print(dt.datetime.now().minute)




# проверяем есть ли новые ставки
# if max_date_stavki_bd[0] < max_date_stavki:
#     print('dfafadfs')


#
# time_stamp = dt.datetime.now()
# print(time_stamp)
#
# cur = connection.cursor()
# cur.execute("INSERT INTO stavki_nb_oper (data_stavki, kredit_over, depozit_over, dabl_kredit, ts) VALUES (%s, %s, %s, %s, %s)", (data_stavki[1], kredit_over_stavki[1], depozit_over_stavki[1], dabl_kredit[1], time_stamp))
# connection.commit()


# print(type(max(data_stavki)))
# print(type(max_date_stavki_bd))
# print(len(data_stavki))
#
# print(kredit_over_stavki)
# print(depozit_over_stavki)
# print(dabl_kredit)
# print(data_stavki)