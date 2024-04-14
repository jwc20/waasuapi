from .core import *
from collections import namedtuple, defaultdict
import csv
import time
import json

from requests.models import PreparedRequest
from pprintpp import pprint

from datetime import datetime

now = datetime.now()

date_time_format = now.strftime("%Y-%m-%d_%H-%M-%S")


class Companies(object):
    def __init__(self, query=[], *args):
        self.query = query

    def _make_companies_url(
        self,
        minExperience,
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
        p_minExperience = (
            ("minExperience", minExperience)
            if minExperience
            else (
                "minExperience",
                "any",
            )
        )
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
            p_minExperience,
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

        for i in range(len(payload_list)):
            if isinstance(payload_list[i][1], list) and len(payload_list[i][1]) > 1:
                for j in range(len(payload_list[i][1])):
                    payload.append((payload_list[i][0], payload_list[i][1][j]))

            if isinstance(payload_list[i][1], list) and len(payload_list[i][1]) == 1:
                payload.append((payload_list[i][0], payload_list[i][1][0]))

            elif isinstance(payload_list[i][1], str):
                payload.append((payload_list[i][0], payload_list[i][1]))
        pprint(payload)
        return payload

    def _load_page(
        self,
        minExperience=None,
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
                minExperience,
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
        pprint(target_url)
        delay_timer("prepping to scrape...", "done", 10)

    def _scrape_companies(self, soup_data):
        result = []
        directory_list = soup_data.find("div", {"class": "directory-list list-compact"})
        # pprint(directory_list)
        companies = directory_list.find_all(
            "div",
            {"class": "bg-beige-lighter border border-gray-200 mb-5 rounded pb-4"},
        )
        # pprint(companies)

        for company in companies:
            d = {}
            company_name = company.find(
                "span", {"class": "company-name hover:underline"}
            )
            d["name"] = company_name.text

            details = company.find(
                "div", {"class": "flex flex-wrap gap-1 whitespace-nowrap sm:gap-3"}
            ).find_all(
                "div",
                {"class": "flex items-center rounded border px-2 py-1 text-gray-600"},
            )

            # pprint(details)

            d["location"] = details[0].find("div", {"class": "detail-label"}).text
            # d["size"] = details[1].find("div", {"class": "detail-label"}).text.strip()
            d["waasu_url"] = eBase.URL + company.a["href"]

            # breakpoint()

            d["company_url"] = company.find(
                "div", {"class": "text-blue-600 ellipsis"}
            ).a.text

            more_details = company.find(
                "div", {"class": "flex"}
            ).next_sibling.next_sibling

            company_founders = more_details.div.find_all(
                "div", {"class": "font-medium"}
            )

            d["founders"] = [
                company_founder.text.strip() for company_founder in company_founders[1:]
            ]
            if more_details.find("div").find_next_sibling("div") is not None:
                d["about"] = (
                    more_details.find("div")
                    .find_next_sibling("div")
                    .text[5:]
                    .replace("\n", " ")
                    .strip()
                )

            # pprint(more_details)
            # breakpoint()

            # if (
            #     more_details.find("div")
            #     .find_next_sibling("div")
            #     .find_next_sibling("div")
            #     is not None
            # ):
            #     d["tech"] = (
            #         more_details.find("div")
            #         .find_next_sibling("div")
            #         .find_next_sibling("div")
            #         .text[4:]
            #         .replace("\n", " ")
            #         .strip()
            #     )

            first_div = more_details.find("div")
            if first_div is not None:
                second_div = first_div.find_next_sibling("div")
                if second_div is not None:
                    third_div = second_div.find_next_sibling("div")
                    if third_div is not None:
                        d["tech"] = third_div.text[4:].replace("\n", " ").strip()

            company_jobs = company.find("div", {"class": "w-full"}).find_all(
                "div", {"class": "mb-4 flex flex-col justify-between sm:flex-row"}
            )
            jobs = []
            # breakpoint()

            for job in company_jobs:
                company_job = {}
                company_job["job_name"] = job.find(
                    "div", {"class": "sm:w-9/10 w-full"}
                ).a.text

                # breakpoint()

                company_job["job_url"] = job.find("div", {"class": "job-name"}).a[
                    "href"
                ]

                job_details = job.find(
                    "div", {"class": "mr-2 text-sm sm:mr-3 sm:flex sm:flex-wrap"}
                ).find_all("span")
                job_details_texts = [job_detail.text for job_detail in job_details]
                job_details_text = " ".join(job_details_texts)
                company_job["details"] = job_details_text
                # print(company_job)
                jobs.append(company_job)

            d["jobs"] = jobs
            # print(d)
            result.append(d)
        # pprint(result)
        return result

    def _save_to_csv(self, data, filename):
        keys = data[0].keys() if data else []
        with open(filename, "w", newline="", encoding="utf-8") as output_file:
            dict_writer = csv.DictWriter(output_file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(data)
            print(f"Data successfully written to {filename}")

    def get_companies(
        self,
        scroll_delay,
        minExperience=None,
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

        delay_timer("prepping to url...", "url prepped", scroll_delay)

        self._load_page(
            minExperience,
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
        # Get scroll height
        last_height = self.driver.execute_script("return document.body.scrollHeight")

        while True:
            # Scroll down to bottom
            self.driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);"
            )

            # Wait to load page
            time.sleep(5)

            # Calculate new scroll height and compare with last scroll height
            new_height = self.driver.execute_script("return document.body.scrollHeight")
            if new_height == last_height:
                break
            last_height = new_height

        for remaining in range(scroll_delay, 0, -1):
            sys.stdout.write("\r")
            sys.stdout.write("{:2d} seconds remaining.".format(remaining))
            sys.stdout.flush()
            time.sleep(1)
        sys.stdout.write("\rComplete!                       \n")
        ###########################################################

        soup = BeautifulSoup(self.driver.page_source, "lxml")
        results = self._scrape_companies(soup)

        # pprint(results)

        filename = f"data_{date_time_format}.json"

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(results, f, ensure_ascii=False, indent=4)

        csv_filename = f"data_{date_time_format}.csv"
        self._save_to_csv(results, csv_filename)
