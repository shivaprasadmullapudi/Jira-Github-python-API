# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://shivaprasadmullapudi8.atlassian.net/rest/api/3/project"

#API_TOkEN=""

auth = HTTPBasicAuth("shivaprasadmullapudi8@gmail.com","API_TOkEN")

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output=json.loads(response.text)

name=output[0]["name"]

print(name)