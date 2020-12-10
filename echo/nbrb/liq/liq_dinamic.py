import pandas as pd
import matplotlib.pyplot as plt
import io
from PIL import Image
import datetime as dt
import pymysql as pm
import echo.config as cf
import warnings


def get_liq_all():

    connection = pm.connect(host=cf.host,
                            user=cf.user,
                            password=cf.password,
                            db=cf.db)

    date = (dt.datetime.now().date() - dt.timedelta(days=360))
    cur = connection.cursor()
    cur.execute(f"select date, liq from liq where date > '{date}' ORDER BY date")
    data_mysql = cur.fetchall()
    connection.commit()

    df = pd.DataFrame(data_mysql)

    df[0] = pd.to_datetime(df[0])
    df[1] = pd.to_numeric(df[1])

    warnings.simplefilter("ignore", UserWarning)

    plt.figure(figsize=(18, 12), dpi=100)
    plt.plot(df[0], df[1], color='tab:red')
    plt.grid(axis='both', alpha=.5)

    # размер точек на линии
    plt.scatter(x=df[0], y=df[1], color='tab:red', s=10)

    # подпись оси у
    plt.yticks(fontsize=30)

    # подпись оси х - делаем разрядность подписей - автоформат
    plt.xticks(fontsize=14, alpha=.5, rotation=90)

    # название графика
    plt.title('Динамика ликвидности банковской системы, млн. руб. Период - 1 год.', fontsize=30, pad=45, alpha=1)

    # Remove borders
    plt.gca().spines["top"].set_alpha(0.0)
    plt.gca().spines["bottom"].set_alpha(0.9)
    plt.gca().spines["right"].set_alpha(0.0)
    plt.gca().spines["left"].set_alpha(0.3)

    # ось х по центру графика
    plt.gca().spines['bottom'].set_position(('data', 0))
    plt.gca().spines['bottom'].set_linewidth(3)
    plt.gca().spines['bottom'].set_color('green')

    plt.rcParams.update({'font.size': 28})

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
