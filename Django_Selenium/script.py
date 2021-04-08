from selenium import webdriver
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Django_Selenium.settings')
django.setup()

import time

from bs4 import BeautifulSoup

from web_panel.models import ParsingResults



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

    time.sleep(3)

    driver.get("https://hosting.timeweb.ru/")
    time.sleep(2)
    driver.get("https://hosting.timeweb.ru/")
    time.sleep(1)
    driver.execute_script("return document.documentElement.outerHTML")
    time.sleep(1)
    data = driver.page_source
    with open('data.html', 'w', encoding='utf-8') as f:
        f.write(data)


get_raw_to_file()

with open('data.html', 'r', encoding='utf-8') as f:
    data = f.read()

soup = BeautifulSoup(data, 'html.parser')

up_time_el = "#up-time-info > p > span.cpS-tooltip-inline.js-info-tooltip"
sub_fee_el = "article.cpS-icon-n-info-blk > div.cpS-icon-n-info > p.cpS-h-XS"
time_left_el = "article.cpS-icon-n-info-blk.__last > div.cpS-icon-n-info > p.cpS-h-XS"


def get_text(doom):
    path = doom.replace("> ", "").replace("..", ".")
    content = soup.select_one(path)
    if content:
        return " ".join((content.text.replace("\n", " ")).split())


up_time = get_text(up_time_el)
sub_fee = get_text(sub_fee_el)
time_left = get_text(time_left_el)

print(f"{up_time=}")
print(f"{sub_fee=}")
print(f"{time_left=}")


def save_to_db():
    res = ParsingResults()
    res.slot_1 = up_time
    res.slot_2 = sub_fee
    res.slot_3 = time_left
    res.save()
    print('seved')


save_to_db()

