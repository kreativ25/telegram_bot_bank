import matplotlib.pyplot as plt
import io
from PIL import Image
import requests as rq
import datetime as dt
from dateutil.parser import *

sr = rq.get('https://www.nbrb.by/api/refinancingrate', verify=False)
sr_json = sr.json()

date = []
value = []

for i in sr_json:
    date_prepare = parse(i['Date'])
    date.append(dt.datetime.date(date_prepare).strftime('%Y.%m.%d'))
    value.append(i['Value'])

date_len = 15
date = date[-date_len:]
value = value[-date_len:]

plt.figure(figsize=(24, 12), dpi=80)
plt.plot(date, value, color='tab:red')

# размер точек на линии
plt.scatter(x=date, y=value, color='tab:red', s=30)

# подпись оси у
plt.yticks(fontsize=20, alpha=.5)

# подпись оси х / rotation=90 - переварачивваем даты
plt.xticks(fontsize=14, alpha=.5, rotation=90)

# название графика
plt.title('Динамика ставки рефинансирования', fontsize=45, pad=45, alpha=.5)

# подписи точек
plt.grid(axis='both', alpha=.5)
for i in range(date_len):
    plt.text(date[i], value[i], value[i], horizontalalignment='left', fontsize=35, alpha=1)

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
im.show()


def get_plot_sr_all():
    return im
