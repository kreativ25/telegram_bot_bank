import requests as rq
from xml.etree import ElementTree
import datetime as dt
from requests.adapters import HTTPAdapter
from dateutil.parser import *


def get_economy():

    url = 'http://www.economy.gov.by/ru/rss-ru/'
    adapter = HTTPAdapter(max_retries=10)
    with rq.Session() as session:
        session.mount(url, adapter)
        response = session.get(url)

        root = ElementTree.fromstring(response.content)

    title = []
    link = []
    pubDate = []
    n = 0
    count = 5

    for x in root.iter('item'):
        if n < count:
            for i in x.iter('title'):
                title.append(i.text.strip())

            for j in x.iter('guid'):
                link.append(j.text)

            for h in x.iter('pubDate'):
                date_prepare = parse(h.text)
                pubDate.append(dt.datetime.date(date_prepare).strftime('%Y.%m.%d'))
            n = n + 1

    news_text = '<b>Новости Министерства Финансов:</b> \n'

    for a in range(5):
        nam = a + 1
        news_text = news_text + str(nam) + ')' + ' <a href="' + link[a] + '">' + title[a] + '</a>' + ' (' \
                    + str(pubDate[a]) + ')\n\n'

    return news_text
