from PIL import Image, ImageFont, ImageDraw
import pathlib
from echo.nbrb.liq.liq_api import get_liq_data_old, get_liq_delta

img = Image.new("RGB", (1200, 800), (255, 255, 255))
img_draw = ImageDraw.Draw(img)

font_path = pathlib.Path('font/Open_Sans/OpenSans-Regular.ttf').__str__()
# font_path = pathlib.Path('OpenSans-Regular.ttf').__str__()

name_font = ImageFont.truetype(font_path, 60)
date_font = ImageFont.truetype(font_path, 53)
title_font = ImageFont.truetype(font_path, 40)
price_font = ImageFont.truetype(font_path, 30)
line_font = ImageFont.truetype(font_path, 10)

name = 'Показатели ликвидности, млн. руб.'
date = 'на утро:'

name_pl = 'показатели'
sum = 'сумма'
delta = 'изменение'

liq = 'Ликвидность'
prt_1 = 'Позиция по'
prt_2 = 'резервным'
prt_3 = 'требованиям'

psi_1 = 'Позиция по'
psi_2 = 'инструментам'

line = ''
for _ in range(260):
    line = line + '_'


def znak(x):
    if x > 0:
        return '"плюс"  '
    elif x == 0:
        return 'без изменений'
    else:
        return '"минус"  '


def _null(x):
    if x == 0:
        return ''
    else:
        return x


# название
img_draw.text(
    (70, 20),
    name,
    font=name_font,
    fill=(134, 31, 45),

)
img_draw.text(
    (350, 110),
    date,
    font=date_font,
    fill=(134, 31, 45),

)
img_draw.text(
    (570, 110),
    str(get_liq_data_old()[0]),
    font=date_font,
    fill=(134, 31, 45),

)

# название таблицы
img_draw.text(
    (70, 250),
    name_pl,
    font=title_font,
    fill=(134, 31, 45),

)
img_draw.text(
    (500, 250),
    sum,
    font=title_font,
    fill=(134, 31, 45),

)
img_draw.text(
    (800, 250),
    delta,
    font=title_font,
    fill=(134, 31, 45),

)
img_draw.text(
    (40, 300),
    line,
    font=line_font,
    fill=(134, 31, 45),

)

# Ликвидность
img_draw.text(
    (70, 350),
    liq,
    font=title_font,
    fill=(134, 31, 45),

)
img_draw.text(
    (500, 350),
    str('{:.1f}'.format(float(get_liq_data_old()[1])).replace(',', ' ')),
    font=title_font,
    fill=(134, 31, 45),

)
img_draw.text(
    (800, 350),
    znak(get_liq_delta()['liq']) + str(_null(get_liq_delta()['liq'])),
    font=title_font,
    fill=(134, 31, 45),

)

# ПРТ
img_draw.text(
    (70, 450),
    prt_1,
    font=title_font,
    fill=(134, 31, 45),

)
img_draw.text(
    (70, 490),
    prt_2,
    font=title_font,
    fill=(134, 31, 45),

)
img_draw.text(
    (70, 530),
    prt_3,
    font=title_font,
    fill=(134, 31, 45),

)
img_draw.text(
    (500, 450),
    str('{:.1f}'.format(float(get_liq_data_old()[2])).replace(',', ' ')),
    font=title_font,
    fill=(134, 31, 45),

)
img_draw.text(
    (800, 450),
    znak(get_liq_delta()['prt']) + str(_null(get_liq_delta()['prt'])),
    font=title_font,
    fill=(134, 31, 45),

)

# ПСИ
img_draw.text(
    (70, 630),
    psi_1,
    font=title_font,
    fill=(134, 31, 45),

)
img_draw.text(
    (70, 670),
    psi_2,
    font=title_font,
    fill=(134, 31, 45),

)
img_draw.text(
    (500, 630),
    str('{:.1f}'.format(float(get_liq_data_old()[3])).replace(',', ' ')),
    font=title_font,
    fill=(134, 31, 45),

)
img_draw.text(
    (800, 650),
    znak(get_liq_delta()['psi']) + str(_null(get_liq_delta()['psi'])),
    font=title_font,
    fill=(134, 31, 45),

)

# img.show()


def get_img_liq_one():
    return img
