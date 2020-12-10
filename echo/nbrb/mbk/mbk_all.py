import matplotlib.pyplot as plt
import io
from PIL import Image
import datetime as dt
from echo.nbrb.mbk.mbk_api import get_mbk_all
import warnings


def get_mbk():

    date_len = 290
    x = []
    y = []
    v = []

    for i in get_mbk_all(date_len):
        x_prepare = dt.datetime.strptime(dt.datetime.strftime(i[0], '%Y.%m.%d'), '%Y.%m.%d').date()
        x.append(x_prepare)
        y.append(float(i[2]))
        v.append(float(i[1]))

    x = x[:date_len]
    y = y[:date_len]
    v = v[:date_len]

    warnings.simplefilter("ignore", UserWarning)
    plt.figure(figsize=(18, 12), dpi=100)
    plt.plot(x, y, color='tab:red')
    plt.grid(axis='both', alpha=.5)

    # размер точек на линии
    plt.scatter(x=x, y=y, color='tab:red', s=10)

    # подпись оси у
    plt.yticks(fontsize=30)

    # подпись оси х - делаем разрядность подписей - автоформат
    plt.xticks(fontsize=14, alpha=.5, rotation=90)

    # название графика
    plt.title('Динамика ставки МБК. Период - ' + str(date_len) + ' дней.', fontsize=30, pad=45, alpha=1)

    # Remove borders
    plt.gca().spines["top"].set_alpha(0.0)
    plt.gca().spines["bottom"].set_alpha(0.9)
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
