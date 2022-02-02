from multiprocessing.connection import wait
import sys
import os
import json
import filelock
from kivy.network.urlrequest import UrlRequest
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.list import OneLineListItem
from kivymd.uix.list import OneLineAvatarListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.uix.image import AsyncImage
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
    pass
    #with open(MainApp.basename, 'w+b') as fp1:
    #    fp1.write(args[1])

def got_failure1(*args):
    print('failure')
def got_error1(*args):
    print('error')

def got_success(*args):
    try:
        for rij in args[1]['data']:
            item = OneLineIconListItem(text=rij['name'])
            url1 = rij['image'].replace('https://','http://')
            aimg = AsyncImage(source=url1)
            icons = IconLeftWidget(icon="android")
            item.add_widget(icons)
            MainApp.screen1.ids.container.add_widget(item)
    except BaseException as err:
        oke_button = MDFlatButton(text='Oke',on_press=close_dialog)
        MainApp.mydialog = MDDialog(text=f"Unexpected {err=}, {type(err)=}",
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
    oke_button = MDFlatButton(text='Oke1',on_press=close_dialog)
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
        UrlRequest(url=variabelen.url1,
                        on_success=got_success,
                        on_failure=got_failure,
                        on_error=got_error,
                        on_progress=got_progress,
                        req_headers=variabelen.header1)

MainApp().run()
