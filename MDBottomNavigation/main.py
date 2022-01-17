from kivymd.app import MDApp
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.menu import MDDropdownMenu

class MyContent(BoxLayout):
    pass

popup = Popup(title='Test popup',
    content=Label(text='Hello world'),
    size_hint=(None, None), size=(400, 400)
)
class MainApp(MDApp):
    dialog = None
    dropdown = None

    def print_ids(self, ii):
        print(ii)

    def set_text(self, text):
        print(text)
        self.root.ids.special_gridlayout.ids.special_label.text = text
        print(self.root.ids.special_gridlayout.ids.special_label.text)

    def popup1(self):
        popup.open()

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text="Discard draft?",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="DISCARD",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        self.dialog.open()

    def on_start(self):
        self.dropdown = MDDropdownMenu(width_mult=4)
        print(self.dropdown)
        for i in range(6):
            self.dropdown.items.append(
                {"viewclass":"MDMenuItem","text":"Option " + str(i), "callback": self.option_callback}
            )
        names = ["Option 1", "Option 2", "Option 3"]

        for name in names:
            panel = MDExpansionPanel(
                content=MyContent(),
                panel_cls=MDExpansionPanelOneLine(text=name))
            self.root.ids.panel_container.add_widget(panel)

    def option_callback(self, text_of_the_option):
        print(text_of_the_option)

MainApp().run()
