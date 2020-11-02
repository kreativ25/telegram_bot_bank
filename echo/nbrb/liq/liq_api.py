from requests import Session
from requests.adapters import HTTPAdapter
import xlrd
import re
import datetime as dt

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

date = []
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
                    date_prepare = dt.datetime.date(date_prepare)
                    date.append(date_prepare)

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


