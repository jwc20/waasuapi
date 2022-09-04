from .core import *
from collections import namedtuple, defaultdict
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
        layout,
    ):

        p_demo = ("demographic", demographic) if demographic else ("demographic", "any")
        p_expo = ("expo", expo) if expo else ("expo", expo)
        p_eq = ("hasEquity", hasEquity) if hasEquity else ("hasEquity", "any")
        p_sal = ("hasSalary", hasSalary) if hasSalary else ("hasSalary", "any")
        p_ind = ("industry", industry) if industry else ("industry", "any")
        p_int_proc = (
            ("interviewProcess", interviewProcess)
            if interviewProcess
            else ("interviewProcess", "any")
        )
        p_job_type = ("jobType", jobType) if jobType else ("jobType", "any")
        p_remote = ("remote", remote) if remote else ("remote", "any")
        p_sort_by = ("sortBy", sortBy) if sortBy else ("sortBy", "any")
        p_visa = (
            ("usVisaNotRequired", usVisaNotRequired)
            if usVisaNotRequired
            else ("usVisaNotRequired", "any")
        )
        p_query = ("query", query) if query else ("query", "")
        p_role = ("role", role) if role else ("role", "any")
        p_comp_size = (
            ("companySize", companySize) if companySize else ("companySize", "any")
        )
        p_layout = ("list", "list")  # don't change

        payload_list = [
            p_demo,
            p_expo,
            p_eq,
            p_sal,
            p_ind,
            p_int_proc,
            p_job_type,
            p_remote,
            p_sort_by,
            p_visa,
            p_query,
            p_role,
            p_comp_size,
            p_layout,
        ]

        payload = []

        # naive approach, use double loop
        for i in range(len(payload_list)):
            for j in range(len(payload_list[i])):
                # if (isinstance(payload_list[i][1], list)) and (len(payload_list[i][1]) > 1):
                if isinstance(payload_list[i][1], list):
                    # if (payload_list[i][1] != "any") or (payload_list[i][1] != ""):
                    payload.append((payload_list[i][0], payload_list[i][1][j]))
            if isinstance(payload_list[i][1], str):
                payload.append((payload_list[i][0], payload_list[i][1]))

            # elif len(payload_list[i]) == 1:
            #     payload.add(payload_list[i][0])

        print(payload_list)

        return payload

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
        role=None,
        companySize=None,
        layout=None,
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
                role,
                companySize,
                layout,
            ),
            safe="%20",
        )

        target_url = filter_url + "?" + payload_str
        self.driver.get(target_url)
        delay_timer("making url...", "done", 10)

    def _scrape_companies(self, soup_data):
        # get company names
        companies_span = soup_data.find_all(
            "span", {"class": "company-name hover:underline"}
        )

        result = []
        for span in companies_span:
            if span.parent.parent.parent.find("span", {"class": "text-sm w-full text-orange-500 text-right pr-5 italic"}):
                continue
            result.append(span.text)

        print(result)

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
        role=None,
        companySize=None,
        layout=None,
    ):


        delay_timer("waiting for page to load...", "done", scroll_delay)

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
            role,
            companySize,
            layout,
        )
        

        ###########################################################
        # Scroll all the way to the bottom
        # # Get scroll height
        # last_height = self.driver.execute_script("return document.body.scrollHeight")

        # while True:
        #     # Scroll down to bottom
        #     self.driver.execute_script(
        #         "window.scrollTo(0, document.body.scrollHeight);"
        #     )

        #     # Wait to load page
        #     time.sleep(5)

        #     # Calculate new scroll height and compare with last scroll height
        #     new_height = self.driver.execute_script("return document.body.scrollHeight")
        #     if new_height == last_height:
        #         break
        #     last_height = new_height

        # for remaining in range(scroll_delay, 0, -1):
        #     sys.stdout.write("\r")
        #     sys.stdout.write("{:2d} seconds remaining.".format(remaining))
        #     sys.stdout.flush()
        #     time.sleep(1)
        # sys.stdout.write("\rComplete!                       \n")
        ###########################################################

        
        soup = BeautifulSoup(self.driver.page_source, "lxml")
        self._scrape_companies(soup)


        # companies_span = soup.find_all(
        #     "span", {"class": "company-name hover:underline"}
        # )

        # result = []
        # for span in companies_span:
        #     if span.find("span", {"class": "text-sm w-full text-orange-500 text-right pr-5 italic"}):
        #         pass
        #     result.append(span.text)

        # print(result)

