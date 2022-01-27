from kivy.app import App
from kivy.lang import Builder
from kivy.uix.textinput import TextInput

class MyTextInput(TextInput):
    def on_touch_down(self, touch):
        if self.collide_point(*touch.pos):
            self.text = ""
            return True
        return super(MyTextInput, self).on_touch_down(touch)

kv_string = """
ScreenManager:
    id: manager
    Screen:
        BoxLayout:
            orientation: 'vertical'
            Button:
                text: 'Why does it clear multiple inputs? And why do they get cleared after touch_up?'
            MyTextInput:
                text: 'Write Your Name'
            MyTextInput:
                text: 'Write Your Last Name'  
            MyTextInput:
                text: 'Write Your Phone Number'
"""
kv_string2 = """
ScreenManager:
    id: manager
    Screen:
        BoxLayout:
            orientation: 'vertical'
            Button:
                text: 'Why does it clear multiple inputs? And why do they get cleared after touch_up?'
            TextInput:
                text: 'Write Your Name'
                on_touch_down: if self.collide_point(*args[1].pos): self.text = ""
            TextInput:
                text: 'Write Your Last Name'
                on_touch_down: if self.collide_point(*args[1].pos): self.text = ""
            TextInput:
                text: 'Write Your Phone Number'
                on_touch_down: if self.collide_point(*args[1].pos): self.text = ""
"""
kv_string3 = """
ScreenManager:
    id: manager
    Screen:
        BoxLayout:
            orientation: 'vertical'
            Button:
                text: 'Why does it clear multiple inputs? And why do they get cleared after touch_up?'
            TextInput:
                text: 'Write Your Name'
                on_focus: self.text = ""
            TextInput:
                text: 'Write Your Last Name'
                on_focus: self.text = ""
            TextInput:
                text: 'Write Your Phone Number'
                on_focus: self.text = ""
"""

class MyApp(App):
    def build(self):
        root_widget = Builder.load_string(kv_string3)
        return root_widget

if __name__ == "__main__":
    MyApp().run()