import sys
import json
from kivy.network.urlrequest import UrlRequest
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog

# https://kivy.org/doc/stable/api-kivy.network.urlrequest.html

LISTHELPER = """
Screen:
    ScrollView:
        MDList:
            id: container
"""

def got_success(*args):
    try:
        for rij in args[1]['data']:
            item = OneLineListItem(text=rij['name'])
            MainApp.screen1.ids.container.add_widget(item)
    except:
        pass

def got_error(*args):
    oke_button = MDFlatButton(text='Oke',on_press=close_dialog)
    MainApp.mydialog = MDDialog(text=f'{args[1]}',
                                    size_hint=(0.7, 1), buttons=[oke_button])
    MainApp.mydialog.open()

def got_progress(*args):
    pass

def close_dialog(*args):
    MainApp.mydialog.dismiss()

def got_failure(*args):
    oke_button = MDFlatButton(text='Oke',on_press=close_dialog)
    MainApp.mydialog = MDDialog(text=f'{args[1]}',
                                    size_hint=(0.7, 1), buttons=[oke_button])
    MainApp.mydialog.open()

class MainApp(MDApp):

    screen1 = None

    def build(self):
        self.icon = "android.png"
        self.title = "test"
        MainApp.screen1 = Builder.load_string(LISTHELPER)
        return MainApp.screen1

    def on_start(self):
        webrequest_dict = {}
        try:
            with open("../testbestanden/webrequest.json", encoding='iso-8859-1') as fp1:
                webrequest_dict = json.loads(fp1.read())
        except FileNotFoundError:
            print('testbestanden/webrequest.json is niet aanwezig')
            sys.exit(1)

        myheader = {'X-Oc-Merchant-Id': '123'}
        UrlRequest(url='http://' + webrequest_dict["site"] + webrequest_dict["pagina"],
                        on_success=got_success,
                        on_failure=got_failure,
                        on_error=got_error,
                        on_progress=got_progress,
                        req_headers=myheader)

MainApp().run()
