from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

link = "http://suninjuly.github.io/selects1.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # input_x = browser.find_element_by_css_selector("#input_value")
    # x=int(input_x.text)
    time.sleep(1)

    num_1 = browser.find_element_by_css_selector("#num1")
    n1 = int(num_1.text)
    num_2 = browser.find_element_by_css_selector("#num2")
    n2 = int(num_2.text)
    rez=n1+n2

    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(str(rez))  # ищем элемент с текстом "Python"
    time.sleep(1)



    submit_but = browser.find_element_by_css_selector(".btn-default")
    submit_but.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла