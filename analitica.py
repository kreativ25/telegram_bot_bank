import matplotlib.pyplot as plt
import io
from PIL import Image

a = [3, 5, 7, 5, 10]
b = [1, 2, 3, 4, 5]

plt.plot(a, b, 'g--')
plt.grid()
plt.xlabel('икс')
plt.ylabel('игрек')
plt.title('Название')

buf = io.BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)
im = Image.open(buf)
# im.show()
# buf.close()


def get_plot():
    return im


# from dateutil.parser import *
# import datetime as dt
# import locale
#
# locale.setlocale(locale.LC_TIME, 'ru_RU.UTF-8')
# test = 'Mon, 28 Sep 2020 14:43:00 +0300'
# dd = parse(test)
#
# dd = dt.datetime.date(dd).strftime('%d-%b-%Y')
#
# print(dd)
