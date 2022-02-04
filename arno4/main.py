import sys
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.swiper import MDSwiperItem
from kivymd.utils.fitimage import FitImage
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.network.urlrequest import UrlRequest
sys.path.insert(1, '../testbestanden')
sys.path.insert(2, 'D:\\Github\\Python\\testbestanden')
import variabelen

def got_success(*args):
    try:
        for rij in args[1]['data']:
            url1 = rij['image'].replace('https://','http://')
            item = MDSwiperItem()
            item2 = FitImage(source=url1,radius=[20,])
            item.add_widget(item2)
            MainApp.screen1.ids.myswiper.add_widget(item)

    except BaseException as err:
        oke_button = MDFlatButton(text='Oke',on_press=MainApp.mydialog.dismiss())
        MainApp.mydialog = MDDialog(text=f"Unexpected {err=}, {type(err)=}",
                                    size_hint=(0.7, 1), buttons=[oke_button])
        MainApp.mydialog.open()

class MainApp(MDApp):

    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'BlueGray'
        MainApp.screen1 = Builder.load_file('main.kv')
        return MainApp.screen1

    def on_start(self):
        UrlRequest(url=variabelen.url1,
                on_success=got_success,
                req_headers=variabelen.header1)

MainApp().run()
