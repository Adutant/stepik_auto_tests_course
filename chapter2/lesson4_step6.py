from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "https://suninjuly.github.io/cats.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.ID, "button")

finally:
    # закрываем браузер после всех манипуляций
    browser.quit()