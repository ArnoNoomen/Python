from kivy.app import App
from kivy.lang import Builder
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import button
from kivy.uix.stacklayout import StackLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.base import runTouchApp
from kivy.uix.dropdown import DropDown

bt = Button(text='Hello')

Window.size=(300,450)

Builder.load_string("""
<myListView>:
    ListView:
        item_strings: [str(index) for index in range(100)]
""")

class ListView(BoxLayout):
    pass

if __name__ == '__main__':
    runTouchApp(ListView())