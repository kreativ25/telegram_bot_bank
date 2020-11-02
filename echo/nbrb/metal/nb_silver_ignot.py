from requests import Session
from requests.adapters import HTTPAdapter
import datetime as dt
from PIL import Image, ImageFont, ImageDraw
import pathlib

date = dt.datetime.date(dt.datetime.now()).__str__()
kod_metal = 1
url = f'https://www.nbrb.by/api/ingots/prices/{kod_metal}?ondate={date}'

# делаем стабильное подключение с реконектом = 7 раз
adapter = HTTPAdapter(max_retries=7)
with Session() as session:
    session.mount(url, adapter)
    response = session.get(url)

metal_data = response.json()

img = Image.new("RGB", (1200, 800), (255, 255, 255))
img_draw = ImageDraw.Draw(img)


data = dt.datetime.date(dt.datetime.now()).__str__()
font_path = pathlib.Path('font/Open_Sans/OpenSans-Regular.ttf').__str__()
# font_path = pathlib.Path('OpenSans-Regular.ttf').__str__()

name_font = ImageFont.truetype(font_path, 60)
date_font = ImageFont.truetype(font_path, 53)
title_font = ImageFont.truetype(font_path, 40)
price_font = ImageFont.truetype(font_path, 30)
line_font = ImageFont.truetype(font_path, 10)

name = 'Цены на СЕРЕБРЕННЫЕ мерные слитки'
date = 'на дату:'
nominal = 'номинал'
pokupka = 'покупка, руб.'
prodaja = 'продажа, руб.'

line = ''
for _ in range(243):
    line = line + '_'

img_draw.text((20, 20), name, font=name_font, fill=(134, 31, 45))
img_draw.text((350, 110), date, font=date_font, fill=(134, 31, 45))
img_draw.text((570, 110), data, font=date_font, fill=(134, 31, 45))

img_draw.text((100, 220), nominal, font=title_font, fill=(0, 31, 45))
img_draw.text((400, 220), pokupka, font=title_font, fill=(0, 31, 45))
img_draw.text((800, 220), prodaja, font=title_font, fill=(0, 31, 45))
img_draw.text((100, 270), line, font=line_font, fill=(134, 31, 45))


up_text = 0
up_line = 0
for i in range(len(metal_data)):
    img_draw.text((120, 280 + up_text), str('{:,}'.format(int(metal_data[i]['Nominal'])).replace(',', ' ')) + ' г.', font=price_font, fill=(0, 31, 45))
    img_draw.text((420, 280 + up_text), str('{:,}'.format(metal_data[i]['CertificateRubles']).replace(',', ' ')), font=price_font, fill=(0, 31, 45))
    img_draw.text((820, 280 + up_text), str('{:,}'.format(metal_data[i]['EntitiesRubles']).replace(',', ' ')), font=price_font, fill=(0, 31, 45))
    img_draw.text((100, 310 + up_line), line, font=line_font, fill=(134, 31, 45))

    up_text = up_text + 40
    up_line = up_line + 40

# img.show()


def get_silver_ignot():
    return img
