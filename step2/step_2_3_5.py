from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Ваш код, который заполняет обязательные поля

    button = browser.find_element_by_css_selector("button")
    button.click()

    # alert = browser.switch_to.alert
    # alert.accept()
    new_name = browser.window_handles[1]

    browser.switch_to.window(new_name)

    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)
    elem1 = browser.find_element_by_css_selector("#answer")
    elem1.send_keys(y)
    button = browser.find_element_by_css_selector("button")
    button.click()

    '''
    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)
    elem1 = browser.find_element_by_css_selector("#answer")
    elem1.send_keys(y)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    elem1 = browser.find_element_by_css_selector("[for='robotCheckbox']")
    elem1.click()
    elem1 = browser.find_element_by_css_selector("[for='robotsRule'")
    elem1.click()
    button.click()
    '''
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
