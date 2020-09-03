import urllib.request
from bs4 import BeautifulSoup
import time

# codi 크롤링
for i in range(16, 100):
    print('page : ' + str(i))
    url = 'https://ko.codibook.net/codi?page='+str(i)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    data_list = soup.find_all('div', {'id': 'content'})
    label_list = []
    for data in data_list:
        label_list.extend(data.find_all('div', 'codi'))
    codi_list = []
    for label in label_list:
        title_label = label.find('a', 'codi_link')
        title = title_label['data-codi_id']
        codi_list.append(title)
    # codi item 크롤링
    for codi in codi_list:
        count = 0
        url = 'https://ko.codibook.net/codi/' + codi
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html, 'html.parser')
        item_data_list = soup.find('div', {'id': 'content'})
        item_label_list = []
        for item_data in item_data_list:
            item_label_list.extend(item_data.find_all('div', 'item'))
        for item_label in item_label_list:
            count = count + 1
            item = item_label.find('img', 'item')
            # print(item)
            img_src = item['src']
            urllib.request.urlretrieve(img_src, codi + '_' + str(count) + '.png')
            time.sleep(5)
