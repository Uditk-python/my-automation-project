from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.service import Service
from selenium.common.exceptions import NoSuchElementException
import time
driver=webdriver.Chrome()
# time.sleep(2)
driver.get('https://www.techlistic.com/p/selenium-practice-form.html')
driver.find_element(By.NAME,"firstname").send_keys("hello")
driver.find_element(By.NAME,"lastname").send_keys("hell")
exp_button = driver.find_element(By.ID, "exp-2")
driver.execute_script("arguments[0].scrollIntoView();", exp_button)
exp_button.click()
driver.find_element(By.ID,"sex-0").click()
driver.find_element(By.ID,"datepicker").send_keys("23/12/24")
driver.find_element(By.ID,"profession-0").click()
driver.find_element(By.ID,"tool-1").click()
driver.find_element(By.XPATH,"//select/option[text()='Europe']").click()
driver.find_element(By.XPATH,"//select/option[text()='Navigation Commands']").click()
driver.find_element(By.CSS_SELECTOR,"input.input-file").send_keys(r"C:\Users\udit2\Pictures\nit2.jpg")
driver.find_element(By.CSS_SELECTOR,"button.btn.btn-info").click()
time.sleep(5)
driver.close()
