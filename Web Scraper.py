import requests
from bs4 import BeautifulSoup

html = requests.get("https://en.wikipedia.org/wiki/Deep_learning")

bsObj=BeautifulSoup(html.content,"html.parser")

print(bsObj.title.string)
file = open('links.txt','w')
for link in bsObj.find_all('a'):#Searching all the links in html
    formattedLink=(str(link.get('href')) + '\n\n') #format a link
    if '/' in formattedLink: #
        if '/wiki/' in formattedLink:
            file.write("https://en.wikipedia.org/" + formattedLink)
        else:
            file.write(formattedLink)



file.close()
