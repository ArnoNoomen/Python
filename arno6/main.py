from pickle import TRUE
from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.app import MDApp
from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable

class MainApp(MDApp):
    def build(self):
        screen = Screen()
        table = MDDataTable(
            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
            size_hint = (0.9, 0.6),
            check = TRUE,
            column_data = [
                ("First Name", dp(30)),
                ("Last Name", dp(30)),
                ("Email Address", dp(30)),
                ("Phone number", dp(30))
                ],
            row_data = [
                ("a","b","c","d"),
                ("a","b","c","d")
            ]
        )
        table.bind(on_check_press=self.checked)
        table.bind(on_row_press=self.row_checked)
        screen.add_widget(table)
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        return screen

    def checked(self, instance_table, current_row):
        print(instance_table)

    def row_checked(self, instance_table, instance_row):
        print(instance_row)

MainApp().run()
