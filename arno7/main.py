import kivy
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import NumericProperty, StringProperty
from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard

Builder.load_file('story.kv')
Window.size = (320, 600)

class WindowManager(ScreenManager):
    pass

class MessageScreen(Screen):
    pass

class StoryWithImage(MDBoxLayout):
    text = StringProperty()
    source = StringProperty()

class ChatListItem(MDCard):
    text = StringProperty()
    source = StringProperty()


class MainApp(MDApp):
    def build(self):
        self.theme_cls.theme_style = 'Dark'
        self.theme_cls.primary_palette = 'Teal'
        self.theme_cls.accent_palette = 'Teal'
        self.theme_cls.accent_hue = '400'
        self.title = 'WhatsApp Redesign'

        sreens = [
            MessageScreen(name='message')
        ]

        self.wm = WindowManager(transition=FadeTransition())
        for screen in sreens:
            self.wm.add_widget(screen)

        return self.wm

if __name__ == "__main__":
    MainApp().run()
