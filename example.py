
import waasu
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Retrieve username and password from environment variables
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")

client = waasu.WorkAtAStartUp()
client.log_in(username=username, password=password)

# Example usage with parameters
query = ["engineer"]
client.get_companies(query=query, jobType="fulltime", role="eng", scroll_delay=10)

