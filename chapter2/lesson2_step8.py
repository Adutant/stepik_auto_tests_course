from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from faker import Faker
import os

fake = Faker()


try: 
    link = "https://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    first_name = browser.find_element(By.CSS_SELECTOR, "[name='firstname']")
    last_name = browser.find_element(By.CSS_SELECTOR, "[name='lastname']")
    email = browser.find_element(By.CSS_SELECTOR, "[name='email']")
    file_input = browser.find_element(By.ID, "file")

    first_name.send_keys(fake.first_name())
    last_name.send_keys(fake.last_name())
    email.send_keys(fake.email())

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'file.txt') 
    file_input.send_keys(file_path)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()