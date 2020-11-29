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
data_stavki = connection.cursor()
data_stavki.execute("select max(data_stavki) from stavki_nb_oper")
max_date_bd = data_stavki.fetchone()
connection.commit()

# выбираем даты на сайте
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

        # elif wb.cell(row, col).value == 'Срок (дней)':
        #     for data in range(wb_ncols):
        #         if type(wb.cell(row, data).value) == float:
        #             date_prepare = xlrd.xldate_as_tuple(wb.cell(row, data).value, wb_date.datemode)
        #             date_prepare = dt.datetime(date_prepare[0], date_prepare[1], date_prepare[2])
        #             date_prepare = dt.datetime.date(date_prepare).strftime('%Y.%m.%d')
        #             data_stavki.append(date_prepare)

max_date_site = dt.datetime.strptime(max(data_stavki), '%Y.%m.%d').date()

date_bd_list = []
date_site_list = []
if max_date_bd[0] != max_date_site:
    print('ss')

    # получаем список дат в БД MySQL
    cur = connection.cursor()
    cur.execute('select data_stavki as data from stavki_nb_oper')
    date_satavki_nb_mysql = cur.fetchall()
    connection.commit()

    time_stamp = dt.datetime.now()

    for i in range(len(date_satavki_nb_mysql)):
        date_bd_list.append(date_satavki_nb_mysql[i][0])

    for x in range(len(data_stavki)):
        date_site_list.append(dt.datetime.strptime(data_stavki[x], '%Y.%m.%d').date())

    for j in range(len(date_site_list)):
        if date_site_list[j] not in date_bd_list:
            cur = connection.cursor()
            cur.execute(
                "INSERT LOW_PRIORITY INTO stavki_nb_oper (data_stavki, kredit_over, depozit_over, dabl_kredit, ts)"
                " VALUES (%s, %s, %s, %s, %s)",
                (data_stavki[j], kredit_over_stavki[j], depozit_over_stavki[j], dabl_kredit[j], time_stamp))
            connection.commit()
