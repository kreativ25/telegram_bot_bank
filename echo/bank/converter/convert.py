import re
from echo.nbrb.kurs.api_nbrb_curs import get_kurs_nb

# print(get_kurs_nb()['usd'])

text = '10 sdffssdfsdfрбелк'

# res = re.search(r'\d+', text) #числа
# res = re.search(r'usd', text) #слова
# res = re.search(r'дол', text) #слова

def converter(re_text):
    usd = float(get_kurs_nb()['usd'])
    eur = float(get_kurs_nb()['eur'])
    rub = float(get_kurs_nb()['rub'])
    uah = float(get_kurs_nb()['uah'])
    pln = float(get_kurs_nb()['pln'])

    usd_res_1 = re.search(r'usd', re_text)
    usd_res_2 = re.search(r'дол', re_text)

    eur_res_1 = re.search(r'eur', re_text)
    eur_res_2 = re.search(r'евр', re_text)

    rub_res_1 = re.search(r'rub', re_text)
    rub_res_2 = re.search(r'росс', re_text)

    uah_res_1 = re.search(r'uah', re_text)
    uah_res_2 = re.search(r'грив', re_text)


    pln_res_1 = re.search(r'pln', re_text)
    pln_res_2 = re.search(r'злот', re_text)

    byr_res_1 = re.search(r'рубл', re_text)
    byr_res_2 = re.search(r'белк', re_text)


    res_nam = re.search(r'\d+', re_text)
    if res_nam:
        res_num = res_nam.group(0)

    # расчет базовой суммы
    sum_baza = 1

    if usd_res_1 is not None or usd_res_2 is not None:
        sum_baza = float(usd) * float(res_num)

    if eur_res_1 is not None or eur_res_2 is not None:
        sum_baza = float(eur) * float(res_num)

    if rub_res_1 is not None or rub_res_2 is not None:
        sum_baza = (float(rub) * float(res_num))/100

    if uah_res_1 is not None or uah_res_2 is not None:
        sum_baza = float(uah) * float(res_num)

    if pln_res_1 is not None or pln_res_2 is not None:
        sum_baza = float(pln) * float(res_num)

    if byr_res_1 is not None or byr_res_2 is not None:
        sum_baza = 1 * float(res_num)


    return sum_baza




print(converter(text))


    #
    #
    #
    #
    # res = re.search(r'usd', re_text)
    # res_2 = re.search(r'дол', re_text)
    # # res_nam = float(re.search(r'\d+', re_text).group(0))
    #
    #
    #
    # if res is not None or res_2 is not None:
    #     if res_nam:
    #         result = '<b>' + str(int((usd * float(res_num_2)))) + ' рублей </b> \n'
    #         return result
    #     else:
    #         return False




        # print(int(res_nam), 'долларов')
        # print(int(usd * res_nam), 'рублей')
        # print(int((usd * res_nam)/eur), 'евро')
        # print(int(((usd * res_nam) / rub)*100), 'рос руб')

# news_text = '<b>Новости Национального банка:</b> \n'

