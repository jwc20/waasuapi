import waasu
from bs4 import BeautifulSoup




# Log In
# username = "example_username"
# password = "example_password"

client = waasu.WorkAtAStartUp()
client.log_in(username=username, password=password)

# some parameters can have more than one choice
# client.get_companies(
#     jobType="contract", role="eng", demographic="black-founders", scroll_delay=10
# )

query = ["junior"]
# query = ["python", "javascript", "data", "typescript"]
client.get_companies(query=query, industry="B2B Software and Services", jobType="contract", role="eng", scroll_delay=10)

# breakpoint()
