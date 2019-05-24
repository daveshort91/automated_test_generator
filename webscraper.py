import requests
import urllib.request
import time
from bs4 import BeautifulSoup

# url = input("What is the site url to scrape?")

url = 'https://plundercomic.com/'

response = requests.get(url)

print(response)
