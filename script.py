from selenium import webdriver
from selenium.webdriver import ActionChains


driver = webdriver.Chrome()
driver.get('https://timeweb.com/ru/services/hosting/#hosting-optimo')

input_name = driver.find_element_by_css_selector("html > body.pattern1 > div.overlay > div.table > div.cell > div.form.w560 > form > div.double > div.left > div.label.js-fiz > div > input.suggestions-input")
input_name.send_keys("HSBCBankplc")

input_email = driver.find_element_by_css_selector("html > body.pattern1 > div.overlay > div.table > div.cell > div.form.w560 > form > div.double > div.left > div.columns > div.c5-5 > div.label > div > input.suggestions-input")
input_email.send_keys("123.public@gmail.com")

input_btn = driver.find_element_by_css_selector("html > body.pattern1 > div.overlay > div.table > div.cell > div.form.w560 > form > div.double > div.left > div.hosting-items__button.js-send-hosting-form.mt10")
input_btn.click()

