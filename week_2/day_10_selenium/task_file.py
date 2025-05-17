# program to automate login in a website using selenium in python
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
from selenium.common.exceptions import NoSuchElementException
import time
driver=webdriver.Chrome()
time.sleep(2)
driver.get('https://www.saucedemo.com/')
driver.find_element(By.NAME,"user-name").send_keys("error_user")
driver.find_element(By.NAME,"password").send_keys("secret_sauce")
driver.find_element(By.NAME,"login-button").click()
time.sleep(10)
try:
    print(driver.find_element(By.CSS_SELECTOR,"div.error-message-container").text)

except NoSuchElementException:
    print("succesfully logined")
driver.close()