import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from classwriter import ClassWriter

class Page:
    url = ""
    wfile = ""
    def __init__(self, siteUrl):
        self.url = siteUrl
        self.wfile = ClassWriter("test")

    def write(self):
        self.wfile.createfile()
        self.wfile.writepackages()
        self.wfile.writeclassheader("Test")
        self.wfile.writefooter()
