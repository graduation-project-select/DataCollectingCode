import urllib.request
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
import os

keywords = ['여성 원피스', '여성 점프수트', 'trousers', 'A라인 스커트', 'H라인 스커트', 'shorts']

def crawling(keyword):
    baseUrl = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='
    # plusUrl = input('검색어를 입력하세요 : ')
    plusUrl = keyword
    url = baseUrl + quote_plus(plusUrl)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    data_list = soup.find_all('div', 'img_area')
    img = []
    for data in data_list:
        img.extend(data.find_all('img'))
    n = 1
    for i in img:
        imgUrl = i['data-source']
        imgUrl = imgUrl.split('&')
        if not (os.path.isdir('temp_img/' + plusUrl)):
            os.makedirs(os.path.join('temp_img/' + plusUrl))
        urllib.request.urlretrieve(imgUrl[0], 'temp_img/' + plusUrl + '/' + str(n) + '.jpg')
        n += 1
    print('다운로드 완료')

for kw in keywords:
    print(kw)
    crawling(kw)