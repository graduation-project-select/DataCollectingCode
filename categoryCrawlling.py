import urllib.request
from bs4 import BeautifulSoup
import os


class category:
    def __init__(self, c1, c2, page):
        self.c1 = c1
        self.c2 = c2
        self.page = page


categoryList = []

# ## H&M 크롤링
# categoryList.append(category('none', 'none', '1000'))
# categoryList.append(category('dresses', 'ladies_dresses', '682'))
# categoryList.append(category('shirts-and-blouses', 'ladies_shirtsblouses', '190'))
# categoryList.append(category('tops', 'ladies_tops', '683'))
# categoryList.append(category('cardigans-and-jumpers', 'ladies_cardigansjumpers', '289'))
# categoryList.append(category('hoodies-sweatshirts', 'ladies_hoodiessweatshirts', '127'))
# categoryList.append(category('blazers-and-waistcoats', 'ladies_blazerswaistcoats', '75'))
# categoryList.append(category('jackets-and-coats', 'ladies_jacketscoats', '162'))
# categoryList.append(category('knitwear', 'ladies_knitwear', '219'))
# categoryList.append(category('skirts', 'ladies_skirts', '199'))
# categoryList.append(category('shorts', 'ladies_shorts', '110'))
# categoryList.append(category('jumpsuits-playsuits', 'ladies_jumpsuits', '53'))
# categoryList.append(category('trousers', 'ladies_trousers', '277'))
# categoryList.append(category('jeans', 'ladies_jeans', '115'))
# categoryList.append(category('shoes', 'ladies_shoes', '291'))

# categoryList.append(category('shirts-and-tanks', '349'))
# categoryList.append(category('shirts', 'men_shirts', '176'))
# categoryList.append(category('hoodies-sweatshirts', 'men_hoodiessweatshirts', '161'))
# categoryList.append(category('trousers', '196'))
# categoryList.append(category('shorts', '74'))
# categoryList.append(category('jeans', 'men_jeans', '77'))
# categoryList.append(category('shoes', '111'))
# categoryList.append(category('jackets-and-coats', 'men_jacketscoats', '103'))
# categoryList.append(category('blazers-and-suits', 'men_blazerssuits', '44'))

# categoryList.append(category('cardigans-and-jumpers', 'men_cardigansjumpers', '94'))

# categoryList.append(category('dresses', '138'))
# categoryList.append(category('tops', '166'))
# categoryList.append(category('cardigans-jumpers', '45'))
# categoryList.append(category('shirts-and-blouses', '50'))
# categoryList.append(category('jackets-coats', '70'))
# categoryList.append(category('hoodies-sweatshirts', '63'))
# categoryList.append(category('trousers-leggings', '64'))
# categoryList.append(category('jeans', '115'))
# categoryList.append(category('skirts', '48'))
# categoryList.append(category('jumpsuits-playsuits', '11'))
# categoryList.append(category('shorts', '31'))
# categoryList.append(category('shoes', '71'))

# https://www2.hm.com/ko_kr/ladies/shop-by-product/view-all.html?sort=stock&colorWithNames=블루_0000ff&productTypes=드레스&clothingStyles=A라인&image-size=small&image=stillLife&offset=0&page-size=36
# https://www2.hm.com/ko_kr/ladies/shop-by-product/shirts-and-blouses.html?product-type=ladies_shirtsblouses&sort=stock&productTypes=%EC%85%94%EC%B8%A0&image-size=small&image=stillLife&offset=0&page-size=36

# 패턴 없는 것
# pattern_none = 'https://www2.hm.com/ko_kr/ladies/shop-by-product/view-all.html?sort=stock&patterns=%EB%8B%A8%EC%83%89&image-size=small&image=stillLife&offset=0&page-size='


# for i in range(1, 5):
#     categoryList.append(category('tops', 'blouses', i))
# for i in range(1,5):
#     categoryList.append(category('tops', 't-shirts', i))
# for i in range(1,4):
#     categoryList.append(category('tops', 'shirts', i))
# for i in range(1,3):
#     categoryList.append(category('tops', 'sweatshirts', i))
# for i in range(1,4):
#     categoryList.append(category('tops', 'sleeveless', i))
for i in range(1,14):
    categoryList.append(category('jackets', 'jackets', i))

labelName = ''
for cate in categoryList:
    if labelName != cate.c2:
        count = 0
        labelName = cate.c2
    # url = 'https://www2.hm.com/ko_kr/ladies/shop-by-product/'+ cate.name +'.html?product-type='+ cate.type +'&sort=stock&image-size=small&image=stillLife&offset=0&page-size=' + cate.size
    # url = 'https://www2.hm.com/ko_kr/men/shop-by-product/'+ cate.name + '.html?sort=stock&image-size=small&image=stillLife&offset=0&page-size=' + cate.size
    # url = 'https://www2.hm.com/ko_kr/divided/shop-by-product/'+ cate.name + '.html?sort=stock&image-size=small&image=stillLife&offset=0&page-size=' + cate.size
    # url = 'https://www2.hm.com/ko_kr/ladies/shop-by-product/'+ cate.name +'.html?product-type=' + cate.type + '&sort=stock&productTypes=%EC%85%94%EC%B8%A0&image-size=small&image=stillLife&offset=0&page-size=' + cate.size
    # url = pattern_none+ cate.size
    # url = 'https://www.mytheresa.com/ko-kr/clothing/' + cate.c1 + '/' + cate.c2 + '.html?p=' + str(cate.page)
    # url = 'https://www.mytheresa.com/ko-kr/clothing/' + cate.c1 + '/' + cate.c2 + '.html'
    url = 'https://www.mytheresa.com/ko-kr/clothing/' + cate.c1 + '.html?p=' + str(cate.page)
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    html = urllib.request.urlopen(req).read()
    soup = BeautifulSoup(html, 'html.parser')
    data_list = soup.find_all('ul', 'products-grid')
    label_list = []
    for data in data_list:
        label_list.extend(data.find_all('li', 'item'))
    for label in label_list:
        count = count + 1
        print(cate.c1 + '_' + cate.c2 + ':' + str(count))
        img = label.find('img')
        title = img['alt']
        print(title)
        titleArr = title.split(' ')
        img_src = img['data-src']
        # if not (os.path.isdir('temp_img/' + cate.c1 + '_' + cate.c2)):
        #     os.makedirs(os.path.join('temp_img/' + cate.c1 + '_' + cate.c2))
        # urllib.request.urlretrieve('http:' + img_src, 'temp_img/' + cate.c1 + '_' + cate.c2 + '/' + str(count) + '.jpg')
        if titleArr[-3] == '블레이저':
            # urllib.request.urlretrieve('http:' + img_src, 'temp_img/outer_blazers/' + str(count) + '.jpg')
            continue
        if titleArr[-3] == '코트':
            urllib.request.urlretrieve('http:' + img_src, 'temp_img/coat/' + str(count) + '.jpg')
            continue
        if titleArr[-3] == '베스트':
            urllib.request.urlretrieve('http:' + img_src, 'temp_img/vest/' + str(count) + '.jpg')
            continue
        if titleArr[-3] == '카디건':
            urllib.request.urlretrieve('http:' + img_src, 'temp_img/cadigans/' + str(count) + '.jpg')
            continue
        isPadding = 0
        for t in titleArr:
            if t == '다운':
                # urllib.request.urlretrieve('http:' + img_src, 'temp_img/outer_padding/' + str(count) + '.jpg')
                isPadding = 1
                break
        # if not (os.path.isdir('temp_img/outer_coats')):
        #     os.makedirs(os.path.join('temp_img/outer_coats'))
        if isPadding == 0:
            urllib.request.urlretrieve('http:' + img_src, 'temp_img/outer_jackets/' + str(count) + '.jpg')
