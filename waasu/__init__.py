from .core import *
from .companies import Companies
from .company import Company
from .login import LogIn


class WorkAtAStartUp(Companies, Company, LogIn):
    def __init__(self, keywords=[], username="", password="", *args):
        Companies.__init__(self, keywords=keywords, *args)
        Company.__init__(self)
        LogIn.__init__(self, username=username, password=password, *args)


__authors__ = ["jwc20"]
__source__ = "https://github.com/jwc20/workatastartup-api"
__license__ = "MIT"
