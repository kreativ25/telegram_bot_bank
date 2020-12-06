import re
from echo.nbrb.kurs.api_nbrb_curs import get_kurs_nb


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
        sum_baza = (float(uah) * float(res_num))/100

    if pln_res_1 is not None or pln_res_2 is not None:
        sum_baza = (float(pln) * float(res_num))/10

    if byr_res_1 is not None or byr_res_2 is not None:
        sum_baza = 1 * float(res_num)

    # расчет курсов
    usd_resalt = float('{:.2f}'.format(sum_baza / usd))
    eur_resalt = float('{:.2f}'.format(sum_baza / eur))
    rub_resalt = float('{:.2f}'.format(sum_baza * 100 / rub))
    uah_resalt = float('{:.2f}'.format((sum_baza * 100 / uah)))
    pln_resalt = float('{:.2f}'.format(sum_baza * 10 / pln))

    msg_resalt = '<b>Конвертер валют:</b>\n\n' \
                 '🇧🇾 ' + str('{:.2f}'.format(sum_baza)) + '\n' \
                 '🇺🇸 ' + str(usd_resalt) + '\n' \
                 '🇪🇺 ' + str(eur_resalt) + '\n' \
                 '🇷🇺 ' + str(rub_resalt) + '\n' \
                 '🇺🇦 ' + str(uah_resalt) + '\n' \
                 '🇵🇱 ' + str(pln_resalt)

    if usd_res_1 is not None\
            or usd_res_2 is not None\
            or eur_res_1 is not None\
            or eur_res_2 is not None\
            or rub_res_1 is not None\
            or rub_res_2 is not None\
            or uah_res_1 is not None\
            or uah_res_2 is not None\
            or pln_res_1 is not None\
            or pln_res_2 is not None:
        if res_nam:
            return msg_resalt
        else:
            return False
