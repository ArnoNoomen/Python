import requests

# http://localhost
url = "http://localhost/index.php?route=ocrestapi/common/home"

payload={}
files={}
headers = {
  'Authorization': 'Bearer 39da1e9f467af951e4f0b3dc9eb565c7e6c8d334',
  'Cookie': 'OCSESSID=daa4535295bbfa04fa063be9e5; currency=USD; language=en-gb'
}

response = requests.request("GET", url, headers=headers, data=payload, files=files)

print(response.text)