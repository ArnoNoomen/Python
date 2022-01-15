from kivymd.app import MDApp
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivy.uix.boxlayout import BoxLayout
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

class MyContent(BoxLayout):
    pass

popup = Popup(title='Test popup',
    content=Label(text='Hello world'),
    size_hint=(None, None), size=(400, 400)
)
class MainApp(MDApp):
    dialog = None

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
        names = ["Option 1", "Option 2", "Option 3"]

        for name in names:
            print(name)
            panel = MDExpansionPanel(
                content=MyContent(),
                panel_cls=MDExpansionPanelOneLine(text=name))
            self.root.ids.panel_container.add_widget(panel)

MainApp().run()
