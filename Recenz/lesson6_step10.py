from selenium import webdriver
import time

try: 
    # link = "http://suninjuly.github.io/registration1.html"
    link = "http://suninjuly.github.io/registration2.html"
    
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
    input1 = browser.find_element_by_tag_name("input")
    input1.send_keys("Ivan")
    
    #вариант с placeholder 
    #input2 = browser.find_element_by_xpath('//input[@placeholder="Input your last name"]')
    
    input2 = browser.find_element_by_xpath('//div[@class="first_block"]//input[@class="form-control second"]')
    input2.send_keys("Petrov")
    
    #вариант с placeholder 
    #input3 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
    
    input3 = browser.find_element_by_xpath('//div[@class="first_block"]//input[@class="form-control third"]')
    input3.send_keys("v354@24.ru")
    
    
    #input3 = browser.find_element_by_class_name("city")
    #input3 = browser.find_element(By.CLASS_NAME, "city")
    #input3.send_keys("Smolensk")
    #input4 = browser.find_element_by_id("country")
    #input4.send_keys("Russia")
    time.sleep(3)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()

    # Тест успешно проходит на странице http: // suninjuly.github.io / registration1.html
    # Тест падает с ошибкой "Message: no such element" на странице http: // suninjuly.github.io / registration2.html
    # Селекторы уникальны