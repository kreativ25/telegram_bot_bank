import requests as rq
from xml.etree import ElementTree

news = rq.get('http://www.nbrb.by/rss')
root = ElementTree.fromstring(news.content)

# for i in root.iter('*'):
#     print(i.tag)

title = []
link = []
n = 0

for x in root.iter('item'):
    if n < 5:
        for i in x.iter('title'):
            title.append(i.text)

        for j in x.iter('link'):
            link.append(j.text)

        n = n + 1


print(title[4])
print(link[4])