from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

WebDriverWait(driver, 10).until(EC.alert_is_present())

import time
driver=webdriver.Chrome()
driver.get("https://practicetestautomation.com/practice-test-login/")
time.sleep(2)
driver.find_element(By.NAME,"username").send_keys("student")
driver.find_element(By.NAME,"password").send_keys("Password123")

driver.find_element(By.ID,"submit").click()
time.sleep(5)
try:
    print(f"there is a error saying:{driver.find_element(By.ID,"error").text}")
except NoSuchElementException:
    
    h=driver.find_element(By.XPATH,"//h1").text
    p=driver.find_element(By.CSS_SELECTOR,"p.has-text-align-center").text
    print(h)
    print(p)
    time.sleep(5)
    driver.find_element(By.CSS_SELECTOR,"a.wp-block-button__link.has-text-color.has-background.has-very-dark-gray-background-color").click()
time.sleep(3)
driver.close()