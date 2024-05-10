from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://suninjuly.github.io/registration2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    first_name_input = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.first')
    first_name_input.send_keys('Stepik')
    
    last_name_input = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.second')
    last_name_input.send_keys('Org')

    email_input = browser.find_element(By.CSS_SELECTOR, '.first_block .form-control.third')
    email_input.send_keys('Stepik@org.com')

    submit_btn = browser.find_element(By.CSS_SELECTOR, "button.btn")
    submit_btn.click()

    time.sleep(1)

    welcome_text = browser.find_element(By.TAG_NAME, 'h1').text

    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(30)
    browser.quit()
