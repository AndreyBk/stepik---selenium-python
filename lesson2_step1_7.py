from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
try:
    browser = webdriver.Chrome()
    browser.get(link)

    # input_x = browser.find_element_by_css_selector("#input_value")
    # x=int(input_x.text)
    # time.sleep(2)

    input_x = browser.find_element_by_css_selector("img")
    x = int(input_x.get_attribute("valuex"))
    time.sleep(2)


    response_field=browser.find_element_by_css_selector("#answer")
    response_field.send_keys(calc(x))

    check_boxL=browser.find_element_by_css_selector("#robotCheckbox")
    check_boxL.click()
    time.sleep(2)

    radio_but=browser.find_element_by_css_selector("#robotsRule")
    radio_but.click()

    time.sleep(3)

    submit_but = browser.find_element_by_css_selector(".btn-default")
    submit_but.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла