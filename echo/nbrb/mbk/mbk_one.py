from PIL import Image, ImageFont, ImageDraw
import pathlib
from echo.nbrb.mbk.mbk_api import get_mbk_one


img = Image.new("RGB", (1200, 800), (255, 255, 255))
img_draw = ImageDraw.Draw(img)

font_path = pathlib.Path('font/Open_Sans/OpenSans-Regular.ttf').__str__()
# font_path = pathlib.Path('OpenSans-Regular.ttf').__str__()

name_font = ImageFont.truetype(font_path, 85)
date_font = ImageFont.truetype(font_path, 53)
percent_font = ImageFont.truetype(font_path, 170)
sum_font = ImageFont.truetype(font_path, 70)
no_font = ImageFont.truetype(font_path, 90)


name = 'Ставкa однодневного МБК'
date = 'на дату:'
persent = 'Ставка:'
sum = 'Объем:'
no = 'Сделки не заключались!'

# название
img_draw.text(
    (20, 20),
    name,
    font=name_font,
    fill=(134, 31, 45),

)
img_draw.text(
    (350, 150),
    date,
    font=date_font,
    fill=(134, 31, 45),

)

img_draw.text(
    (570, 150),
    str(get_mbk_one()[0][0]),
    font=date_font,
    fill=(134, 31, 45),

)

# ставка и объем
if str(get_mbk_one()[0][2]) != 0:
    img_draw.text(
        (120, 350),
        persent,
        font=date_font,
        fill=(134, 31, 45),

    )

    img_draw.text(
        (520, 260),
        str(get_mbk_one()[0][2]) + ' %',
        font=percent_font,
        fill=(134, 31, 45),

    )

    img_draw.text(
        (120, 550),
        sum,
        font=date_font,
        fill=(134, 31, 45),

    )

    img_draw.text(
        (520, 530),
        str(get_mbk_one()[0][1]) + ' тыс. руб.',
        font=sum_font,
        fill=(134, 31, 45),

    )


else:
    img_draw.text(
        (50, 400),
        no,
        font=no_font,
        fill=(134, 31, 45),
    )

img.show()


def get_img_mbk_one():
    return img
