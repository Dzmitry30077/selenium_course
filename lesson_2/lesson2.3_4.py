from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/alert_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    btn = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    btn.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    time.sleep(2)

    input_value = browser.find_element(By.ID, "input_value").text
    result = calc(input_value)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(result)

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit.click()
    
finally:
    time.sleep(10)
    browser.quit()
