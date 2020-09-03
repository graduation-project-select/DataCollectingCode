import urllib.request
from bs4 import BeautifulSoup
import os

count = 0
url = 'https://www.mytheresa.com/ko-kr/clothing/tops/blouses.html?p=1'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')
data_list = soup.find_all('ul', 'products-grid')
label_list = []
for data in data_list:
    label_list.extend(data.find_all('li', 'item'))
for label in label_list:
    count = count + 1
    print(str(count))
    img = label.find('img')
    # title = img['alt']
    img_src = img['data-src']
    if not (os.path.isdir('temp_img/blouses')):
        os.makedirs(os.path.join('temp_img/blouses'))
    urllib.request.urlretrieve('http:' + img_src, 'temp_img/blouses/' + str(count) + '.jpg')
