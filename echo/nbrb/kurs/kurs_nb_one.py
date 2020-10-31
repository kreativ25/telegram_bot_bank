from PIL import Image, ImageFont, ImageDraw
import pathlib
from echo.nbrb.kurs.api_nbrb_curs import *

img = Image.new("RGB", (1200, 800), (255, 255, 255))
img_draw = ImageDraw.Draw(img)

font_path = pathlib.Path('font/Open_Sans/OpenSans-Regular.ttf').__str__()
# font_path = pathlib.Path('OpenSans-Regular.ttf').__str__()

name_font = ImageFont.truetype(font_path, 60)
date_font = ImageFont.truetype(font_path, 50)
kurs_font = ImageFont.truetype(font_path, 50)
line_font = ImageFont.truetype(font_path, 20)

name = 'Курсы валют Национального банка'
date = 'на дату:'
usd = '1 USD:'
eur = '1 EUR:'
rub = '100 RUB:'
uah = '100 UAH:'
pln = '10 PLN:'
line = '_______________________________________________'

img_draw.text((60, 20), name, font=name_font, fill=(134, 31, 45))

img_draw.text((350, 100), date, font=date_font, fill=(134, 31, 45))
img_draw.text((570, 100), get_date_kurs_nb(), font=date_font, fill=(134, 31, 45))

img_draw.text((360, 230), usd, font=date_font, fill=(134, 31, 45))
img_draw.text((620, 230), str(get_kurs_nb()['usd']), font=kurs_font, fill=(134, 31, 45))
img_draw.text((360, 290), line, font=line_font, fill=(20, 11, 15))

img_draw.text((360, 330), eur, font=date_font, fill=(134, 31, 45))
img_draw.text((620, 330), str(get_kurs_nb()['eur']), font=kurs_font, fill=(134, 31, 45))
img_draw.text((360, 390), line, font=line_font, fill=(20, 11, 15))

img_draw.text((360, 430), rub, font=date_font, fill=(134, 31, 45))
img_draw.text((620, 430), str(get_kurs_nb()['rub']), font=kurs_font, fill=(134, 31, 45))
img_draw.text((360, 490), line, font=line_font, fill=(20, 11, 15))


img_draw.text((360, 530), uah, font=date_font, fill=(134, 31, 45))
img_draw.text((620, 530), str(get_kurs_nb()['uah']), font=kurs_font, fill=(134, 31, 45))
img_draw.text((360, 590), line, font=line_font, fill=(20, 11, 15))


img_draw.text((360, 630), pln, font=date_font, fill=(134, 31, 45))
img_draw.text((620, 630), str(get_kurs_nb()['pln']), font=kurs_font, fill=(134, 31, 45))
img_draw.text((360, 690), line, font=line_font, fill=(20, 11, 15))

# img.show()


def get_kurs_nb_one():
    return img