import matplotlib.pyplot as plt
import numpy as np
import io
from PIL import Image
from echo.nbrb.stavki_oper.stavki_nb_oper import *

# устанавливаем количество отображаемых дат/изменений ставок
date_len = 4
x = get_data_stavki_all()
x = x[:date_len]


# приводим y оси к float формату
# первый временной ряд
y1 = get_kredit_over_stavki()
y1_prepare =[]
for i in y1:
    y1_prepare.append(float(i))
y1 = np.array(y1_prepare)
y1 = y1[:date_len]


# второй временной ряд
y2 = get_depozit_over_stavki()
y2_prepare = []
for i in y2:
    y2_prepare.append(float(i))
y2 = np.array(y2_prepare)
y2 = y2[:date_len]


# делаем несколько временных рядов
plt.figure(figsize=(18, 12), dpi=80)
plt.plot(x, y1, color='tab:red', label='Кредиты овернайт')
plt.plot(x, y2, color='tab:blue', label='Депозиты овернайт')

# размер точек на линии
plt.scatter(x=x, y=y1, color='tab:red', s=30)
plt.scatter(x=x, y=y2, color='tab:blue', s=30)

# подпись оси у
plt.yticks(fontsize=20, alpha=.5)

# подпись оси х / rotation=90 - переварачивваем даты
plt.xticks(fontsize=14, alpha=.5, rotation=90)

# название графика
plt.title('Динамика ставок по операциям НБ', fontsize=45, pad=45, alpha=1)

# подписи точек
plt.grid(axis='both', alpha=.5)
for i in range(len(x)):
    plt.text(x[i], y1[i], y1[i], horizontalalignment='left', fontsize=25, alpha=1)
    plt.text(x[i], y2[i], y2[i], horizontalalignment='left', fontsize=25, alpha=1)

# Remove borders
plt.gca().spines["top"].set_alpha(0.0)
plt.gca().spines["bottom"].set_alpha(0.3)
plt.gca().spines["right"].set_alpha(0.0)
plt.gca().spines["left"].set_alpha(0.3)
plt.legend(fontsize=18)
# # plt.show()

buf = io.BytesIO()
plt.savefig(buf, format='png', dpi=80)
buf.seek(0)
im = Image.open(buf)
# im.show()


def get_plot_stavki_nb_all():
    return im
