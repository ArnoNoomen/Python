from wsgiref import headers
import requests

url = 'http://inalphen.nl/ws/index.php?route=feed/rest_api/session'
myobj = {'somekey': 'somevalue'}


# https://opencart3-simple.api.opencart-api.com/

url = 'http://inalphen.nl/ws/index.php?route=feed/rest_api/products/simple'
# url = 'http://localhost/index.php?route=feed/rest_api/products/simple'

myheader =  {'X-Oc-Merchant-Id': '123'}
x = requests.get(url, headers = myheader, data = myobj)
print(x.text)