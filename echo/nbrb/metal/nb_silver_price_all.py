import matplotlib.pyplot as plt
import io
from PIL import Image
from echo.nbrb.metal.get_metal import get_metall_all

term = 360
data_all = get_metall_all('silver', term)

x = []
y = []

for i in range(len(data_all)):
    x.append(data_all[i][0])
    y.append(float(data_all[i][1]))


metal_name = 'СЕРЕБРО'

y_day =y[-1:]

plt.figure(figsize=(18, 12), dpi=100)
plt.plot(x, y, color='tab:red', label=metal_name)
plt.grid(axis='both', alpha=.5)

# размер точек на линии
plt.scatter(x=x, y=y, color='tab:red', s=10)

# подпись оси у
plt.yticks(fontsize=15)

# подпись оси х - делаем разрядность подписей - автоформат
plt.xticks(fontsize=14, alpha=.5, rotation=90)

# название графика
plt.title('График цен на ' + metal_name + '.' + ' Период - 1 год.' + ' Текущая цена (1 г.) - '
          + str(y_day[0]) + ' руб.', fontsize=30, pad=45, alpha=1)

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
