import kivy
from kivymd.app import MDApp
from kivymd.uix.card import MDCard

KV='''
Home:

    MDCard:
        size_hint: None, None
        size: "280dp", "180dp"
        pos_hint: {"center_x": .5, "center_y": .5}

'''

class Home(MDCard):
    pass

class Manage(MDApp):
    title = 'QUICKP'
    def build(self):
        return Home()


if __name__ == '__main__':
    Manage().run()