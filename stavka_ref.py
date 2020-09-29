from PIL import Image, ImageFont, ImageDraw
import requests as rq
import datetime as dt

data = dt.datetime.date(dt.datetime.now()).__str__()
params = {'ondate': data}

sr = rq.get('https://www.nbrb.by/api/refinancingrate', params=params, verify=False)
sr_json = sr.json()
sr = sr_json[0]['Value'].__str__()
# sr = sr + ' %'

img = Image.open('png/sr.png')
data_font = ImageFont.truetype('font/Open_Sans/OpenSans-Regular.ttf', 50)
sr_font = ImageFont.truetype('font/Open_Sans/OpenSans-Regular.ttf', 350)

img_draw = ImageDraw.Draw(img)
img_draw.text((520, 333), data, font=data_font, fill=(134, 31, 65))
img_draw.text((220, 500), sr, font=sr_font, fill=(134, 31, 65))


# img.show()

def get_sr():
    return img

