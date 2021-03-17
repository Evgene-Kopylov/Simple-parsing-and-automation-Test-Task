from selenium import webdriver
from selenium.webdriver import ActionChains

import time

from bs4 import BeautifulSoup

driver = webdriver.Chrome()
driver.get('https://timeweb.com/ru')
# driver.get('https://manga.garden/')

data = driver.page_source
with open('data.txt', 'w', encoding='utf-8') as f:
    f.write(data)
print(data)
soup = BeautifulSoup(data, 'html.parser')


el_el = 'html > body > main > div.block.block-intro > div > div.intro-text > p'
up_time_el = "js-up-time-info-template"
sub_fee_el = "html.k-webkit.k-webkit88 > body.l-decor-bg.cp-style-theme.page-site.locale-ru_RU.page-start > #default-layout > div.grid__content > div.layout-cnt-w.js-content-wrapper > #p0 > div.page-start.js-main-page > div.flex-row > div.flex-row.flex-row_revers > #w4-4-604863f1 > article.cpS-icon-n-info-blk > div.cpS-icon-n-info > p.cpS-h-XS"
time_left_el = "html.k-webkit.k-webkit88 > body.l-decor-bg.cp-style-theme.page-site.locale-ru_RU.page-start > #default-layout > div.grid__content > div.layout-cnt-w.js-content-wrapper > #p0 > div.page-start.js-main-page > div.flex-row > div.flex-row.flex-row_revers > #w4-4-604863f1 > article.cpS-icon-n-info-blk.__last > div.cpS-icon-n-info > p.cpS-h-XS"

def get_text(doom):
    path = doom.replace("> ", "").replace("..", ".")
    content = soup.select_one(path)
    return content

el = get_text(el_el)
up_time = get_text(up_time_el)
sub_fee = get_text(sub_fee_el)
time_left = get_text(time_left_el)


# print(f"{el=}")
# print(f"{up_time=}")
# print(f"{sub_fee=}")
# print(f"{time_left=}")


