import requests as rq
from xml.etree import ElementTree


news = rq.get('http://www.nbrb.by/rss')
root = ElementTree.fromstring(news.content)
# for i in root.iter('*'):
#     print(i.tag)

for i in root.iter('title'):
    if i.text != 'Национальный банк Республики Беларусь | новости':
        print(i.tag, i.text)


# print(root)
