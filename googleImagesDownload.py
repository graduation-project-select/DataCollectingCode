# -*- Encoding: UTF-8 -*- #
from urllib.request import urlopen
from urllib.request import urlretrieve
from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import os

root_dir = 'corduroy/'

# search = input('검색어:')
keywords = ['corduroy trousers', '코듀로이 자켓', '코듀로이 셔츠', '코듀로이 팬츠','골덴바지', '골덴 옷']

driver = webdriver.Chrome(ChromeDriverManager().install())

def crawling(keyword):
    url = f'https://www.google.com/search?q={quote_plus(keyword)}&sxsrf=ALeKk009KquRYhbQIQDrU46OIgmcBVrB9w:1597661141060&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiRzqLGh6LrAhVDI6YKHWw6CjEQ_AUoAXoECA4QAw&biw=760&bih=899'
    driver.get(url)
    for i in range(500):
        driver.execute_script("window.scrollBy(0,10000)")
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    img = soup.select('.rg_i.Q4LuWd')
    n=1
    imgUrl = []

    for i in img:
        try:
            imgUrl.append(i.attrs["src"])
        except KeyError:
            imgUrl.append(i.attrs["data-src"])

    for i in imgUrl:
        search = '_'.join(keyword.split())
        download_folder_name = root_dir
        if not (os.path.isdir(download_folder_name)):
            os.makedirs(os.path.join(download_folder_name))
        urlretrieve(i, download_folder_name+ '/' +search+"_"+str(n) + ".jpg")

        n += 1
        if (n == 101):
            break

for kw in keywords:
    print(kw)
    crawling(kw)

driver.close()