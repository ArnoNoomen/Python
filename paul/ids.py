from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.lang import Builder


# https://stackoverflow.com/questions/67767960/attributeerror-nonetype-object-has-no-attribute-ids-in-kivymd    

ids = """
<LoginScreen>
    MDScreen:
        name: 'Screen1'
        md_bg_color: (23/255, 31/255, 40/255, 1)

        MDCard:
            size_hint: None, None
            size: 320, 400
            pos_hint: {"center_x": .5, "center_y": .5}
            orientation: 'vertical'
            padding: '8dp'
            md_bg_color: (23/255, 31/255, 47/255, 1)
            elevation: 10
            spacing: 10

            MDLabel:
                text: 'LOGIN'
                font_style: 'Button'
                font_size: 45
                halign: 'center'
                size_hint_y: None
                height: self.texture_size[1]
                theme_text_color: 'Custom'
                text_color: (1, 1, 1, 1)
                padding_y: 15

            MDTextFieldRound:
                hint_text: 'enter username'
                icon_right: 'account'
                color_active: 1, 1, 1, 1
                pos_hint: {"center_x":.5}
                size_hint_x: None
                width: 220
                font_size: 16
                on_text: app.set_user_name(self.text)
            MDTextFieldRound:
                hint_text: 'enter password'
                icon_right: 'eye-off'
                color_active: 1, 1, 1, 1
                size_hint_x: None
                width: 210
                font_size: 15
                pos_hint: {"center_x": .5}
                password: True

            MDTextField:
                id: users_name
                hint_text: "What's your name?"
                helper_text: "What your friends call you.."
                helper_text_mode: "on_focus"
                pos_hint: {"center_x": .5}
                size_hint_x: None
                width: 200

            MDRectangleFlatButton:
                text: 'LOGIN'
                pos_hint: {'center_x': .5}
                size_hint_x: None
                root_button_anim: True
                on_press:
                    # change direction to to non-movable
                    root.manager.transition.direction = 'left'
                    root.manager.current = 'Screen2'
        
            Widget:
                pos_hint_y: None
                height: 30
            
<SecondScreen>
    MDScreen:
        md_bg_color: (23/255, 31/255, 40/255, 1)
        name: 'Screen2'
        MDCard:
            md_bg_color: (23/255, 31/255, 47/255, 1)
            padding: 10
            elevation: 10
            orientation: 'vertical'
            spacing: 25
            pos_hint: {'center_x': .5, "center_y": .5}
            size_hint: None, None
            size: 340, 400

            MDTextButton:
                text: '< Back'
                padding_x: 0
                custom_color: (244/255, 246/255, 214/255, 1)
                pos_hint: {"center_y": .1}
                root_button_anim: True
                on_press:
                    # change direction to to non-movable
                    root.manager.transition.direction = 'right'
                    root.manager.current = 'Screen1'

            MDLabel:
                id: my_label
                text: f'Hello {my_label.text}'
                # halign: 'center'
                pos_hint: {'center_x': .5}
                size_hint_y: None
                font_style: 'Body1'
                theme_text_color: 'Custom'
                text_color: (1, 1, 1, 1)

                font_size: 20
                height: self.texture_size[1]
                padding_y: 15

            Widget:
                height: 10

"""

class LoginScreen(Screen):
    pass


class SecondScreen(Screen):
    pass


class LoginApp(MDApp):
    def build(self):

        # users_name = self.root.ids.users_name
        # my_label = self.root.ids.my_label
        # my_label.text = users_name.text

        screen = Builder.load_string(ids)
        sm = ScreenManager()
        sm.add_widget(LoginScreen(name='Screen1'))
        sm.add_widget(SecondScreen(name='Screen2'))

        return sm
    def set_user_name(self, name):
        my_label = self.root.get_screen('Screen2').ids.my_label
        my_label.text = name

LoginApp().run()