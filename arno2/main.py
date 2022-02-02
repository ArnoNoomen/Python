import sys
import os
import json
from kivy.network.urlrequest import UrlRequest
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
sys.path.insert(1, '../testbestanden')
sys.path.insert(2, 'D:\\Github\\Python\\testbestanden')
import variabelen

# https://kivy.org/doc/stable/api-kivy.network.urlrequest.html

LISTHELPER = """
Screen:
    ScrollView:
        MDList:
            id: container
"""

def ophalen_image(url):
    MainApp.basename = os.path.basename(url)
    url1 = url.replace('https://','http://')
    UrlRequest(url1,on_success=got_success1,
                   on_failure=got_failure1,
                   on_error=got_error1,
                   req_headers=variabelen.header1)

def got_success1(*args):
    with open(MainApp.basename, 'w+b') as fp1:
        fp1.write(args[1])

def got_failure1(*args):
    print('failure')
def got_error1(*args):
    print('error')

def got_success(*args):
    try:
        for rij in args[1]['data']:
            item = OneLineListItem(text=rij['name'])
            MainApp.screen1.ids.container.add_widget(item)
    except:
        try:
            print(args[1]['error'])
        except:
            pass
        oke_button = MDFlatButton(text='Oke',on_press=close_dialog)
        MainApp.mydialog = MDDialog(text='Fout',
                                    size_hint=(0.7, 1), buttons=[oke_button])
        MainApp.mydialog.open()

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
    MainApp.mydialog = MDDialog(text='fout',
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
        UrlRequest(url=variabelen.url1,
                        on_success=got_success,
                        on_failure=got_failure,
                        on_error=got_error,
                        on_progress=got_progress,
                        req_headers=variabelen.header1)
        ophalen_image('https://inalphen.nl/ws/image/cache/catalog/demo/htc_touch_hd_1-500x500.jpg')

MainApp().run()
