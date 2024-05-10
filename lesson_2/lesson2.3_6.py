from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

link = "http://suninjuly.github.io/redirect_accept.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    btn_troll = browser.find_element(By.CSS_SELECTOR, "button.trollface.btn.btn-primary")
    btn_troll.click()

    new_window = browser.window_handles[1]

    browser.switch_to.window(new_window)

    input_value = browser.find_element(By.ID, "input_value").text
    result = calc(input_value)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(result)

    submit = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit.click()

finally:
    time.sleep(10)
    browser.quit()
