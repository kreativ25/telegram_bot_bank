import matplotlib.pyplot as plt
import io
from PIL import Image
import pymysql as pm
import echo.config as cf
import warnings


def get_plot_sr_all():

    try:
        connection = pm.connect(host=cf.host,
                                user=cf.user,
                                password=cf.password,
                                db=cf.db)

        sr_all = connection.cursor()
        sr_all.execute("select date, sr from sr_all")
        date_bd = sr_all.fetchall()
        connection.commit()

    finally:
        connection.close()

    date = []
    value = []
    for i in range(len(date_bd)):
        date.append(date_bd[i][0])
        value.append(float(date_bd[i][1]))

    date_len = 20
    date = date[-date_len:]
    value = value[-date_len:]

    warnings.simplefilter("ignore", UserWarning)
    plt.figure(figsize=(16, 12), dpi=80)
    plt.plot(date, value, color='tab:red')

    # размер точек на линии
    plt.scatter(x=date, y=value, color='tab:red', s=15)

    # подпись оси у
    plt.yticks(fontsize=20, alpha=.5)

    # подпись оси х / rotation=90 - переварачивваем даты
    plt.xticks(fontsize=14, alpha=.5, rotation=90)

    # название графика
    plt.title('Динамика ставки рефинансирования', fontsize=45, pad=45, alpha=1)

    # подписи точек
    plt.grid(axis='both', alpha=.5)
    for i in range(date_len):
        plt.text(date[i], value[i], value[i], horizontalalignment='left', fontsize=15, alpha=1)

    # Remove borders
    plt.gca().spines["top"].set_alpha(0.0)
    plt.gca().spines["bottom"].set_alpha(0.3)
    plt.gca().spines["right"].set_alpha(0.0)
    plt.gca().spines["left"].set_alpha(0.3)
    # plt.show()

    buf = io.BytesIO()
    plt.savefig(buf, format='png', dpi=80)
    buf.seek(0)
    im = Image.open(buf)
    # im.show()

    # закрываем все открытые окна графика
    plt.cla()
    plt.clf()
    plt.close('all')

    return im
