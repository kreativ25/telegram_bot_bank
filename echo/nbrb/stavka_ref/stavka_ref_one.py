from PIL import Image, ImageFont, ImageDraw
import pathlib
from echo.nbrb.stavki_oper.stavki_nb_oper import *

img = Image.new("RGB", (1200, 800), (255, 255, 255))
img_draw = ImageDraw.Draw(img)

data = dt.datetime.date(dt.datetime.now()).__str__()
params = {'ondate': data}

sr = rq.get('https://www.nbrb.by/api/refinancingrate', params=params, verify=False)
sr_json = sr.json()
sr = sr_json[0]['Value'].__str__()

font_path = pathlib.Path('font/Open_Sans/OpenSans-Regular.ttf').__str__()

name_font = ImageFont.truetype(font_path, 48)
stavka_font = ImageFont.truetype(font_path, 300)
percent_font = ImageFont.truetype(font_path, 150)

name = 'Ставка рефинансирования Национального банка'
date = 'на дату:'

img_draw.text((20, 20), name, font=name_font, fill=(134, 31, 45))

img_draw.text((350, 100), date, font=name_font, fill=(134, 31, 45))
img_draw.text((570, 100), data, font=name_font, fill=(134, 31, 45))

img_draw.text((230, 300), sr, font=stavka_font, fill=(134, 31, 45))
img_draw.text((850, 450), '%', font=percent_font, fill=(134, 31, 45))

# img.show()


def get_sr():
    return img
