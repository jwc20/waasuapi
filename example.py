import waasu

client = waasu.WorkAtAStartUp()

client.get_scraped_companies()

c_search_url = "https://www.workatastartup.com/companies?demographic=any&expo=any&hasEquity=any&hasSalary=any&industry=any&interviewProcess=any&jobType=any&layout=list-compact&remote=any&sortBy=keyword&usVisaNotRequired=any"
company_url = "https://www.workatastartup.com/companies/focal-systems"

print(waasu.is_companies_search(c_search_url)) # => True
print(waasu.is_company(company_url)) # => True

print(waasu.is_companies_search(company_url)) # => False
print(waasu.is_company(c_search_url)) # => False
