from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

link = "https://SunInJuly.github.io/execute_script.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    fieldx=browser.find_element_by_css_selector("#input_value")
    x=fieldx.text

    input = browser.find_element_by_css_selector("#answer")
    input.send_keys(calc(x))


    button = browser.find_element_by_tag_name("button")

    check_boxL=browser.find_element_by_css_selector("#robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", check_boxL)
    check_boxL.click()
    time.sleep(1)

    radio_but=browser.find_element_by_css_selector("#robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_but)
    radio_but.click()

    time.sleep(1)

    # submit_but = browser.find_element_by_css_selector(".btn-default")
    # submit_but.click()
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла