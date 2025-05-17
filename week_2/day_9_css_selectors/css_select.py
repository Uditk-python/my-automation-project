import requests
from lxml import html

with open("udit.txt", 'w', encoding="utf-8") as file:
    source = requests.get("http://books.toscrape.com/")
    tree = html.fromstring(source)
    helo = tree.xpath("//article//a/@href")
    for n in helo:
        # n = li.text_content().strip()
        if n:
            # cleaned_line = " ".join(n.split() )  # Removes extra spaces, joins into a clean line
            file.write(n.strip() + "\n")