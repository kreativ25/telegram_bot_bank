import re
from echo.nbrb.kurs.api_nbrb_curs import get_kurs_nb

# print(get_kurs_nb()['usd'])

text = '100 sdffssdfsdfsusdдол'

# res = re.search(r'\d+', text) #числа
# res = re.search(r'usd', text) #слова
# res = re.search(r'дол', text) #слова

# print(res.group(0))

def converter(re_text):
    usd = float(get_kurs_nb()['usd'])
    eur = float(get_kurs_nb()['eur'])
    rub = float(get_kurs_nb()['rub'])

    res = re.search(r'usd', re_text)
    res_2 = re.search(r'дол', re_text)
    res_nam = float(re.search(r'\d+', text).group(0))

    if res is not None or res_2 is not None:
        print('да')
        print(int(res_nam), 'долларов')
        print(int(usd * res_nam), 'рублей')
        print(int((usd * res_nam)/eur), 'евро')
        print(int(((usd * res_nam) / rub)*100), 'рос руб')


    return re_text

converter(text)
