from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "https://suninjuly.github.io/file_input.html"


try:
    browser = webdriver.Chrome()
    browser.get(link)

    name = browser.find_element(By.NAME, "firstname")
    last_name = browser.find_element(By.NAME, "lastname")
    email = browser.find_element(By.NAME, "email")
    file = browser.find_element(By.ID, 'file')

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'test.txt')
    

    name.send_keys('a')
    last_name.send_keys('b')
    email.send_keys('email')
    file.send_keys(file_path)
    
    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-primary")
    submit_btn.click()
    
finally:
    time.sleep(10)
    browser.quit()
