import waasu

# Must input login informations
# username = "example_username"
# password = "example_password"

client = waasu.WorkAtAStartUp()
client.log_in(username=username, password=password)

# some parameters can have more than one choice
# client.get_companies(
#     jobType="contract", role="eng", demographic="black-founders", scroll_delay=10
# )

# query = ["junior"]
# query = ["python", "javascript", "data", "typescript"]
# client.get_companies(query=query, jobType="contract", role="eng", scroll_delay=10)

query = ["engieer", "entry", "junior"]
client.get_companies(query=query, jobType="fulltime", role="eng", scroll_delay=10)
