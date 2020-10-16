import requests as rq
import xlrd

# подключаем экселевский файл
url_nb_oper = 'http://www.nbrb.by/statistics/monetarypolicyinstruments/interestrates/intratesnbrb_archive.xlsx'
r = rq.get(url_nb_oper)

wb = xlrd.open_workbook(file_contents=r.content)
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


print(kredit_over_stavki)
print(depozit_over_stavki)
print(dabl_kredit)



# дата
# кредит овернайт
# ставка реф
# деп овернайт
# двусторонний кредит
# тс