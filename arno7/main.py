from ast import Str
import kivy
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.properties import StringProperty, DictProperty, OptionProperty
from kivy.lang.builder import Builder
from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.card import MDCard
from demo.demo import profiles

Builder.load_file('story.kv')
Builder.load_file('chat_list.kv')
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
    timestamp = StringProperty()
    profile = DictProperty()
    isread = OptionProperty(None, options=['deliverd', 'read', 'new', 'waiting'])
    friend_name = StringProperty()

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

    def story_builder(self):
        for profile in profiles:
            self.story = StoryWithImage()
            self.story.text = profile['name']
            self.story.image = profile['image']
            self.story.source = profile['source']
            self.wm.screens[0].ids['story_layout']

    def chat_list_builder(self):
        for profile in profiles:
            for message in profile['msg']:
                self.chatitem = ChatListItem()
                self.chatitem.profile = profile
                self.chatitem.friend_name = message['name']
                self.chatitem.friend_avatar = message['image']

if __name__ == "__main__":
    MainApp().run()
