import requests
from enum import Enum
from bs4 import BeautifulSoup
import sys
import time

try:
    from urllib import urlencode, urlunsplit
except ImportError:
    from urllib.parse import urlunsplit, urlencode


class eBase(str, Enum):
    URL = "https://www.workatastartup.com"


class eHeaders(dict, Enum):
    PAYLOAD = {"Content-Type": "text/html; charset=UTF-8"}


class eCompanies(str, Enum):
    URL = "/companies"


# Helper functions:
def is_companies_search(url):
    return True if (eCompanies.URL in url) and ("=" in url) else False
