import waasu
from bs4 import BeautifulSoup


query = ["query1", "query2"]

# Log In
# username = "example_username"
# password = "example_password"


client = waasu.WorkAtAStartUp().log_in(username=username, password=password)
companies = waasu.WorkAtAStartUp(query=query).get_companies(
    client, scroll_delay=6
)

print(companies)

client.quit()

# breakpoint()
