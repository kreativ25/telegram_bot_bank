import matplotlib.pyplot as plt
import io
from PIL import Image
from echo.nbrb.kurs.get_func_curs import *
import warnings


def get_kurs_nb_pln_all():

    term = 700
    data_pln = curs_nb_all('pln', max_date_curs_nb(), term)

    x = []
    y = []

    for i in range(len(data_pln)):
        x.append(data_pln[i][0])
        y.append(float(data_pln[i][1]))

    cur_name = 'Польского злотого'

    warnings.simplefilter("ignore", UserWarning)
    plt.figure(figsize=(18, 12), dpi=100)
    plt.plot(x, y, color='tab:red', label=cur_name)
    plt.grid(axis='both', alpha=.5)

    # размер точек на линии
    plt.scatter(x=x, y=y, color='tab:red', s=10)

    # подпись оси у
    plt.yticks(fontsize=15)

    # подпись оси х - делаем разрядность подписей - автоформат
    plt.xticks(fontsize=14, alpha=.5, rotation=90)

    # название графика
    plt.title('Динамика ' + cur_name + ' - за последние ' + str(term) + ' дней.', fontsize=35, pad=45, alpha=1)

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

    # закрываем все открытые окна графика
    plt.cla()
    plt.clf()
    plt.close('all')

    return im
