"""
Ищем лекарства
"""

import bs4, re, requests


base = [
    {'name': 'Катэна (капсулы 300 мг № 100) БЕЛУПО', 'url': "https://www.2048080.ru/ekaterinburg/aptsonlist/240677_1?sort-price"},
    {'name': 'Мелоксикам (таблетки 15 мг № 20) Канонфарма', 'url': "https://www.2048080.ru/ekaterinburg/aptsonlist/132262_1?sort-price"},
]


def DrugsMe(url, count=3):
    src = requests.get(url).text
    soup = bs4.BeautifulSoup(src, 'html.parser')
    ff = soup.find('div', class_='list-view-pl', id='apts-listview').findAll('div', class_=re.compile('list-group-item'))
    for i in ff[:min(count, len(ff) + 1)]:
        item = {}
        inf = i.find('div', class_='information')
        item['price'] = float(inf.find('div', class_='price-b').find('span', class_='price').text.strip().replace(' ', '').replace('-', '.'))
        item['geo'] = f"{i.find('geo', class_='geo_apt')['lng']},{i.find('geo', class_='geo_apt')['lat']}"
        item['apt'] = inf.find('div', class_='apt-info').find('div', class_='title').text.strip()
        item['addr'] = inf.find('div', class_='apt-info').find('div', class_='apts-add').text.strip()
        item['phone'] = inf.find('div', class_='phone-pharmacy').findAll('span')[2].text
        print(f"\t{item['price']:7.2f}, {item['apt']}, {item['addr']}, {item['phone']}, {item['geo']}")


for i in base:
    print(i['name'])
    DrugsMe(i['url'])
