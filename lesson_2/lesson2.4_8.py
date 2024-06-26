from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math
import time

link = "http://suninjuly.github.io/explicit_wait2.html"

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    browser.get(link)

    price = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    btn_book = browser.find_element(By.ID, "book")
    btn_book.click()

    input_value = browser.find_element(By.ID, "input_value").text
    result = calc(input_value)

    answer = browser.find_element(By.ID, "answer")
    answer.send_keys(result)

    submit = browser.find_element(By.ID, "solve")
    submit.click()


finally:
    time.sleep(15)
    browser.quit()