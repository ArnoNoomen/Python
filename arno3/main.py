#from kivymd.app import MDApp
#from kivy.uix.image import AsyncImage
#
#class MainApp(MDApp):
#    def build(self):
#        url1 = 'http://inalphen.nl/ws/image/cache/catalog/demo/htc_touch_hd_1-500x500.jpg'
#        img = AsyncImage(source=url1)
#        return img
#
#MainApp().run()
#
from kivymd.app import MDApp
from kivy.lang import Builder

KV = '''
ScrollView:

    GridLayout:
        id: mygridlayout
        cols: 3
        row_default_height: (self.width - self.cols*self.spacing[0]) / self.cols
        row_force_default: True
        size_hint_y: None
        height: self.minimum_height
        padding: dp(4), dp(4)
        spacing: dp(4)

        SmartTileWithLabel:
            source: "http://inalphen.nl/ws/image/cache/catalog/demo/htc_touch_hd_1-500x500.jpg"

        SmartTileWithLabel:
            source: "cat-2.jpg"
            tile_text_color: app.theme_cls.accent_color

        SmartTileWithLabel:
            source: "cat-3.jpg"
            tile_text_color: app.theme_cls.accent_color
'''

class MyApp(MDApp):
    def build(self):
        root = Builder.load_string(KV)
        return root
    def on_start(self):
        pass

MyApp().run()
