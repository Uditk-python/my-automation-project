import requests
import csv
from bs4 import BeautifulSoup
wf=open("udit.csv","w",newline='',encoding='utf-8')
csv_writer=csv.writer(wf)
csv_writer.writerow(['name','price','rating','actual_link'])
headers = {
    "User-Agent": "Mozilla/5.0",
}
url = "https://www.flipkart.com/search?q=iphone"
base_url = "https://www.flipkart.com"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.content, 'lxml')
all_product = soup.select('div.KzDlHZ')
if len(all_product)>0:
    for product in all_product:
        NAME=product.text
        parent = product.find_parent().find_parent()
        Price = parent.select_one('div.Nx9bqj._4b5DiR').text
        rating = parent.select_one('div.XQDdHH').text
        element = parent.select_one('a[href]')['href']
        actual_link = base_url+element
        print("the product name is:",NAME )
        print("the price is:",Price)
        print("the rating of product is:",rating)
        print("the link of product is:",actual_link)


        lis=[NAME,Price,rating,actual_link]
        csv_writer.writerow(lis)
else:
    print("the page is empty")
wf.close
import os
import pandas as pd
if os.path.exists("udit.csv"):
    udit=pd.read_csv("udit.csv")
    udit.to_excel("hello.xlsx",index=False)

# import requests
# import csv
# from bs4 import BeautifulSoup
# import os
# import pandas as pd

# wf = open("udit.csv", "w", newline='', encoding='utf-8')
# csv_writer = csv.writer(wf)
# csv_writer.writerow(['name', 'price', 'rating', 'actual_link'])

# headers = {
#     "User-Agent": "Mozilla/5.0",
# }

# url = "https://www.flipkart.com/search?q=iphone"
# base_url = "https://www.flipkart.com"

# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.content, 'lxml')

# all_product = soup.select('div.KzDlHZ')

# if len(all_product) > 0:
#     for product in all_product:
#         NAME = product.text
#         parent = product.find_parent().find_parent()

#         Price = parent.select_one('div.Nx9bqj._4b5DiR')
#         rating = parent.select_one('div.XQDdHH')
#         element = parent.find('a', href=True)

#         Price = Price.text if Price else "No Price"
#         rating = rating.text if rating else "No Rating"
#         link = element['href'] if element else "No Link"
#         actual_link = base_url + link if element else "No Link Found"

#         print("Name:", NAME)
#         print("Price:", Price)
#         print("Rating:", rating)
#         print("Link:", actual_link)
#         print("-" * 50)

#         lis = [NAME, Price, rating, actual_link]
#         csv_writer.writerow(lis)
# else:
#     print("The page is empty")

# wf.close()

# if os.path.exists("udit.csv"):
#     udit = pd.read_csv("udit.csv")
#     udit.to_excel("hello.xlsx", index=False)