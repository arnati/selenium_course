from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


def link_test(link):
    browser = webdriver.Chrome()
    browser.get(link)
    browser.implicitly_wait(5)

    input_first_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.first")
    input_first_name.send_keys("Ivan")
    input_last_name = browser.find_element(By.CSS_SELECTOR, "div.first_block input.second")
    input_last_name.send_keys("Petrov")
    input_email = browser.find_element(By.CSS_SELECTOR, "div.first_block input.third")
    input_email.send_keys("Petrov@gmail.com")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn.btn-default")
    button.click()

    welcome_text_elt = browser.find_element(By.CSS_SELECTOR, "h1")
    welcome_text = welcome_text_elt.text
    return welcome_text


list1 = "http://suninjuly.github.io/registration1.html"
list2 = "http://suninjuly.github.io/registration2.html"


class Test_UI(unittest.TestCase):
    def test_link1(self):
        self.assertEqual(link_test(list1), "Congratulations! You have successfully registered!")

    def test_link2(self):
        self.assertEqual(link_test(list2), "Congratulations! You have successfully registered!")


if __name__ == "__main__":
    # print(link_test(list1))
    unittest.main()
