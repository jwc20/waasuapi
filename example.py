import waasu
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


keywords = []

# Log In
# username = "example_username"
# password = "example_password"


options = Options()
# options.add_argument("--headless")
# options.add_argument("--window-size=1980,1020")
# options.add_argument('--disable-gpu')

driver = webdriver.Chrome(options=options)

client = waasu.WorkAtAStartUp().log_in(username=username, password=password, driver=driver, delay=15)

soup = BeautifulSoup(driver.page_source, "lxml")
print(soup.find_all("span", {"class": "company-name hover:underline"}))

# client.get_company_info()
# client.get_companies()
# 
# c_search_url = "https://www.workatastartup.com/companies?demographic=any&expo=any&hasEquity=any&hasSalary=any&industry=any&interviewProcess=any&jobType=any&layout=list-compact&remote=any&sortBy=keyword&usVisaNotRequired=any"
# company_url = "https://www.workatastartup.com/companies/focal-systems"

# print(waasu.is_companies_search(c_search_url)) # => True
# print(waasu.is_company(company_url)) # => True

# print(waasu.is_companies_search(company_url)) # => False
# print(waasu.is_company(c_search_url)) # => False
