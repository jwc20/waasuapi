from .core import *
from collections import namedtuple
import csv


class Company(object):
    def __init__(self, keywords=[], *args):
        self.keywords = keywords

    @staticmethod
    def _make_url():
        return

    @staticmethod
    def _load_page():
        return

    @staticmethod
    def _scrape_element_a():
        return


    def get_company_info(self):
        print("hello from company class")
        return
