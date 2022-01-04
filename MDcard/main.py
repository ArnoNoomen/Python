# https://www.udemy.com/share/101Utk3@b5jRGn9gJYVO0W8fzcUs9PRBuitpji58aINb5YJXJzOb6RlH6nzZj--5UWU2bqhf/

# https://kivymd.readthedocs.io/en/latest/components/dialog/

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.floatlayout import FloatLayout
from kivy.core.window import Window
import runpy

# set window size
Window.size=(310,450)

KV='''
Screen:
    
    MDTextField:
        pos: 1,360
        id: receive
        icon_left: "account-check"
        hint_text: "Receive Number"
        foreground_color: 1, 0, 1, 1
        width: 220
        font_size: 20   
       
    MDTextField:
        pos: 1,100
        id: dock
        icon_left: "key-variant"
        hint_text: "Dock"
        foreground_color: 1, 0, 1, 1
        width: 220
        font_size: 20         
    
    MDFillRoundFlatButton:
        text: "Ok"
        font_size: 15    
        orientation: 'horizontal'
        on_press: app.verder()
        pos: 1,1
    MDFillRoundFlatButton:
        text: "Cancel"
        font_size: 15
        orientation: 'horizontal'
        pos: 100,1
        # on_press: app.login() 
'''


class LoginApp(MDApp):
    dialog = None
    def build(self):
        # define theme colors
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.accent_palette = "Blue"
        # load and return kv string
        return Builder.load_string(KV)
    
    def verder(self):
        print( 'jaja' )
        self.dialog.dismiss()
        runpy.run_module(mod_name='banner')

    def close(self, instance):
        # close dialog
        self.dialog.dismiss()
    
# run app    
LoginApp().run()