from .core import *
from .companies import Companies
from .login import LogIn

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

# Define Chrome options
options = Options()
# options.add_argument("--headless")  # Enable headless mode
# options.add_argument("--window-size=500,1020")  # Uncomment if you need a specific window size
# options.add_argument('--disable-gpu')  # Recommended for headless mode, though may become unnecessary in future versions

class WorkAtAStartUp(Companies, LogIn):
    def __init__(self, **kwargs):
        # Initialize webdriver with options using webdriver-manager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
        Companies.__init__(self, **kwargs)
        LogIn.__init__(self)



__authors__ = ["jwc20"]
__source__ = "https://github.com/jwc20/workatastartup-api"
__license__ = "MIT"
