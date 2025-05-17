import requests
import csv
from lxml import html
headers = {
    "User-Agent": "Mozilla/5.0",
}
url="https://www.flipkart.com/search?q=iphone"
source=requests.get(url,headers=headers) 
tree = html.fromstring(source.content)
name = tree.xpath("//div[@class='KzDlHZ']/text()")
price=tree.xpath("//div[@class='Nx9bqj _4b5DiR']/text()")
rating= tree.xpath("//div[@class='XQDdHH']/text()")
link=tree.xpath("//a[@class='CGtC98' and @target='_blank' and rel='noopener noreferrer']/@href")
actual_link=url+link[0]
print("the product name is:",name )
print("the price is:",price)
print("the rating of product is:",rating)
print("the link of product is:",actual_link)
with open("udit.csv","w",newline='') as wf:
    csv_writer=csv.writer(wf)

    csv_writer.writerow(['name','price','rating','actual_link'])
    lis=[name,price,rating,actual_line]
    csv_writer.writerow(lis)
# import requests
# import csv
# from lxml import html

# headers = {
#     "User-Agent": "Mozilla/5.0",
# }

# url = "https://www.flipkart.com/search?q=iphone"
# source = requests.get(url, headers=headers)
# tree = html.fromstring(source.content)

# name = tree.xpath("//div[@class='_4rR01T']/text()")
# price = tree.xpath("//div[@class='_30jeq3 _1_WHN1']/text()")
# rating = tree.xpath("//div[@class='_3LWZlK']/text()")
# link = tree.xpath("//a[@class='_1fQZEK']/@href")

# # Joining links properly
# actual_links = ["https://www.flipkart.com" + l for l in link]

# # Showing Clean Output
# for n, p, r, l in zip(name, price, rating, actual_links):
#     print("Name   :", n)
#     print("Price  :", p)
#     print("Rating :", r)
#     print("Link   :", l)
#     print('-' * 50)

# # Writing to CSV
# with open("udit.csv", "w", newline='', encoding='utf-8') as wf:
#     csv_writer = csv.writer(wf)
#     csv_writer.writerow(['Name', 'Price', 'Rating', 'Link'])
    
#     for n, p, r, l in zip(name, price, rating, actual_links):
#         csv_writer.writerow([n, p, r, l])
# print(name, price, rating, actual_links)