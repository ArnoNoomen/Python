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

def got_success(*args):
    print(MainApp.rrr)
    for rij in args[1]['data']:
        item = OneLineListItem(text=rij['name'])
        print(rij['name'])
        #self.root.ids.container.add_widget(item)

def got_error(*args):
    print(args[1])

def got_progress(*args):
    pass

def got_failure(*args):
    print('on_failure')


class MainApp(MDApp):

    rrr = 'eee'

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

        req = UrlRequest(url='http://' + webrequest_dict["site"] + webrequest_dict["pagina"],
                        on_success=got_success,
                        on_failure=got_failure,
                        on_error=got_error,
                        on_progress=got_progress,
                        req_headers=myheader)

MainApp().run()