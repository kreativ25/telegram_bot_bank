from PIL import Image, ImageFont, ImageDraw
import pathlib
import pymysql as pm
import echo.config as cf


def get_platinum_ignot():

    nominal_ignot = ['1', '5', '10', '20', '50', '100', '250', '500']

    connection = pm.connect(host=cf.host,
                            user=cf.user,
                            password=cf.password,
                            db=cf.db)

    platinum = connection.cursor()
    platinum.execute(f"select date from platinum_ignot")
    date_platinum = platinum.fetchone()
    connection.commit()

    gold_price = connection.cursor()
    gold_price.execute(
        f"select nominal_1_in, nominal_1_out, nominal_5_in, nominal_5_out, nominal_10_in, nominal_10_out,"
        f"nominal_20_in, nominal_20_out, nominal_50_in, nominal_50_out, nominal_100_in, nominal_100_out,"
        f"nominal_250_in, nominal_250_out, nominal_500_in, nominal_500_out "
        f" from platinum_ignot")
    data_gold_price = gold_price.fetchone()
    connection.commit()

    price_in = [data_gold_price[x] for x in range(len(data_gold_price)) if not int(x) % 2]
    price_out = [data_gold_price[x] for x in range(len(data_gold_price)) if int(x) % 2]

    img = Image.new("RGB", (1200, 800), (255, 255, 255))
    img_draw = ImageDraw.Draw(img)

    font_path = pathlib.Path('font/Open_Sans/OpenSans-Regular.ttf').__str__()
    # font_path = pathlib.Path('OpenSans-Regular.ttf').__str__()

    name_font = ImageFont.truetype(font_path, 60)
    date_font = ImageFont.truetype(font_path, 53)
    title_font = ImageFont.truetype(font_path, 40)
    price_font = ImageFont.truetype(font_path, 30)
    line_font = ImageFont.truetype(font_path, 10)

    name = 'Цены на ПЛАТИНОВЫЕ мерные слитки'
    date = 'установленные на дату:'
    nominal = 'номинал'
    pokupka = 'покупка, руб.'
    prodaja = 'продажа, руб.'

    line = ''
    for _ in range(243):
        line = line + '_'

    img_draw.text((20, 20), name, font=name_font, fill=(134, 31, 45))
    img_draw.text((150, 110), date, font=date_font, fill=(134, 31, 45))
    img_draw.text((780, 110), str(date_platinum[0]), font=date_font, fill=(134, 31, 45))

    img_draw.text((100, 220), nominal, font=title_font, fill=(0, 31, 45))
    img_draw.text((400, 220), pokupka, font=title_font, fill=(0, 31, 45))
    img_draw.text((800, 220), prodaja, font=title_font, fill=(0, 31, 45))
    img_draw.text((100, 270), line, font=line_font, fill=(134, 31, 45))

    up_text = 0
    up_line = 0
    for i in range(len(nominal_ignot)):
        img_draw.text(
            (120, 280 + up_text),
            '{:,}'.format(int(nominal_ignot[i])).replace(',', ' ') + ' г.',
            font=price_font,
            fill=(0, 31, 45)
        )
        img_draw.text(
            (420, 280 + up_text),
            str('{:,}'.format(float(price_in[i])).replace(',', ' ')),
            font=price_font,
            fill=(0, 31, 45)
        )
        img_draw.text(
            (820, 280 + up_text),
            str('{:,}'.format(float(price_out[i])).replace(',', ' ')),
            font=price_font,
            fill=(0, 31, 45)
        )
        img_draw.text(
            (100, 310 + up_line),
            line,
            font=line_font,
            fill=(134, 31, 45)
        )

        up_text = up_text + 45
        up_line = up_line + 45

        # img.show()

    return img
