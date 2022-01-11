#import os
#os.environ["KIVY_NO_CONSOLELOG"] = "1"
from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window

from scherm2_layout import scherm

class NavigationLayout(Screen):
    print('NavigationLayout')
    pass

class ContentNavigationDrawer(Screen):
    print('ContentNavigationDrawer')
    pass

class DrawerList(Screen):
    print('DrawerList')
    pass

class MenuScreen(Screen):
    print('MenuScreen')
    pass

class ProfileScreen(Screen):
    print('ProfileScreen')
    pass

class UploadScreen(Screen):
    print('UploadScreen')
    pass

popup = Popup(title='Test popup',
    content=Label(text='Hello world'),
    size_hint=(None, None), size=(400, 400)
)

class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(scherm)
        return screen

    def on_start(self):
        print('on_start')

    def popup1(self):
        popup.open()   
        
    def close(self):
        print('close')
        #self.dialog.dismiss()

DemoApp().run()
