
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.core.window import Window

KV = """
Screen:
    numericObj: numeric
 
    Widget:
        
    MDTextField:
        id: numeric
        focus: True
        pos_hint: {"center_x": .5, "center_y": .5}
        helper_text: "Alleen numbers toestaan"
        helper_text_mode: "on_focus" # persitent verdwijnt text bij input
        width: 20
        font_size: 48
        # on_focus: self.text = "" # maak veld leeg bij om click
        on_text: app.num(self.text)
               
    Button:
        text: 'OK'
        size_hint: ( 0.35 , 0.10) 
        pos_hint: {"center_x": .5, "center_y": .3}
"""

class MainApp(MDApp):
    
    # numeric = ObjectProperty()
    def build(self):
        screen = Builder.load_string(KV)
        return screen
    
    def num(self, name):
        if len(name) and name[-1] not in ('0123456789'):        
            # fieldObj = self.root.ids.numeric 
            # fieldObj.text = name.rstrip(name[-1])
            self.root.ids.numeric.text = name.rstrip(name[-1]) 
            
MainApp().run()