from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select
import os

link = "http://suninjuly.github.io/file_input.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    firstName=browser.find_element_by_css_selector("[name='firstname']")
    firstName.send_keys("Name")

    firstName=browser.find_element_by_css_selector("[name='lastname']")
    firstName.send_keys("lastname")

    firstName=browser.find_element_by_css_selector("[name='email']")
    firstName.send_keys("email")


    fileLoad= browser.find_element_by_css_selector("#file")
    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'lesson1_step2.py')  # добавляем к этому пути имя файла
    fileLoad.send_keys(file_path)


    button = browser.find_element_by_tag_name("button")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла