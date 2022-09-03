import waasu
from bs4 import BeautifulSoup







keywords = []

# Log In
# username = "example_username"
# password = "example_password"


client = waasu.WorkAtAStartUp().log_in(username=username, password=password)
waasu.WorkAtAStartUp().get_companies(client, scroll_delay=5)


# breakpoint()
