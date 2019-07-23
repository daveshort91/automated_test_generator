import requests
import urllib.request
import time
from bs4 import BeautifulSoup
from classwriter import ClassWriter

class Page:
    
    def __init__(self, url, filename, lang, className):
        self.page = urllib.request.urlopen(url)
        self.siteDoc = BeautifulSoup(self.page, 'html.parser')
        self.wfile = ClassWriter(filename, lang)
        self.inputElements = self.siteDoc.find_all('input')
        self.linkElements = self.siteDoc.find_all('a')
        self.write_class(className)

    def write_class(self, className):
        self.wfile.create_file()
        self.wfile.write_packages()
        self.wfile.write_class_header(className)
        self.wfile.write_class_constructor(className)
        self.get_elements()
        self.wfile.write_footer()

    def get_elements(self):
        self.scrape_text_inputs()
        self.scrape_button_inputs()
        self.scrape_radio_buttons()
        self.scrape_submit_inputs()
        self.scrape_links()
        
    def filter_by_type(self, type):
        results = []
        for element in self.inputElements:
            #print(element)
            if (element.get('type') == type):
                results.append(element)
        return results

    def scrape_text_inputs(self): 
        textFields = self.filter_by_type('text')
        ids = self.get_id(textFields)
        self.wfile.format_text_fields(ids)
    
    def scrape_button_inputs(self):
        buttons = self.filter_by_type('button')
        ids = self.get_id(buttons)
        self.wfile.format_buttons(ids)
        
    def scrape_radio_buttons(self):
        radioButtons = self.filter_by_type('radio')
        ids = self.get_id(radioButtons)
        self.wfile.format_radio_buttons(ids)
 
    def scrape_submit_inputs(self):
        submitButtons = self.filter_by_type('submit')
        ids = self.get_id(submitButtons)
        self.wfile.format_submit_buttons(ids)

    def scrape_links(self):
        links = []
        for link in self.linkElements:
            if (link.get('id')):
                string = link.get('id')
                result = string.replace("-", "_") 
                links.append(result)
                
    def get_id(self, elements):
        results = []
        for element in elements:
            if(element.get('id')):
                string = element.get('id')
                result = string.replace("-", "_")
                results.append(result)

        return results
                
    
#test = Page('http://ldsp-pay.ldschurch.org', '/Users/Dave/Documents/Spring 2019/test025')


