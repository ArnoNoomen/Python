from turtle import width
from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.textfield import MDTextField

from kivymd.uix.screen import Screen

class MainApp(MDApp):
    def show_data(*args):
        oke_button = MDFlatButton(text='Oke2',on_press=MainApp.close_dialog)
        MainApp.mydialog = MDDialog(text=f'{MainApp.screen.width} {MainApp.screen.height}',
                                    size_hint=(0.7, 1), buttons=[oke_button])
        MainApp.mydialog.text = MainApp.mydialog.text + f'\n{MainApp.mydialog.width} {MainApp.mydialog.height}'
        MainApp.mydialog.text = MainApp.mydialog.text + f'\n{MainApp.username.width} {MainApp.username.height}'
        MainApp.mydialog.open()
    def close_dialog(*args):
        MainApp.mydialog.dismiss()
    def build(self):
        MainApp.screen = Screen()
        MainApp.username = MDTextField(
                            pos_hint={'center_x': 0.5, 'center_y': 0.7},
                            )
        btn1 = MDFlatButton(text='Oke1',
                            pos_hint={'center_x': 0.5, 'center_y': 0.5},
                            on_press=self.show_data
                            )
        MainApp.screen.add_widget(MainApp.username)
        MainApp.screen.add_widget(btn1)
        return MainApp.screen

MainApp().run()
