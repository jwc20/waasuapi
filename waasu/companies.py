from .core import *
from collections import namedtuple
import csv
import time
import sys


class Companies(object):
    def __init__(self, keywords=[], *args):
        self.keywords = keywords

    def _make_companies_url(
        self,
        p_demo,
        p_expo,
        p_eq,
        p_sal,
        p_ind,
        p_int_proc,
        p_job_type,
        p_rem,
        p_sort_by,
        p_visa,
        p_query,
    ):
        # url = "https://www.workatastartup.com/companies?demographic=any&expo=any&hasEquity=any&hasSalary=any&industry=any&interviewProcess=any&jobType=any&layout=list-compact&remote=any&sortBy=keyword&usVisaNotRequired=any"
        """
        companies?
        demographic=any
        expo=any
        hasEquity=any
        hasSalary=any
        industry=any
        interviewProcess=any
        jobType=any
        layout=list-compact
        remote=any
        sortBy=keyword
        usVisaNotRequired=any
        """

        payload = {}

        if self.keywords:
            print(keywords)
        else:
            print("no keywords")

        return

    @staticmethod
    def _load_page():
        return

    @staticmethod
    def _scrape_element_a():
        return

    def get_companies(
        self,
        client,
        scroll_delay,
        p_demo=None,
        p_expo=None,
        p_eq=None,
        p_sal=None,
        p_ind=None,
        p_int_proc=None,
        p_job_type=None,
        p_rem=None,
        p_sort_by=None,
        p_visa=None,
        p_query=None,
    ):
        # print("hello world")

        # PAYLOAD = {"Content-Type": "text/html; charset=UTF-8"}
        # target_url = url
        # r = requests.get(target_url, headers=PAYLOAD)
        # html = r.text
        # print(html)

        # Get scroll height
        # last_height = client.execute_script("return document.body.scrollHeight")
        #
        # while True:
        #     # Scroll down to bottom
        #     client.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #
        #     # Wait to load page
        #     time.sleep(5)
        #
        #     # Calculate new scroll height and compare with last scroll height
        #     new_height = client.execute_script("return document.body.scrollHeight")
        #     if new_height == last_height:
        #         break
        #     last_height = new_height

        for remaining in range(scroll_delay, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("{:2d} seconds remaining.".format(remaining))
            sys.stdout.flush()
            time.sleep(1)

        sys.stdout.write("\rComplete!            \n")

        result = []
        soup = BeautifulSoup(client.page_source, "lxml")

        self._make_companies_url(
            p_demo,
            p_expo,
            p_eq,
            p_sal,
            p_ind,
            p_int_proc,
            p_job_type,
            p_rem,
            p_sort_by,
            p_visa,
            p_query,
        )

        # get company names
        companies = soup.find_all("span", {"class": "company-name hover:underline"})

        for company in companies:
            result.append(company.text)

        # print(result, len(result))
        return result

        # client.quit()
