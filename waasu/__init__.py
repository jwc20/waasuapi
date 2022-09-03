from .core import *
from .companies import Companies
from .login import LogIn


class WorkAtAStartUp(Companies, LogIn):
    def __init__(self, query=[], *args):
        Companies.__init__(self, query=query, *args)
        LogIn.__init__(self, *args)


__authors__ = ["jwc20"]
__source__ = "https://github.com/jwc20/workatastartup-api"
__license__ = "MIT"
