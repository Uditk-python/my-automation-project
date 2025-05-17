from bs4 import BeautifulSoup
import csv
import requests
# url=input("Enter the url of the website")
wf=open("scrap_data.csv",'w') 
csv_writer=csv.writer(wf)
csv_writer.writerow(["title","paragragh","link"])
source=requests.get("https://www.scrapethissite.com/pages/?utm_source=chatgpt.com").text
soup=BeautifulSoup(source,'lxml')
# print(soup.prettify())
# tit
# article=soup.find_all("div",class_="page")
# print(article)
ariv=soup.find_all("div",class_="page")
for k in ariv:
    l=k.h3.text
    p=k.p.text
    link=k.a["href"]
    # print(l,p.strip(),link)
    print()
    csv_writer.writerow([l.strip(),p.strip(),link.strip()])
wf.close
# artice=article.h3.text
# summary=article.p.text
# for atic in article:
#     print(atic)
# print(artice)
# print(summary)
# from selenium import webdriver

# # Initialize the browser (use Chrome or Edge)
# driver = webdriver.Chrome()
# driver.get("https://www.scrapethissite.com/pages/?utm_source=chatgpt.com")

# # Get the fully rendered page source
# html = driver.page_source

# # Parse with BeautifulSoup
# soup = BeautifulSoup(html, "lxml")
# print(soup.prettify())

# # Close the browser
# driver.quit()