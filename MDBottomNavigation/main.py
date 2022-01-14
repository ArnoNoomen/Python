from kivymd.app import MDApp
from kivy.uix.popup import Popup
from kivy.uix.label import Label

popup = Popup(title='Test popup',
    content=Label(text='Hello world'),
    size_hint=(None, None), size=(400, 400)
)
class MainApp(MDApp):

    def popup1(self):
        popup.open()

MainApp().run()
