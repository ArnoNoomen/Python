
import requests
import json

url = "http://localhost/index.php?route=ocrestapi/account/register"

payload = json.dumps({
  "firstname": "user3",
  "lastname": "testing",
  "email": "heeren@inalphen.com",
  "telephone": "9874567890",
  "password": "Heeren123456",
  "confirm": "Heeren123456",
  "customer_group_id": "1",
  "newsletter": "1",
  "agree": "1"
})
headers = {
  'Authorization': 'Bearer 39da1e9f467af951e4f0b3dc9eb565c7e6c8d334',
  'Content-Type': 'application/json',
  'Cookie': 'OCSESSID=657f5c3732eed0750289fa16fe; currency=USD; language=en-gb'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

