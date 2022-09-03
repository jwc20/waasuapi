from .core import *
from collections import namedtuple
import csv
import time
import sys
from requests.models import PreparedRequest

# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.keys import Keys


class Companies(object):
    def __init__(self, query=[], *args):
        self.query = query

    def _make_companies_url(
        self,
        demographic,
        expo,
        hasEquity,
        hasSalary,
        industry,
        interviewProcess,
        jobType,
        remote,
        sortBy,
        usVisaNotRequired,
        query,
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
        layout=list
        remote=any
        sortBy=keyword
        usVisaNotRequired=any
        """

        # payload = {}
        Payload = namedtuple(
            "Payload",
            [
                "demographic",
                "expo",
                "hasEquity",
                "hasSalary",
                "industry",
                "interviewProcess",
                "jobType",
                "layout",
                "remote",
                "sortBy",
                "usVisaNotRequired",
                "query",
            ],
        )

        if self.query:
            print(self.query)
        else:
            print("no query")

        p_demo = demographic if demographic else "any"
        p_expo = expo if expo else "any"
        p_exq = hasEquity if hasEquity else "any"
        p_sal = hasSalary if hasSalary else "any"
        p_ind = industry if industry else "any"
        p_int_proc = interviewProcess if interviewProcess else "any"
        p_job_type = jobType if jobType else "any"
        p_layout = "list"  # don't change
        p_remote = remote if remote else "any"
        p_sort_by = sortBy if sortBy else "any"
        p_visa = usVisaNotRequired if usVisaNotRequired else "any"
        p_query = query if query else ""
        print(p_query)

        payload_prep = Payload(
            p_demo,
            p_expo,
            p_exq,
            p_sal,
            p_ind,
            p_int_proc,
            p_job_type,
            p_layout,
            p_remote,
            p_sort_by,
            p_visa,
            p_query,
        )

        # print(filter_url, pay.demographic)

        return payload_prep._asdict()

    def _load_page(
        self,
        demographic=None,
        expo=None,
        hasEquity=None,
        hasSalary=None,
        industry=None,
        interviewProcess=None,
        jobType=None,
        remote=None,
        sortBy=None,
        usVisaNotRequired=None,
        query=None,
    ):
        filter_url = eBase.URL + eCompanies.URL
        payload_str = urlencode(
            self._make_companies_url(
                demographic,
                expo,
                hasEquity,
                hasSalary,
                industry,
                interviewProcess,
                jobType,
                remote,
                sortBy,
                usVisaNotRequired,
                query,
            ),
            safe="%20",
        )

        target_url = filter_url + "?" + payload_str
        self.driver.get(target_url)
        time.sleep(10)
        # html = r.page_source
        # return BeautifulSoup(html, "lxml")

    @staticmethod
    def _scrape_element_a():
        return

    def get_companies(
        self,
        scroll_delay,
        demographic=None,
        expo=None,
        hasEquity=None,
        hasSalary=None,
        industry=None,
        interviewProcess=None,
        jobType=None,
        remote=None,
        sortBy=None,
        usVisaNotRequired=None,
        query=None,
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

        # self._make_companies_url(
        self._load_page(
            demographic,
            expo,
            hasEquity,
            hasSalary,
            industry,
            interviewProcess,
            jobType,
            remote,
            sortBy,
            usVisaNotRequired,
            query,
        )


        soup = BeautifulSoup(self.driver.page_source, "lxml")


        # get company names
        companies_span = soup.find_all(
            "span", {"class": "company-name hover:underline"}
        )

        result = []
        for span in companies_span:
            result.append(span.text)

        # companies_div = page.find_all("div", {"class": "company-details text-lg"})
        # result_div = []
        # for div in companies_div:
        #     result_div.append(div.text)

        # print(result_div)
        print(result)


        # print(result, len(result))
        # return result

        # client.quit()
