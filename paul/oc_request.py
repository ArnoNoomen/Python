# https://www.letscms.com/documents/api/opencart-rest-api.html

import requests
import json

url = "http://localhost/index.php?route=ocrestapi/account/login"

payload = json.dumps({
  "email": "info@noomenict.nl",
  "password": "1234"
})
headers = {
  'Content-Type': 'application/json',
  'Cookie': 'OCSESSID=657f5c3732eed0750289fa16fe; currency=USD; language=en-gb'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
