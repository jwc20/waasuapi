import waasu
from bs4 import BeautifulSoup


query = ["query1", "query2"]

# Log In
# username = "example_username"
# password = "example_password"


client = waasu.WorkAtAStartUp(query=query)
client.log_in(username=username, password=password)

# some parameters can have more than one choice
client.get_companies(companySize="seed", jobType="contract", role="eng", demographic="black-founders", scroll_delay=10)

# breakpoint()
