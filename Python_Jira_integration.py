# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://shivaprasadmullapudi8.atlassian.net/rest/api/3/issue"

#API_TOkEN=""


auth = HTTPBasicAuth("shivaprasadmullapudi8@gmail.com", "API_TOkEN")

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
    
    
  "fields": {
    
   
  
   
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My First Ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
   
    
    "issuetype": {
      "id": "10006"
    },

    "project": {
      "key": "SHIV"
    },
   
    "summary": "Python Problem",

  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))
