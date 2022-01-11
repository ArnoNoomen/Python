scherm = """
Screen:
    id: screen
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Demo2 Application'
                        left_action_items: [["menu", lambda x: nav_drawer.set_state()]]
                        elevation:5
                    MDLabel:
                        text: 'menu'
                        halign: 'center'
                    MDRectangleFlatButton:
                        text: 'Oke'
                        pos_hint: {'center_x':0.5,'center_y':0.5 }
                        #on_press: root.manager.current = 'profile'
                        on_press: app.popup1()
                    MDRectangleFlatButton:
                        text: 'Close'
                        pos_hint: {'center_x':0.5,'center_y':0.5 }
                        on_press: app.close()
        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"
                Image:
                    id: avatar
                    size_hint: (1,1)
                MDLabel:
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    size_hint_y: None
                    font_style: "Caption"
                    height: self.texture_size[1]
                ScrollView:
                    DrawerList:
                        id: md_list
                        MDList:
                            OneLineIconListItem:
                                text: "Profile"
                                IconLeftWidget:
                                    icon: "face-profile"
                            OneLineIconListItem:
                                text: "Upload"
                                IconLeftWidget:
                                    icon: "upload"
                            OneLineIconListItem:
                                text: "Logout"
                                on_press: app.close()
                                IconLeftWidget:
                                    icon: "logout"

"""
