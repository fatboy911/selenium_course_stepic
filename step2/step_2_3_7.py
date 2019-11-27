from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Ваш код, который заполняет обязательные поля

    elem1 = browser.find_element_by_css_selector("[name='firstname']")
    elem1.send_keys('a')
    elem1 = browser.find_element_by_css_selector("[name='lastname']")
    elem1.send_keys('a')
    elem1 = browser.find_element_by_css_selector("[name='email']")
    elem1.send_keys('a')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')

    elem1 = browser.find_element_by_css_selector("#file")
    elem1.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
