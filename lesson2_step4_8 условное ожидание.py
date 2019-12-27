from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
print("****$100***")
try:

    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)

    price_field = browser.find_element_by_css_selector("#price")
    print(price_field.text)
    price_field=WebDriverWait(browser, 25).until(#жду когда в поле будет значение $100. Не более 25 сек.
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "#price"),"100")
    )
    button = browser.find_element_by_css_selector("#book")
    button.click()

    input_x = browser.find_element_by_css_selector("#input_value")
    x=int(input_x.text)

    response_field=browser.find_element_by_css_selector("#answer")
    response_field.send_keys(calc(x))

    time.sleep(1)

    button = browser.find_element_by_tag_name("[type='submit']")
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла