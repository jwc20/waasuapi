import requests
from bs4 import BeautifulSoup



from selenium.webdriver.common.keys import Keys
import time


class LogIn(object):
    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = password

    def __init__(self):
        pass

    def log_in(self, username, password, driver, delay=None):
        login_url = "https://account.ycombinator.com/?continue=https%3A%2F%2Fwww.workatastartup.com%2F"

        driver.get(login_url)
        time.sleep(2)

        # YCombinator username
        yc_username = driver.find_element_by_css_selector("#ycid-input")
        yc_username.send_keys(username)  # insert username here

        # YCombinator password
        yc_password = driver.find_element_by_css_selector("#password-input")
        yc_password.send_keys(password)  # insert username here

        submit_button = driver.find_element_by_css_selector(".MuiButton-label")
        submit_button.click()


        if(delay is not None): time.sleep(delay) # Must set a time to quit the browser
        else: time.sleep(10)

        # print("hellow asdijaisdl")

        # soup = BeautifulSoup(driver.page_source, "lxml")
        # print(soup.find_all("span", {"class": "company-name hover:underline"}))
