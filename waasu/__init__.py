from .core import *
from .companies import Companies
from .company import Company


class WorkAtAStartUp(Companies, Company):
    def __init__(self, keywords=[], *args):
        Companies.__init__(self, keywords=keywords, *args)
        Company.__init__(self)


__authors__ = ["jwc20"]
__source__ = "https://github.com/jwc20/workatastartup-api"
__license__ = "MIT"

__all__ = [""]
