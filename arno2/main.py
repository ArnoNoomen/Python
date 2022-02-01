import http.client
import urllib.parse
import sys
import json
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivy.network.urlrequest import UrlRequest

# https://kivy.org/doc/stable/api-kivy.network.urlrequest.html

LISTHELPER = """
Screen:
    ScrollView:
        MDList:
            id: container
"""

def got_json(req, result):
    print('got_json')
    print(result)

def got_error(req, result):
    print('got_error')
    print(result)
    print('b')

class MainApp(MDApp):

    def build(self):
        self.icon = "android.png"
        self.title = "test"
        screen = Builder.load_string(LISTHELPER)
        return screen

    def on_start(self):
        webrequest_dict = {}
        try:
            with open("../testbestanden/webrequest.json", encoding='iso-8859-1') as fp1:
                webrequest_dict = json.loads(fp1.read())
        except FileNotFoundError:
            print('testbestanden/webrequest.json is niet aanwezig')
            sys.exit(1)

        params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
        myheader = {'X-Oc-Merchant-Id': '123'}

        if webrequest_dict["protocol"].upper() == 'HTTPS':
            conn = http.client.HTTPSConnection(webrequest_dict["site"])
        else:
            conn = http.client.HTTPConnection(webrequest_dict["site"])
        conn.request("GET", webrequest_dict["pagina"], None, myheader)
        res = conn.getresponse()
        body_dict = json.loads(res.read().decode("utf-8"))

        url1 = webrequest_dict["site"] + webrequest_dict["pagina"]
        print(url1)
        req = UrlRequest(url=url1, on_success=got_json, on_error=got_error)
        print('a')
        print(res)
        #for rij in body_dict['data']:
        #    item = OneLineListItem(text=rij['name'])
        #    self.root.ids.container.add_widget(item)

MainApp().run()
