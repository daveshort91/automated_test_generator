import requests
import urllib.request
import time
from bs4 import BeautifulSoup

#url = input("What is the site url to scrape?")

#url = 'https://plundercomic.com/'
url = 'https://ldsp-pay.ldschurch.org/donations/lds-church/ldsp.html?cde2=795-home&'
response = urllib.request.urlopen(url)

#response = requests.get(url)

print(response)

siteDoc = BeautifulSoup(response, 'html.parser')

#print(siteDoc)

links = siteDoc.find_all('a')


for link in siteDoc.find_all('button'):
    print(link)

