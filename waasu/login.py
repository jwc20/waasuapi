import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time
from .core import * 

# login_url = "https://account.ycombinator.com/"
login_url = (
    "https://account.ycombinator.com/?continue=https%3A%2F%2Fwww.workatastartup.com%2F"
)


class LogIn(object):
    def __init__(self):
        pass

    def log_in(self, username, password, scroll_delay=None):
        # driver = self._set_driver()
        self.driver.get(login_url)
        # time.sleep(5)
        delay_timer("waiting for login page...", "login page loaded", 3)


        # YCombinator username
        yc_username = self.driver.find_element_by_css_selector("#ycid-input")
        yc_username.send_keys(username)  # insert self.username here

        # YCombinator password
        yc_password = self.driver.find_element_by_css_selector("#password-input")
        yc_password.send_keys(password)  # insert self.username here

        submit_button = self.driver.find_element_by_css_selector(".MuiButton-label")
        submit_button.click()
        # time.sleep(5)
        delay_timer("logging in...", "logged in",  5)

        # driver.quit()
