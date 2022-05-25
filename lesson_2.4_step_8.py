from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ES
from selenium.webdriver.support.ui import WebDriverWait
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.implicitly_wait(5)

try:
    browser.get(link)

    WebDriverWait(browser, 20).until(ES.text_to_be_present_in_element((By.ID, "price"), "$100"))

    browser.find_element(By.CSS_SELECTOR, "#book").click()

    value_x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)

    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(value_x))

    browser.find_element(By.CSS_SELECTOR, "#solve").click()

finally:
    time.sleep(10)
    browser.quit()
