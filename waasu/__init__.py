from .core import *
from .companies import Companies
from .login import LogIn

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

# Define Chrome options
options = Options()
options.add_argument("--headless")  # Enable headless mode
# options.add_argument("--window-size=500,1020")  # Uncomment if you need a specific window size
# options.add_argument('--disable-gpu')  # Recommended for headless mode, though may become unnecessary in future versions
# options.add_argument("--user-data-dir=chrome-data")  # TODO: save cookies

class WorkAtAStartUp(Companies, LogIn):
    def __init__(self, **kwargs):
        # Initialize webdriver with options
        # Specify the path to your ChromeDriver executable
        chrome_driver_path = '/usr/bin/chromedriver-linux64/chromedriver'
        self.driver = webdriver.Chrome(service=Service(chrome_driver_path), options=options)
        Companies.__init__(self, **kwargs)
        LogIn.__init__(self)


__authors__ = ["jwc20"]
__source__ = "https://github.com/jwc20/workatastartup-api"
__license__ = "MIT"
