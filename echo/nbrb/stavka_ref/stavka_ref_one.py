from PIL import Image, ImageFont, ImageDraw
import pathlib
from echo.nbrb.stavki_oper.stavki_nb_oper import *
import pymysql as pm
import echo.config as cf


def get_sr():

    try:
        con_sr = pm.connect(host=cf.host,
                            user=cf.user,
                            password=cf.password,
                            db=cf.db)

        sr_one = con_sr.cursor()
        sr_one.execute("select sr, time_stamp from sr_one")
        sr_one_result = sr_one.fetchone()
        con_sr.commit()

    finally:
        con_sr.close()

    sr_value = str(sr_one_result[0])
    sr_date = str(dt.datetime.date(sr_one_result[1]))

    img = Image.new("RGB", (1200, 800), (255, 255, 255))
    img_draw = ImageDraw.Draw(img)

    font_path = pathlib.Path('font/Open_Sans/OpenSans-Regular.ttf').__str__()
    # font_path = pathlib.Path('OpenSans-Regular.ttf').__str__()

    name_font = ImageFont.truetype(font_path, 48)
    stavka_font = ImageFont.truetype(font_path, 300)
    percent_font = ImageFont.truetype(font_path, 150)

    name = 'Ставка рефинансирования Национального банка'
    date = 'на дату:'

    img_draw.text((20, 20), name, font=name_font, fill=(134, 31, 45))

    img_draw.text((350, 100), date, font=name_font, fill=(134, 31, 45))
    img_draw.text((570, 100), sr_date, font=name_font, fill=(134, 31, 45))

    img_draw.text((230, 300), sr_value, font=stavka_font, fill=(134, 31, 45))
    img_draw.text((850, 450), '%', font=percent_font, fill=(134, 31, 45))

    # img.show()

    return img
