from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/registration1.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    input_first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.first")
    input_first_name.send_keys("Ivan")
    input_last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")
    input_last_name.send_keys("Petrov")
    input_email = browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
    input_email.send_keys("Petrov@gmail.com")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()

    time.sleep(1)
    welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "h1")
    welcome_text = welcome_text_elt.text
    assert "Congratulations! You have successfully registered!" == welcome_text
finally:
    time.sleep(10)
    browser.quit()
