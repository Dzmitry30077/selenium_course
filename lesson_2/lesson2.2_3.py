from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import math

link = "https://suninjuly.github.io/selects1.html"

def summa(a, b):
    return int(a) + int(b)

try:
    browser = webdriver.Chrome()
    browser.get(link)
    
    num1 = browser.find_element(By.ID, 'num1').text
    num2 = browser.find_element(By.ID, 'num2').text
    
    result = summa(num1, num2)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(result))

    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    submit_btn.click()

finally:
    time.sleep(10)
    browser.quit()
