import pandas as pd
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
# driver=webdriver.Chrome()
import time
import csv
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("start-maximized")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64)...")

driver = webdriver.Chrome(options=options)
with open("udit.csv","w",encoding="utf-8") as wf:
    o=csv.writer(wf)
    o.writerow(['name','price','img','link'])
    for i in range(1,5):
        driver.get(f"https://www.amazon.in/s?k=watch&page={i}&crid=294W2WBPCWZHG&qid=1747412819&sprefix=watch%2Caps%2C539&xpid=epoJLnz-E7VVQ&ref=sr_pg_{i}")
        time.sleep(2)
        elems=driver.find_elements(By.CLASS_NAME, "a-section.a-spacing-base")
        for element in elems:
            name=element.find_elements(By.CSS_SELECTOR,"h2")

            try:
                name=name[len(name)-1].text
            except:
                name="NA"
            try:
                price=element.find_element(By.CSS_SELECTOR,"span[aria-hidden='true']").text
            except:
                price="NA"
            try:
                img_element=element.find_element(By.CSS_SELECTOR,"img.s-image")
                source=img_element.get_attribute("src")
            except:
                source="NA"
            try:
                link=element.find_element(By.CSS_SELECTOR,"a")
                link=link.get_attribute("href")
            except:
                link="NA"
            # print(name,price,source,link)
            o.writerow([name,price,source,link])
driver.quit()
if os.path.exists("udit.csv"):
    udit=pd.read_csv("udit.csv")
    udit.to_excel("watch.xlsx",index=False)