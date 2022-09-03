from .core import *
from collections import namedtuple
import csv
import time


class Companies(object):
    def __init__(self, keywords=[], *args):
        self.keywords = keywords

    @staticmethod
    def _make_url():
        return

    @staticmethod
    def _load_page():
        return

    @staticmethod
    def _scrape_element_a():
        return

    def get_companies(self, client, delay):
        # print("hello world")
        # url = "https://www.workatastartup.com/companies?demographic=any&expo=any&hasEquity=any&hasSalary=any&industry=any&interviewProcess=any&jobType=any&layout=list-compact&remote=any&sortBy=keyword&usVisaNotRequired=any"
        # PAYLOAD = {"Content-Type": "text/html; charset=UTF-8"}
        # target_url = url
        # r = requests.get(target_url, headers=PAYLOAD)
        # html = r.text
        # print(html)

        # Get scroll height
        last_height = client.execute_script("return document.body.scrollHeight")
        
        while True:
            # Scroll down to bottom
            client.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        
            # Wait to load page
            if delay is not None:
                time.sleep(delay)
            else:
                time.sleep(10)
        
            # Calculate new scroll height and compare with last scroll height
            new_height = client.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height



        result = []
        soup = BeautifulSoup(client.page_source, "lxml")
        companies = soup.find_all("span", {"class": "company-name hover:underline"})

        for company in companies:
            result.append(company.text)

        print(result, len(result))

