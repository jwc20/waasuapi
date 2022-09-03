from .core import *
from collections import namedtuple
import csv
import time

from requests.models import PreparedRequest


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
        role,
        companySize,
    ):



        # if self.query:
        #     print(self.query)
        # else:
        #     print("no query")

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
        p_comp_size = companySize if companySize else "any"
        p_role = role if role else "any"

        p_query = query if query else ""
        # print(p_query)

        
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
                "role",
                "companySize",
            ],
        )
        # Payload order of keys must be same as above namedtuple.
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
            p_role,
            p_comp_size,
        )
        return payload_prep._asdict()

    def _load_page(
        self,
        companySize=None,
        role=None,
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
                role,
                companySize,
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

    @staticmethod
    def _scrape_element_a():
        return

    def get_companies(
        self,
        scroll_delay,
        role=None,
        companySize=None,
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

        # # Get scroll height
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
        sys.stdout.write("\rComplete!                       \n")

        # self._make_companies_url(
        self._load_page(
            role,
            companySize,
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

        print(result)
