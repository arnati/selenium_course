from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


link = "http://suninjuly.github.io/math.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    time.sleep(1)

    value_x = browser.find_element(By.ID, "input_value")

    input_answer = browser.find_element(By.ID, "answer")
    input_answer.send_keys(calc(int(value_x.text)))

    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    robot_checkbox.click()

    robot_radiobutton = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robot_radiobutton.click()

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()
finally:
    time.sleep(10)
    browser.quit()
