from bs4 import BeautifulSoup
import requests
file=open(r"C:\Users\udit2\Desktop\udit.txt",'w',encoding="utf-8")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
}
source=requests.get("https://www.thehindu.com/",headers=headers).text
soup=BeautifulSoup(source,'lxml')
count=1
for i in ['h1','h2','h3','h4','h5','h6']:
    artic=soup.find_all(i)
    for article in artic:
        if article:
            article=article.text
            # print(article)
            file.write(str(count)+".]"+article.strip()+"\n")
            count+=1
           
file.close()