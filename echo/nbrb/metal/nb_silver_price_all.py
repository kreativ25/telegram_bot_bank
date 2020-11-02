from requests import Session
from requests.adapters import HTTPAdapter
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import io
from PIL import Image

term = 360
date_start = (dt.datetime.date(dt.datetime.now()) - dt.timedelta(days=term)).__str__()
date_end = dt.datetime.date(dt.datetime.now()).__str__()
kod_metal = 1
url = f'https://www.nbrb.by/api/bankingots/prices/{kod_metal}?startdate={date_start}&enddate={date_end}'

# делаем стабильное подключение с реконектом = 7 раз
adapter = HTTPAdapter(max_retries=7)
with Session() as session:
    session.mount(url, adapter)
    response = session.get(url)

tiks = 6
metal_name = 'СЕРЕБРА'
data = response.json()

x = []
y = []

for i in data:
    x.append(i['Date'][:10])
    y.append(i['Value'])

y_day =y[-1:]

plt.figure(figsize=(18, 12), dpi=100)
plt.plot(x, y, color='tab:red', label=metal_name)
plt.grid(axis='both', alpha=.5)

# размер точек на линии
plt.scatter(x=x, y=y, color='tab:red', s=10)

# подпись оси у
plt.yticks(fontsize=15)

# подпись оси х - делаем разрядность подписей - автоформат
plt.xticks(np.arange(1, term, term // tiks))
plt.xticks(fontsize=14,)

# название графика
plt.title('Динамика ' + metal_name + ' - ' + str(term) + ' дней. Текущая цена (1 г.) - ' + str(y_day[0]) + ' руб.', fontsize=35, pad=45, alpha=1)

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


def get_nb_silver_price_all():
    return im