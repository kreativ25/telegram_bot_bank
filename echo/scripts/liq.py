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

# получаем список дат в БД MySQL
cur = connection.cursor()
cur.execute('select date as date_mysql from liq')
date_list_mysql = cur.fetchall()

date_now = dt.datetime.now().date()


if date_now != max_date_mysql[0]:

    list_date_mysql = []
    for i in date_list_mysql:
        list_date_prepare = dt.datetime.strptime(dt.datetime.strftime(i[0], '%Y.%m.%d'), '%Y.%m.%d').date()
        list_date_mysql.append(list_date_prepare)

    # выбираем данные с сайта НБ
    url = 'https://www.nbrb.by/mp/liquidity/arch/liqudity_ru.xlsx'

    adapter = HTTPAdapter(max_retries=10)
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
    data_all = {}

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

    for i in range(len(date_liq)):
        data_all[i] = {
            'date_liq': date_liq[i],
            'liq': liq[i],
            'prt': prt[i],
            'psi': psi[i],

        }

    for i in range(len(data_all)):
        date_p = dt.datetime.strptime(data_all[i]['date_liq'], '%Y.%m.%d').date()
        if date_p not in list_date_mysql:
            time_stamp = dt.datetime.now()
            cur = connection.cursor()
            cur.execute("INSERT LOW_PRIORITY INTO liq (date, liq, prt, psi, time_stamp) VALUES (%s, %s, %s, %s, %s)",
                        (data_all[i]['date_liq'], data_all[i]['liq'], data_all[i]['prt'], data_all[i]['psi'], time_stamp))
            connection.commit()
