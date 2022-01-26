from kivymd.app import MDApp
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.screen import Screen

class MainApp(MDApp):
    def show_data(*args):
        oke_button = MDFlatButton(text='Oke',on_press=MainApp.close_dialog)
        MainApp.mydialog = MDDialog(text='Helloworld', size_hint=(0.7, 1), buttons=[oke_button])
        MainApp.mydialog.open()
    def close_dialog(*args):
        MainApp.mydialog.dismiss()
    def build(self):
        screen = Screen()
        btn1 = MDFlatButton(text='Oke',
                            pos_hint={'center_x': 0.5, 'center_y': 0.5},
                            on_press=self.show_data)
        screen.add_widget(btn1)
        return screen

MainApp().run()
