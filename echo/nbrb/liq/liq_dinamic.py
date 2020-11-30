import matplotlib.pyplot as plt
import numpy as np
import io
from PIL import Image
from echo.nbrb.liq.liq_api import get_liq_all, get_date_liq_all

# устанавливаем количество отображаемых дат
date_len = 360

# ось х
x = get_date_liq_all()
x = x[:date_len]

# ось y - приводим к float формату
y = get_liq_all()
y_prepare = []
for i in y:
    y_prepare.append(float(i))
y = np.array(y_prepare)
y = y[:date_len]

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
plt.title('Динамика ликвидности банковской системы, млн. руб. Период - ' + str(date_len) + ' дней.', fontsize=30, pad=45, alpha=1)

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
im.show()


def get_liq_all():
    return im
