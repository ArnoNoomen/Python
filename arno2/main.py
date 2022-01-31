import http.client
import urllib.parse
import sys
import json
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem

LISTHELPER = """
Screen:
    ScrollView:
        MDList:
            id: container
"""

class MainApp(MDApp):

    def build(self):
        screen = Builder.load_string(LISTHELPER)
        return screen

    def on_start1(self):
        print('a')
        for i in range(20):
            item = OneLineListItem(text='Item ' + str(i))
            self.root.ids.container.add_widget(item)

    def on_start(self):
        webrequest_dict = {}
        try:
            with open("../testbestanden/webrequest.json", encoding='iso-8859-1') as fp1:
                webrequest_dict = json.loads(fp1.read())
        except FileNotFoundError:
            print('testbestanden/webrequest.json is niet aanwezig')
            sys.exit(1)

        #params = urllib.parse.urlencode({'@number': 12524, '@type': 'issue', '@action': 'show'})
        myheader = {'X-Oc-Merchant-Id': '123'}

        if webrequest_dict["protocol"].upper() == 'HTTPS':
            conn = http.client.HTTPSConnection(webrequest_dict["site"])
        else:
            conn = http.client.HTTPConnection(webrequest_dict["site"])
        conn.request("GET", webrequest_dict["pagina"], None, myheader)
        res = conn.getresponse()
        print(res.status, res.reason)
        body_dict = json.loads(res.read().decode("utf-8"))
        print(body_dict['success'])
        print(body_dict['error'])
        for rij in body_dict['data']:
            item = OneLineListItem(text=rij['name'])
            self.root.ids.container.add_widget(item)

MainApp().run()
