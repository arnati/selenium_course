from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/huge_form.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    lst_links = browser.find_elements(By.CSS_SELECTOR, "input")
    for i in lst_links:
        i.send_keys("my answer")

    button = browser.find_element(By.CSS_SELECTOR, ".btn.btn-default")
    button.click()
finally:
    time.sleep(30)
    browser.quit()
