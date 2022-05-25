from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/selects2.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    time.sleep(1)

    value_a = browser.find_element(By.CSS_SELECTOR, "#num1")
    value_b = browser.find_element(By.CSS_SELECTOR, "#num2")
    s = int(value_a.text) + int(value_b.text)

    browser.find_element(By.CSS_SELECTOR, "#dropdown").click()
    browser.find_element(By.XPATH, f"//option[text()='{s}']").click()

    browser.find_element(By.CSS_SELECTOR, ".btn.btn-default").click()
finally:
    time.sleep(10)
    browser.quit()
