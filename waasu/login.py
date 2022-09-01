import requests
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# import selenium

class LogIn(object):
    # def __init__(self, username, password):
    #     self.username = username
    #     self.password = password

    def __init__(self):
        pass

    @staticmethod
    def _load_page():
        pass

    @staticmethod
    def _pick_form(soup_data):
        pass

    def log_in(self):
        print("hello from login page")
        options = Options()
        options.add_argument("--headless")
        options.add_argument("--window-size=1980,1020")
        options.add_argument('--disable-gpu')
        
        driver = webdriver.Chrome(options=options)
        driver.get('http://www.google.com/');
        time.sleep(5) # Let the user actually see something!
        search_box = driver.find_element_by_name('q')
        search_box.send_keys('ChromeDriver')
        search_box.submit()
        time.sleep(5) # Let the user actually see something!
        print("reached the end")
        driver.quit()


if __name__ == "__main__":
    LogIn().log_in()
