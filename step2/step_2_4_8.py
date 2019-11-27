from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time
import math
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser = webdriver.Chrome()
    browser.get(link)
    # Ваш код, который заполняет обязательные поля

    label = WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), '100')
    )

    button = browser.find_element_by_css_selector("#book")
    button.click()
    '''
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt')
    
    elem1 = browser.find_element_by_css_selector("#file")
    elem1.send_keys(file_path)

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button")
    button.click()
    '''
    x = browser.find_element_by_css_selector("#input_value").text
    y = calc(x)
    elem1 = browser.find_element_by_css_selector("#answer")
    elem1.send_keys(y)
    button = browser.find_element_by_css_selector("#solve")
    button.click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(40)
    # закрываем браузер после всех манипуляций
    browser.quit()
