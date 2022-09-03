import requests
from enum import Enum
from bs4 import BeautifulSoup

try:
    from urllib import urlencode, urlunsplit
except ImportError:
    from urllib.parse import urlunsplit, urlencode

# Bunch of urls


class eBase(str, Enum):
    URL = "https://www.workatastartup.com"


class eHeaders(dict, Enum):
    PAYLOAD = {"Content-Type": "text/html; charset=UTF-8"}


class eCompanies(str, Enum):
    URL = "/companies"
    # DEMOGRAPHIC_URL = "?demographic"
    # EXPO_URL = "expo"
    # EQUITY_URL = "hasEquity"
    # SALARY_URL = "hasSalary"
    # INDUSTRY_URL = "industry"
    # INTERVIEW_PROCESS_URL = "interviewProcess"
    # JOB_TYPE_URL = "jobType"
    # REMOTE_URL = "remote"
    # SORT_BY_URL = "sortBy"
    # VISA_URL = "usVisaNotRequired"
    # LAYOUT_URL = "layout"


# class eCompany(str, Enum):
#     URL = "companies"


# Helper functions:


def is_companies_search(url):
    return True if (eCompanies.URL in url) and ("=" in url) else False


# def is_company(url):
#     return True if (eCompany.URL in url) and ("=" not in url) else False
