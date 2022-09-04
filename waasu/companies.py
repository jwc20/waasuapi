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
        p_expo = ("expo", expo) if expo else ("expo", "any")
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
        p_layout = ("layout", "list")  # don't change

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
                if isinstance(payload_list[i][1], list) and len(payload_list[i][1]) > 1:
                    payload.append((payload_list[i][0], payload_list[i][1][j]))

            if isinstance(payload_list[i][1], list) and len(payload_list[i][1]) == 1:
                # Note: need to do something different for query
                payload.append((payload_list[i][0], payload_list[i][1][0]))

            elif isinstance(payload_list[i][1], str):
                payload.append((payload_list[i][0], payload_list[i][1]))

        # print(payload_list)
        # breakpoint()
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
        print(target_url)
        delay_timer("making url...", "done", 10)

    def _scrape_companies(self, soup_data):
        result = []
        directory_list = soup_data.find("div", {"class": "directory-list list-compact"})
        companies = directory_list.find_all("div", {"class":"bg-beige-lighter border border-gray-200 rounded mb-5 pb-6"})

        for company in companies:
            d = {}
            company_name = company.find(
                "span", {"class": "company-name hover:underline"}
            )
            d["name"] = company_name.text

            details = company.find(
                "div", {"class": "flex flex-wrap gap-1 sm:gap-3 whitespace-nowrap"}
                ).find_all("div", {"class": "flex text-gray-600 border px-2 rounded"})

            d["location"] = details[0].find("div", {"class": "detail-label"}).text
            d["size"] = details[1].find("div", {"class": "detail-label"}).text.strip()
            # d["tag1"] = details[2].find("div", {"class": "detail-label"}).text if details[2] else None
            # d["tag2"] = details[3].find("div", {"class": "detail-label"}).text if details[3] else None

            d["waasu_url"] = eBase.URL + company.a['href']
            d["company_url"] = company.find("div", {"class": "hidden sm:flex mt-4 sm:w-1/5"}).a.text




            # company_founders =  company.find("div", {"class": "sm:col-span-11"}).find_all("div", {"class":"font-medium"})
            # d["founders"]=  [company_founder.text for company_founder in company_founders]
            # d["about"] =  company.find("div", {"class": "mx-5 prose max-w-none col-span-11"}).p.text
            # d["tech"] = company.find_next("div", {"class": "mx-5 prose max-w-none col-span-11"}).p.text

            more_details = company.find("div", {"class":"flex"}).next_sibling.next_sibling 
            company_founders = more_details.div.find_all("div", {"class":"font-medium"})
            d["founders"]=  [company_founder.text for company_founder in company_founders[1:]]
            if more_details.find("div").find_next_sibling("div").p is not None:
                d["about"] =  more_details.find("div").find_next_sibling("div").p.text

            if more_details.find("div").find_next_sibling("div").find_next_sibling("div").p is not None:
                d["tech"] = more_details.find("div").find_next_sibling("div").find_next_sibling("div").p.text 
            # breakpoint()


            company_jobs = company.find("div", {"class": "w-full"}).find_all("div", {"class":"flex justify-between"})
            jobs = []

            for job in company_jobs:
                company_job = {}
                company_job["job_name"] = job.find("div", {"class":"w-full sm:w-9/10 mb-4"}).a.text
                company_job["job_url"] = job.find("div", {"class":"flex-none my-auto"}).a["href"]
                job_details = job.find("div", {"class":"sm:flex sm:flex-wrap text-sm mr-2 sm:mr-3"}).find_all("span")
                job_details_texts = [job_detail.text for job_detail in job_details]
                job_details_text = ' '.join(job_details_texts)
                company_job["details"] = job_details_text
                jobs.append(company_job)

            d["jobs"] = jobs
            result.append(d)

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

        delay_timer("prepping to scrape...", "done", scroll_delay)

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
