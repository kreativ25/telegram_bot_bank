from PIL import Image, ImageFont, ImageDraw
import pathlib
from echo.nbrb.stavki_oper.stavki_nb_oper import *

img = Image.new("RGB", (1200, 800), (255, 255, 255))
img_draw = ImageDraw.Draw(img)

data = dt.datetime.date(dt.datetime.now()).__str__()
font_path = pathlib.Path('nbrb/stavki_oper/OpenSans-Regular.ttf').__str__()
# font_path = pathlib.Path('OpenSans-Regular.ttf').__str__()

name_font = ImageFont.truetype(font_path, 53)
date_font = ImageFont.truetype(font_path, 45)
data_font = ImageFont.truetype(font_path, 45)
stavka_font = ImageFont.truetype(font_path, 80)

name = 'Ставки по операциям Национального банка'
date = 'на дату:'
kredit_over = 'кредит овернайт:'
depozit_over = 'депозит овернайт:'
dabl_kredit = 'двусторонний кредит:'

img_draw.text((20, 20), name, font=name_font, fill=(134, 31, 45))
img_draw.text((350, 100), date, font=name_font, fill=(134, 31, 45))
img_draw.text((570, 100), data, font=name_font, fill=(134, 31, 45))

img_draw.text((20, 300), kredit_over, font=name_font, fill=(134, 31, 45))
img_draw.text((620, 273), get_kredit_over_stavki_one() + ' %', font=stavka_font, fill=(134, 31, 45))

img_draw.text((20, 450), dabl_kredit, font=name_font, fill=(134, 31, 45))
img_draw.text((620, 423), get_dabl_kredit_stavki_one() + ' %', font=stavka_font, fill=(134, 31, 45))

img_draw.text((20, 600), depozit_over, font=name_font, fill=(134, 31, 45))
img_draw.text((620, 573), get_depozit_over_stavki_one() + ' %', font=stavka_font, fill=(134, 31, 45))


def get_stavki_oper_one():
    return img