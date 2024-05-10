from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://suninjuly.github.io/math.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    value_x = browser.find_element(By.ID, "input_value").text
    result = calc(value_x)
    
    input_field = browser.find_element(By.ID, "answer")
    input_field.send_keys(result)

    robot = browser.find_element(By.ID, "robotCheckbox")
    robot.click()

    robot_rule = browser.find_element(By.ID, "robotsRule")
    robot_rule.click()

    submit_btn = browser.find_element(By.CSS_SELECTOR, 'button.btn.btn-default')
    submit_btn.click()

finally:
    time.sleep(30)
    browser.quit()
