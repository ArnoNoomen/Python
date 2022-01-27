# https://www.udemy.com/share/101Utk3@b5jRGn9gJYVO0W8fzcUs9PRBuitpji58aINb5YJXJzOb6RlH6nzZj--5UWU2bqhf/

# https://kivymd.readthedocs.io/en/latest/components/dialog/

# http:/githup.com/attreyabhatt/

from logging import NullHandler
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.floatlayout import FloatLayout
from kivy.core.window import Window

KV='''
<screen>:
    FloatLayout:
        BoxLayout:
            orientation:'vertical'
            MDToolbar:
                id: toolbar
                title: "Example Banners"
                elevation: 10
                pos_hint: {'top': 1}
            MDTextField:
                id: dock
                icon_left: "key-variant"
                text: "Receive"
                width: 100
                font_size: 20 
                pos_hint: {'right': 1}        
            BoxLayout:
                orientation:'vertical'
                MDTextField:
                    id: dock
                    icon_right: "android"
                    icon_right_color: app.theme_cls.primary_color
                    text: "Dock"
                    helper_text: "Help tekst tbv invoer"
                    helper_text_mode: "on_focus"
                    width: 10
                    font_size: 20 
                    pos_hint: {'right': 1}  
                BoxLayout:
                    orientation:'horizontal'
                    MDFillRoundFlatButton:
                        text: "Ok"
                        size_hint: ( 0.35 , 0.2)
                        font_size: 15    
                    MDFillRoundFlatButton:
                        text: "Tussen"
                        size_hint: ( 0.35 , 0.2)
                        font_size: 15    
                    MDFillRoundFlatButton:
                        text: "Cancel"
                        pos_hint: { 'left': 1 }
                        size_hint: ( 0.35 , 0.2)    
                        font_size: 15    
'''

class ReceiveApp(MDApp):
    dialog = None
    def build(self):
     
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.accent_palette = "Blue"
     
        return Builder.load_string(KV)
    

ReceiveApp().run()
