import matplotlib.pyplot as plt
import numpy as np
import io
from PIL import Image
import echo.nbrb.kurs.api_nbrb_kurs_all as api_kurs_nb

# количество подписей на оси х
tiks = 6

# наименование валют для названия графика
cod_cur_name = {
    'usd': 'Доллара США',
    'eur': 'Евро',
    'rub': 'Российского рубля',
    'uah': 'Гривны',
    'pln': 'Злотого',
}


def get_term(_term):
    if _term >= tiks:
        return _term // tiks
    else:
        return 1


def get_image_kurs_nb_all(cur, term):
    data = api_kurs_nb.get_kurs_nb_all(api_kurs_nb.kurs_nb_list[cur], term)

    x = []
    y = []

    for i in data:
        x.append(i['Date'][:10])
        y.append(i['Cur_OfficialRate'])

    plt.figure(figsize=(18, 12), dpi=90)
    plt.plot(x, y, color='tab:red', label=cod_cur_name[cur])
    plt.grid(axis='both', alpha=.5)

    # размер точек на линии
    plt.scatter(x=x, y=y, color='tab:red', s=10)

    # подпись оси у
    plt.yticks(fontsize=15)

    # подпись оси х - делаем разрядность подписей - автоформат
    plt.xticks(np.arange(1, term, get_term(term)))
    plt.xticks(fontsize=14,)

    # название графика
    plt.title('Динамика ' + cod_cur_name[cur] + '.' + ' Период: ' + str(term) + ' дней.', fontsize=35, pad=45, alpha=1)

    # Remove borders
    plt.gca().spines["top"].set_alpha(0.0)
    plt.gca().spines["bottom"].set_alpha(0.3)
    plt.gca().spines["right"].set_alpha(0.0)
    plt.gca().spines["left"].set_alpha(0.3)

    # преобразуем в png
    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=100)
    buf.seek(0)
    im = Image.open(buf)
    # im.show()

    return im


# get_image_kurs_nb_all('usd', 350)


