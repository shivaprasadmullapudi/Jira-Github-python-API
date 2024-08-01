# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://shivaprasadmullapudi8.atlassian.net/rest/api/3/project"

API_TOkEN="ATATT3xFfGF0uU5pxYFispcvtiHvvU0TacFUowYfBIKJx6P7XqS6VSeBWilbTqOl_yD6kntWwJcio8iyz15s2B7X4fu9wJZr6o5bjE7AQ-jcYcQecHJaInZUH8fPvIBw3xj26iSbdKePzhcsiw5DVYZcg-ws541Npajzq8JO20DMP5aWn3ldkec=914A8451"

auth = HTTPBasicAuth("shivaprasadmullapudi8@gmail.com",API_TOkEN)

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