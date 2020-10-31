import requests as rq
from requests.adapters import HTTPAdapter
import datetime as dt
import matplotlib.pyplot as plt
import numpy as np
import io
from PIL import Image

term = 365
date_start = (dt.datetime.date(dt.datetime.now()) - dt.timedelta(days=term)).__str__()
date_end = dt.datetime.date(dt.datetime.now()).__str__()
kod_cur = 293
url = f'https://www.nbrb.by/api/exrates/rates/dynamics/{kod_cur}?startdate={date_start}&enddate={date_end}'

# делаем стабильное подключение с реконектом = 7 раз
adapter = HTTPAdapter(max_retries=7)
with rq.Session() as session:
    session.mount(url, adapter)
    response = session.get(url)

tiks = 8
cur_name = 'Злотого'
data = response.json()

x = []
y = []

for i in data:
    x.append(i['Date'][:10])
    y.append(i['Cur_OfficialRate'])

plt.figure(figsize=(18, 12), dpi=100)
plt.plot(x, y, color='tab:red', label=cur_name)
plt.grid(axis='both', alpha=.5)

# размер точек на линии
plt.scatter(x=x, y=y, color='tab:red', s=10)

# подпись оси у
plt.yticks(fontsize=15)

# подпись оси х - делаем разрядность подписей - автоформат
plt.xticks(np.arange(1, term, term // tiks))
plt.xticks(fontsize=14,)

# название графика
plt.title('Динамика ' + cur_name + ' - ' + str(term) + ' дней.', fontsize=35, pad=45, alpha=1)

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


def get_kurs_nb_pln_all():
    return im