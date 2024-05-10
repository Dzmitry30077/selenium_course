from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "https://SunInJuly.github.io/execute_script.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    input_value = browser.find_element(By.ID, "input_value").text
    
    result = calc(input_value)

    answer = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(result)

    robotCheckbox = browser.find_element(By.ID, "robotCheckbox")
    robotCheckbox.click()

    robotsRule = browser.find_element(By.ID, "robotsRule")
    robotsRule.click()

    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_btn.click()
    
finally:
    time.sleep(10)
    browser.quit()
