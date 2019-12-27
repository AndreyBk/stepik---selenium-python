from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os

link = "http://suninjuly.github.io/alert_accept.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element_by_tag_name("button")
    button.click()
    time.sleep(1)

    alert = browser.switch_to.alert
    alert.accept()
    time.sleep(1)

    input_x = browser.find_element_by_css_selector("#input_value")
    x=int(input_x.text)

    response_field=browser.find_element_by_css_selector("#answer")
    response_field.send_keys(calc(x))


    time.sleep(1)

    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла