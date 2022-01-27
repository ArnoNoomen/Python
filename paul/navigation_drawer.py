
navigation_helper = """

NavigationLayout:
    
    MDNavigationDrawer:
        id: nav_drawer

        ContentNavigationDrawer:
            orientation: 'vertical'
            padding: "8dp"
            spacing: "8dp"

            Image:
                id: avatar
                size_hint: (1,1)
                source: "easyretail.jpg"

            MDLabel:
                text: "Attreya"
                font_style: "Subtitle1"
                size_hint_y: None
                height: self.texture_size[1]

            MDLabel:
                text: "attreya01@gmail.com"
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
                    
                            IconLeftWidget:
                                icon: "logout"
                                
                        
                            
                        
                            
"""

navigation_helper3 = """

NavigationLayout:
    
    # BoxLayout:
    #     orientation: 'vertical'
    #     MDToolbar:
    #         title: 'Demo Application 2222'
    #         pos_hint: {'top': 1}
    #         left_action_items: [["menu", lambda x: app.root.navigation_draw()]]
    #         elevation:5

    MDNavigationDrawer:
        id: nav_drawer
        pos_hint: {'top': 1}

        ContentNavigationDrawer:
            orientation: 'vertical'
            padding: "8dp"
            spacing: "8dp"

            Image:
                id: avatar
                size_hint: (1,1)
                source: ".jpg"

            MDLabel:
                text: "Attreya"
                font_style: "Subtitle1"
                size_hint_y: None
                height: self.texture_size[1]

            MDLabel:
                text: "attreya01@gmail.com"
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
                        
                            IconLeftWidget:
                                icon: "logout"
                                
                        
                            
                        
                            

"""
navigation_helper2 = """
Screen:
    NavigationLayout:
        ScreenManager:
            Screen:
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Demo Application'
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:5

                    Widget:

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"

                Image:
                    id: avatar
                    size_hint: (1,1)
                    source: ".jpg"

                MDLabel:
                    text: "Attreya"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]

                MDLabel:
                    text: "attreya01@gmail.com"
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
                            
                                IconLeftWidget:
                                    icon: "logout"
                                    
                           
                                
                            
                            

"""