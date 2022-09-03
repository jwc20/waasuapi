import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time


class LogIn(object):
    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = password

    def __init__(self):
        pass

    def log_in(self, username=username, password=password, driver=driver, delay=None):
        options = Options()
        # options.add_argument("--headless")
        # options.add_argument("--window-size=1980,1020")
        # options.add_argument('--disable-gpu')

        driver = webdriver.Chrome(options=options)
        # login_url = "https://account.ycombinator.com/"

        login_url = "https://account.ycombinator.com/?continue=https%3A%2F%2Fwww.workatastartup.com%2F"

        driver.get(login_url)
        time.sleep(2)

        # YCombinator username
        yc_username = driver.find_element_by_css_selector("#ycid-input")
        yc_username.send_keys(username)  # insert self.username here

        # YCombinator password
        yc_password = driver.find_element_by_css_selector("#password-input")
        yc_password.send_keys(password)  # insert self.username here

        submit_button = driver.find_element_by_css_selector(".MuiButton-label")
        submit_button.click()
        # driver.quit()
        if delay is not None:
            time.sleep(delay)
        else:
            time.sleep(10)

        return driver

