import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
from .core import *  # Ensure this import is correct based on your project structure

login_url = (
    "https://account.ycombinator.com/?continue=https%3A%2F%2Fwww.workatastartup.com%2F"
)

class LogIn(object):
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def log_in(self, username, password, scroll_delay=None):
        self.driver.get(login_url)
        # Replace delay_timer with explicit time.sleep for simplicity, unless it's a defined method elsewhere
        # delay_timer("waiting for login page...", "login page loaded", 3)
        time.sleep(3)  # Adjust time as necessary

        # YCombinator username
        yc_username = self.driver.find_element("css selector", "#ycid-input")
        yc_username.send_keys(username)

        # YCombinator password
        yc_password = self.driver.find_element("css selector", "#password-input")
        yc_password.send_keys(password)

        submit_button = self.driver.find_element("css selector", ".MuiButton-label")
        submit_button.click()
        # delay_timer("logging in...", "logged in",  5)
        time.sleep(5)  # Adjust time as necessary

        # Consider adding driver.quit() here or manage driver's lifecycle outside this method

# Example usage:
# login = LogIn()
# login.log_in('your_username', 'your_password')

