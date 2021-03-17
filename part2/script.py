from selenium import webdriver
from selenium.webdriver import ActionChains

import time

from bs4 import BeautifulSoup

import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'RBA_test_task.settings')


def get_raw_to_file():
    '''
    считывает и сохраняет содержание страницы
    '''
    driver = webdriver.Chrome()
    driver.get('https://timeweb.com/ru/services/hosting/#hosting-optimo')

    input_name = driver.find_element_by_css_selector("html > body.pattern1 > div.overlay > div.table > div.cell > div.form.w560 > form > div.double > div.left > div.label.js-fiz > div > input.suggestions-input")
    input_name.send_keys("HSBCBankplc")

    input_email = driver.find_element_by_css_selector("html > body.pattern1 > div.overlay > div.table > div.cell > div.form.w560 > form > div.double > div.left > div.columns > div.c5-5 > div.label > div > input.suggestions-input")
    input_email.send_keys("123.public@gmail.com")

    input_btn = driver.find_element_by_css_selector("html > body.pattern1 > div.overlay > div.table > div.cell > div.form.w560 > form > div.double > div.left > div.hosting-items__button.js-send-hosting-form.mt10")
    input_btn.click()

    time.sleep(4)

    driver.get("https://hosting.timeweb.ru/")
    time.sleep(2)
    driver.get("https://hosting.timeweb.ru/")
    driver.execute_script("return document.documentElement.outerHTML")
    data = driver.page_source
    with open('data.html', 'w', encoding='utf-8') as f:
        f.write(data)

# get_raw_to_file()
with open('data.html', 'r', encoding='utf-8') as f:
    data = f.read()

soup = BeautifulSoup(data, 'html.parser')


up_time_el = "#up-time-info > p > span.cpS-tooltip-inline.js-info-tooltip"
sub_fee_el = "article.cpS-icon-n-info-blk > div.cpS-icon-n-info > p.cpS-h-XS"
time_left_el = "article.cpS-icon-n-info-blk.__last > div.cpS-icon-n-info > p.cpS-h-XS"


def get_text(doom):
    path = doom.replace("> ", "").replace("..", ".")
    content = soup.select_one(path)
    return " ".join((content.text.replace("\n", " ")).split())



up_time = get_text(up_time_el)
sub_fee = get_text(sub_fee_el)
time_left = get_text(time_left_el)


print(f"{up_time=}")
print(f"{sub_fee=}")
print(f"{time_left=}")

from web_panel.models import ParsingResults
def save_res(slot_1, slot_2, slot_3):
    # res = 
    pass






