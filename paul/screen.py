import kivy
kivy.require('1.9.1') # replace with your current kivy version !

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import ObjectProperty


class MainScreen(Screen):
    pass


class AnotherScreen(Screen):
    pass


class ScreenManagement(ScreenManager):
    mainscreen = ObjectProperty(None)
    anotherscreen = ObjectProperty(None)


class Test(App):

    def build(self):
        return ScreenManagement()

if __name__ == "__main__":
    Test().run()