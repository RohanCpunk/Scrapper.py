from urllib import response
from bs4 import BeautifulSoup
import requests
import re , csv

def getHTMLdocument(url):
    response = requests.get(url)
    return response.text

#url = "https://www.uber.com"
url = "https://www.hackingarticles.in/page/12/"
html_document = getHTMLdocument(url) #Create Document
soup = BeautifulSoup(html_document, 'html.parser')

for link in soup.find_all('a', attrs={'href':re.compile("^https://")}):
    print(link.get('href'))

     #with open("C:\Users\91886\Desktop\Python\Parser\link.txt""ab") as l:
         #l.write(link.get('href'))
    # with open('link.csv', 'w', newline='') as f:
    #     fields = ['Material']
    #     writer = csv.DictWriter(f, fieldnames=link)
    #     writer.writeheader()
    # writer.writerows(link.get('href'))
    
    
    
