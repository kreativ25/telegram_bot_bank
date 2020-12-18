from PIL import Image, ImageFont, ImageDraw
import pathlib
import pymysql as pm
import echo.config as cf


def curs(_in, _out):

    global exh
    if _in == 'usd_in':
        exh = 'Доллар США'
    if _in == 'eur_in':
        exh = 'Евро'
    if _in == 'rub_in':
        exh = 'Российский рубль'

    try:
        connection = pm.connect(host=cf.host, user=cf.user, password=cf.password, db=cf.db)
        curs = connection.cursor()
        curs.execute(f'select bank_name, {_in}, {_out}, time_stamp from curs order by {_out} asc')
        curs = curs.fetchall()
        connection.commit()
    finally:
        connection.close()

    img = Image.new("RGB", (1200, 800), (255, 255, 255))
    img_draw = ImageDraw.Draw(img)
    # font_path = pathlib.Path('OpenSans-Regular.ttf').__str__()
    font_path = pathlib.Path('font/Open_Sans/OpenSans-Regular.ttf').__str__()

    name = 'Текущие курсы банков - ' + exh
    # name = 'Текущие курсы банков - Российский рубль'
    name_font = ImageFont.truetype(font_path, 55)
    title_font = ImageFont.truetype(font_path, 50)
    line_font = ImageFont.truetype(font_path, 10)
    text_font = ImageFont.truetype(font_path, 35)
    text_time_font = ImageFont.truetype(font_path, 27)

    img_draw.text((20, 20), name, font=name_font, fill=(134, 31, 45))

    title_name = 'Банк'
    title_in = 'Покупка'
    title_out = 'Продажа'
    title_time = 'Время'

    line = ''
    for _ in range(285):
        line = line + '_'

    img_draw.text((50, 120), title_name, font=title_font, fill=(0, 31, 45))
    img_draw.text((450, 120), title_in, font=title_font, fill=(0, 31, 45))
    img_draw.text((700, 120), title_out, font=title_font, fill=(0, 31, 45))
    img_draw.text((950, 120), title_time, font=title_font, fill=(0, 31, 45))
    img_draw.text((30, 180), line, font=line_font, fill=(134, 31, 45))

    up_text = 0
    up_line = 0
    for i in range(len(curs)):
        img_draw.text((50, 200 + up_text), curs[i][0], font=text_font, fill=(0, 31, 45))
        img_draw.text((490, 200 + up_text), str(curs[i][1]), font=text_font, fill=(0, 31, 45))
        img_draw.text((740, 200 + up_text), str(curs[i][2]), font=text_font, fill=(0, 31, 45))
        img_draw.text((950, 200 + up_text), str(curs[i][3])[:-3], font=text_time_font, fill=(0, 31, 45))

        img_draw.text((30, 245 + up_line), line, font=line_font, fill=(134, 31, 45))

        up_text = up_text + 60
        up_line = up_line + 60

    # img.show()

    return img

# curs('eur_in', 'eur_out')


# date = dt.datetime.date(dt.datetime.now()).__str__()
#
# data_all = get_curs('usd_in', 'usd_out')
#
# img = Image.new("RGB", (1200, 800), (255, 255, 255))
# img_draw = ImageDraw.Draw(img)
# font_path = pathlib.Path('OpenSans-Regular.ttf').__str__()
# # font_path = pathlib.Path('font/Open_Sans/OpenSans-Regular.ttf').__str__()
#
# name = 'Текущие курсы банков - Доллар США'
# # name = 'Текущие курсы банков - Российский рубль'
# name_font = ImageFont.truetype(font_path, 55)
# title_font = ImageFont.truetype(font_path, 50)
# line_font = ImageFont.truetype(font_path, 10)
# text_font = ImageFont.truetype(font_path, 35)
# text_time_font = ImageFont.truetype(font_path, 27)
#
# img_draw.text((20, 20), name, font=name_font, fill=(134, 31, 45))
#
# title_name = 'Банк'
# title_in = 'Покупка'
# title_out = 'Продажа'
# title_time = 'Время'
#
# line = ''
# for _ in range(285):
#     line = line + '_'
#
# img_draw.text((50, 120), title_name, font=title_font, fill=(0, 31, 45))
# img_draw.text((450, 120), title_in, font=title_font, fill=(0, 31, 45))
# img_draw.text((700, 120), title_out, font=title_font, fill=(0, 31, 45))
# img_draw.text((950, 120), title_time, font=title_font, fill=(0, 31, 45))
# img_draw.text((30, 180), line, font=line_font, fill=(134, 31, 45))
#
# up_text = 0
# up_line = 0
# for i in range(len(data_all)):
#     img_draw.text((50, 200 + up_text), data_all[i][0], font=text_font, fill=(0, 31, 45))
#     img_draw.text((490, 200 + up_text), str(data_all[i][1]), font=text_font, fill=(0, 31, 45))
#     img_draw.text((740, 200 + up_text), str(data_all[i][2]), font=text_font, fill=(0, 31, 45))
#     img_draw.text((950, 200 + up_text), str(data_all[i][3])[:-3], font=text_time_font, fill=(0, 31, 45))
#
#     img_draw.text((30, 245 + up_line), line, font=line_font, fill=(134, 31, 45))
#
#     up_text = up_text + 60
#     up_line = up_line + 60
#
# img.show()
#
#
# def get_usd_kurs_kb():
#     return img
