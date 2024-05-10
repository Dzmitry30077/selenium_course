from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/get_attribute.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element(By.ID, "treasure")
    x = treasure.get_attribute("valuex")

    result = calc(x)

    answer_input = browser.find_element(By.ID, "answer")
    answer_input.send_keys(result)

    robotCheckbox = browser.find_element(By.ID, "robotCheckbox")
    robotCheckbox.click()

    robotsRule = browser.find_element(By.ID, "robotsRule")
    robotsRule.click()

    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')
    submit_btn.click()

finally:
    time.sleep(30)
    browser.quit()
