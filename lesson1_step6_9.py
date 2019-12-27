from selenium import webdriver
import time

# link = "http://suninjuly.github.io/registration1.html"
link = "http://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
# 1
    input1 = browser.find_element_by_css_selector("[placeholder=\"Input your first name\"]")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("[placeholder=\"Input your last name\"]")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("[placeholder=\"Input your email\"]")
    input3.send_keys("Smolensk@mail.ru")

    time.sleep(1)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

# 2
    browser.get(link)

    input1 = browser.find_element_by_css_selector("[placeholder=\"Input your first name\"]")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_css_selector("[placeholder=\"Input your last name\"]")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_css_selector("[placeholder=\"Input your email\"]")
    input3.send_keys("Smolensk@mail.ru")
    input4 = browser.find_element_by_css_selector("[placeholder=\"Input your phone:\"]")
    input4.send_keys("123456789")
    input5 = browser.find_element_by_css_selector("[placeholder=\"Input your address:\"]")
    input5.send_keys("Smolensk str")

    time.sleep(1)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

# 3
    browser.get(link)

    input4 = browser.find_element_by_css_selector("[placeholder=\"Input your phone:\"]")
    input4.send_keys("123456789")
    input5 = browser.find_element_by_css_selector("[placeholder=\"Input your address:\"]")
    input5.send_keys("Smolensk str")

    time.sleep(1)
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text
    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" != welcome_text

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла