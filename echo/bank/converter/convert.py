import re
from echo.nbrb.kurs.api_nbrb_curs import get_kurs_nb

# print(get_kurs_nb()['usd'])

text = '10 sdffssdfsdfsusdдол'

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
    # res_nam = float(re.search(r'\d+', re_text).group(0))

    res_nam = re.search(r'\d+', re_text)
    if res_nam:
        res_num_2 = res_nam.group(0)

    if res is not None or res_2 is not None:
        result = str((usd * float(res_num_2))) + ' рублей'

    return result







        # print('да')
        # print(int(res_nam), 'долларов')
        # print(int(usd * res_nam), 'рублей')
        # print(int((usd * res_nam)/eur), 'евро')
        # print(int(((usd * res_nam) / rub)*100), 'рос руб')

    # return '<b>' + 'Новости Национального банка:</b> \n'
    #     ret = str(int(res_nam))+ ' долларов'

# print(converter(text))

# news_text = '<b>Новости Национального банка:</b> \n'

