from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem
from kivy.core.window import Window
# set window size
Window.size=(300,450)

list_helper = """
Screen:
    ScrollView:
        MDList:
            id: container
            
"""


class DemoApp(MDApp):

    def build(self):
        screen = Builder.load_string(list_helper)
        return screen

    def on_start(self):
        for i in range(20):
            item = OneLineListItem(text='Item ' + str(i))
            self.root.ids.container.add_widget(item)


DemoApp().run()