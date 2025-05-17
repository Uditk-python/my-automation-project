from selenium import webdriver
# from selenium.webdriver.common.keys import keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
driver=webdriver.Chrome()
with open("udit.txt","w",encoding="utf-8") as wf:
    for i in range(1,4):
        query="men watch"
        driver.get(f"https://www.amazon.in/s?k={query}&page={i}&xpid=YQW1510Tgg95c&crid=1WH558AEHBCL0&qid=1744203164&sprefix=laptop%2Caps%2C302&ref=sr_pg_2")
        elems=driver.find_elements(By.CLASS_NAME, "puis-card-container")
        for elem in elems:
            # print(elem.text) 
            name=elem.find_element(By.CSS_SELECTOR,"h2").text
            price=elem.find_element(By.CSS_SELECTOR,"span.a-price-whole").text
            element=elem.find_element(By.CSS_SELECTOR,"a")
            link=element.get_attribute('href')
            actual_link="https://www.amazon.com"+link

            wf.write(name+"-"+price+link)
            wf.write("\n")
            break
    # # print(elem.text)
driver.close()