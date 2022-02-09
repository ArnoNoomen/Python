import sys
from pickle import TRUE
from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivy.network.urlrequest import UrlRequest
sys.path.insert(1, '../testbestanden')
sys.path.insert(2, 'D:\\Github\\Python\\testbestanden')
import variabelen

def got_success(*args):
    try:
        for rij in args[1]['data']:
            data1 = (rij['name'],rij['name'],rij['name'],rij['name'])
            MainApp.mytable.row_data.append(data1)
    
    except BaseException as err:
        oke_button = MDFlatButton(text='Oke',on_press=MainApp.dismiss1)
        MainApp.mydialog = MDDialog(text=f"Unexpected {err=}, {type(err)=}",
                                    size_hint=(0.7, 1), buttons=[oke_button])
        MainApp.mydialog.open()

class MainApp(MDApp):

    def build(self):
        screen = Screen()
        MainApp.mytable = MDDataTable(
            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
            size_hint = (0.9, 0.6),
            check = TRUE,
            column_data = [
                ("First Name", dp(30)),
                ("Last Name", dp(30)),
                ("Email Address", dp(30)),
                ("Phone number", dp(30))
                ],
            #row_data = [
            #    ("a","b","c","d"),
            #    ("a","b","c","d")
            #]
        )
        MainApp.mytable.bind(on_check_press=self.checked)
        MainApp.mytable.bind(on_row_press=self.row_checked)
        oke_button = MDFlatButton(text='Oke',on_press=MainApp.addrow)

        screen.add_widget(MainApp.mytable)
        screen.add_widget(oke_button)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return screen

    def addrow(*args):
        print(variabelen.url1)
        UrlRequest(url=variabelen.url1,
                on_success=got_success,
                req_headers=variabelen.header1)

    def checked(self, instance_table, current_row):
        oke_button = MDFlatButton(text='Oke',on_press=MainApp.dismiss1)
        MainApp.mydialog = MDDialog(text=current_row[0],
                                    size_hint=(0.7, 1), buttons=[oke_button])
        MainApp.mydialog.open()

    def row_checked(self, instance_table, instance_row):
        pass

    def dismiss1(*args):
        MainApp.mydialog.dismiss()

MainApp().run()
