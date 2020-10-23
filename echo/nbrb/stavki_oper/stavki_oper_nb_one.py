from PIL import Image, ImageFont, ImageDraw
import pathlib
from echo.nbrb.stavki_oper.stavki_nb_oper import *


data = dt.datetime.date(dt.datetime.now()).__str__()

img_path = pathlib.Path('nbrb/stavki_oper/stavki_oper_one.png')
font_path = pathlib.Path('nbrb/stavki_oper/OpenSans-Regular.ttf').__str__()

img = Image.open(img_path)
data_font = ImageFont.truetype(font_path, 45)
stavka_font = ImageFont.truetype(font_path, 80)

img_draw = ImageDraw.Draw(img)
img_draw.text((520, 83), data, font=data_font, fill=(153, 0, 51))
img_draw.text((550, 233), get_kredit_over_stavki_one(), font=stavka_font, fill=(134, 31, 45))
img_draw.text((550, 360), get_dabl_kredit_stavki_one(), font=stavka_font, fill=(134, 31, 45))
img_draw.text((550, 510), get_depozit_over_stavki_one(), font=stavka_font, fill=(134, 31, 45))
# img.show()


def get_stavki_oper_one():
    return img

