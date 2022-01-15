from kivymd.app import MDApp
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivymd.uix.expansionpanel import MDExpansionPanel
from kivy.uix.boxlayout import BoxLayout

class MyContent(BoxLayout):
    pass

popup = Popup(title='Test popup',
    content=Label(text='Hello world'),
    size_hint=(None, None), size=(400, 400)
)
class MainApp(MDApp):

    def popup1(self):
        popup.open()

    def on_start(self):
        names = ['Option 1', 'Option 2', , 'Option 3']

        for name in names:
            panel = MDExpansionPanel(title=name, content=MyContent())
            self.root.ids.panel_container.add_widget(panel)

MainApp().run()
