from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    input_value_lst = browser.find_elements(By.CSS_SELECTOR, "input")
    for i in range(len(input_value_lst) - 1):
        input_value_lst[i].send_keys(f"{i}")

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'Шаблон.txt')  # добавляем к этому пути имя файла
    browser.find_element(By.CSS_SELECTOR, "#file").send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, ".btn.btn-primary").click()
finally:
    time.sleep(10)
    browser.quit()
