from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    time.sleep(1)
    browser.find_element(By.CSS_SELECTOR, ".trollface.btn.btn-primary").click()

    print(browser.window_handles)

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    time.sleep(1)
    value_x = int(browser.find_element(By.CSS_SELECTOR, "#input_value").text)

    browser.find_element(By.CSS_SELECTOR, "#answer").send_keys(calc(value_x))

    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
finally:
    time.sleep(30)
    browser.quit()
