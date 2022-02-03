import sys
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.imagelist import SmartTileWithLabel
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.network.urlrequest import UrlRequest
sys.path.insert(1, '../testbestanden')
sys.path.insert(2, 'D:\\Github\\Python\\testbestanden')
import variabelen

KV = '''
ScrollView:

    GridLayout:
        id: mygridlayout
        cols: 3
        row_default_height: (self.width - self.cols*self.spacing[0]) / self.cols
        row_force_default: True
        size_hint_y: None
        height: self.minimum_height
        padding: dp(4), dp(4)
        spacing: dp(4)

'''

def got_success(*args):
    try:
        for rij in args[1]['data']:
            url1 = rij['image'].replace('https://','http://')
            item = SmartTileWithLabel(source=url1)
            MainApp.screen1.ids.mygridlayout.add_widget(item)

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
    def build(self):
        MainApp.screen1 = Builder.load_string(KV)
        return MainApp.screen1
    def on_start(self):
        req = UrlRequest(url=variabelen.url1,
                on_success=got_success,
                on_failure=got_failure,
                on_error=got_error,
                on_progress=got_progress,
                req_headers=variabelen.header1)
        print(req.resp_status)

MainApp().run()
