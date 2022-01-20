scherm = """

ScreenManager:
    MenuScreen:
    ProfileScreen:
    UploadScreen:

<MenuScreen>:
    name: 'menu'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Demo Application'
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["dots-vertical", lambda x: app.callback()], ["clock", lambda x: app.callback_2()]]
            elevation:5
        BoxLayout:
            orientation: 'vertical'
            MDLabel:
                text: 'menu'
                halign: 'center'
            MDRectangleFlatButton:
                text: 'Profile'
                pos_hint: {'center_x':0.5,'center_y':0.5 }
                on_press: root.manager.current = 'profile'
            MDRectangleFlatButton:
                text: 'Upload'
                pos_hint: {'center_x':0.5,'center_y':0.5 }
                on_press: root.manager.current = 'upload'

<ProfileScreen>:
    name: 'profile'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Demo Application'
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["dots-vertical", lambda x: app.callback()], ["clock", lambda x: app.callback_2()]]
            elevation:5

        MDLabel:
            text: 'Profile'
            halign: 'center'

        MDRectangleFlatButton:
            text: 'Back'
            pos_hint: {'center_x':0.5,'center_y':0.1}
            on_press: root.manager.current = 'menu'

<UploadScreen>:
    name: 'upload'
    BoxLayout:
        orientation: 'vertical'
        MDToolbar:
            title: 'Demo Application'
            left_action_items: [["menu", lambda x: app.navigation_draw()]]
            right_action_items: [["dots-vertical", lambda x: app.callback()], ["clock", lambda x: app.callback_2()]]
            elevation:5

        MDLabel:
            text: 'Upload'
            halign: 'center'
        MDRectangleFlatButton:
            text: 'Back'
            pos_hint: {'center_x':0.5,'center_y':0.1}
            on_press: root.manager.current = 'menu'

"""