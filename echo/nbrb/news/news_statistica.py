import requests as rq
from xml.etree import ElementTree
import datetime as dt
from dateutil.parser import *


def get_statistica():

    news = rq.get('https://www.nbrb.by/rss/?p=stat')
    root = ElementTree.fromstring(news.content)

    title = []
    link = []
    pubDate = []
    n = 0
    count = 5

    for x in root.iter('item'):
        if n < count:
            for i in x.iter('title'):
                title.append(i.text)

            for j in x.iter('link'):
                link.append(j.text)

            for h in x.iter('pubDate'):
                date_prepare = parse(h.text)
                pubDate.append(dt.datetime.date(date_prepare).strftime('%Y.%m.%d'))
            n = n + 1

    news_text = '<b>Статистика Национального банка:</b> \n'

    for a in range(5):
        nam = a + 1
        news_text = news_text + str(nam) + ')' + ' <a href="' + link[a] + '">' + title[a] + '</a>' + ' (' \
                    + str(pubDate[a]) + ')\n\n'

    return news_text
