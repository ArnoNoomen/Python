from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.screen import Screen


class MainApp(MDApp):
    def build(self):
        screen = Screen()
        btn1 = MDFlatButton(text='Hello World',
                            pos_hint={'center_x': 0.5, 'center_y': 0.5})
        screen.add_widget(btn1)
        return screen

MainApp().run()
