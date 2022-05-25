from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_link_text_redirect13.html?first_name=yu&last_name=utu&firstname=tu&firstname=tyu#"
browser = webdriver.Chrome()

try:
    browser.get(link)

    input_first_name = browser.find_element(By.CSS_SELECTOR, "[name='first_name']")
    input_first_name.send_keys("Ivan")
    input_last_name = browser.find_element(By.CSS_SELECTOR, "[name='last_name']")
    input_last_name.send_keys("Petrov")
    input_city = browser.find_element(By.CSS_SELECTOR, "input.form-control.city")
    input_city.send_keys("Smolensk")
    input_country = browser.find_element(By.ID, "country")
    input_country.send_keys("Russia")

    button = browser.find_element(By.CSS_SELECTOR, "[class='btn btn-default']")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
