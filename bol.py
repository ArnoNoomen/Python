import os
import re
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.list import OneLineListItem, IconLeftWidget, MDList
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.card import MDCard
from kivy.uix.scrollview import ScrollView
from kivy.properties import StringProperty, NumericProperty, \
    BooleanProperty, AliasProperty, OptionProperty, \
    ListProperty, ObjectProperty, VariableListProperty, ColorProperty
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton

# https://www.youtube.com/watch?v=sa4AVMjjzNo
Window.keyboard_anim_args = {'t': 'in_out_expo', 'd': .2 } # in_out_quart
Window.softinput_mode = 'below_target'
# Window.size = (450, 740)


KV = """
#:import Clock kivy.clock.Clock

Screen:
    
    MDToolbar:
        id: toolbar
        pos_hint: {"top": 1}
        title: 'Bol handheld'
        elevation: 0
        left_action_items: [["menu", lambda x: nav_drawer.set_state('toggle')]]

    MDNavigationLayout:  
        x: toolbar.height 
         
        ScreenManager:
            
            id: screen_manager

            Screen_inlog:
                id: screen_inlog
                name: 'inlog'
                userId: user   
                BoxLayout:
                    
                    orientation: 'vertical'
                    padding: 50
                    
                    Widget:
                     
                    MDIcon:
                        icon: 'account'
                        icon_color: 1, 0, 1, 1
                        font_size: 180
                        markup: True
                        halign: 'center'
                    # MDTextFieldRound:    
                    MDTextField:
                        id: user
                        focus: True
                        pos_hint: {"center_x": .5 }
                        helper_text: "Username"
                        helper_text_mode: "on_focus" # persitent verdwijnt text bij input
                        width: 20
                        font_size: 48
                        on_text_validate: screen_inlog.on_enter_user 
                        
                    MDTextField:
                        id: passwd
                        hint_text: "Password"
                        pos_hint: {"center_x": .5 }
                        width: 20
                        font_size: 48           
                        password: True
                        
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: 20
                        Button:
                            text: 'OK'
                            size_hint_y: 1
                            on_press: Clock.schedule_once(lambda x: screen_inlog.handle_ok(screen_inlog, screen_manager, "menu"), .3) 
                                        
            Screen_menu:
                name: 'menu'
                id: screen_menu
                menuBoxObj: menuBox
                BoxLayout:
                    orientation: 'vertical'
                    id: menuBox
                    padding: 20
                    Widget:

                    ScrollView:
                        size_hint: None, None
                        size: "400dp", "400dp"
                        pos_hint: {"center_x": .5, "center_y": 1}
                        MDList:
                            OneLineListItem:
                                text: "Unloading"
                                    
                            OneLineListItem:
                                text: "Receiving"
                                on_release: Clock.schedule_once(lambda x: app.set_screen(screen_manager, "receiving"), .3)
                                    
                    # BoxLayout:
                    #     orientation: 'horizontal'
                    #     padding: 20
                    #     Button:
                    #         text: 'OK'
                    #         size_hint_y: 1
                    #     Button:
                    #         text: 'Cancel'
                    #         size_hint_y: 1
                    #         on_release: Clock.schedule_once(lambda x: app.set_screen(screen_manager,"inlog"), .3)
            
            Screen_receiving:
                name: 'receiving'
                id: screen_receiving
            
                BoxLayout:
                    orientation: 'vertical'
                    id: menuBox
                    padding: 20
                    Widget:

                    MDTextField:
                        id: receiveId
                        hint_text: "Receive number"
                        # pos_hint: {"center_x": .5 }
                        width: 20
                        font_size: 48 
                        on_text_validate: screen_receiving.on_enter_receiveId
                    MDLabel:
                        text: "Receipts 0"
                        font_style: "H3"
                        size_hint_y: None
                        height: '100dp'    
                    ScrollView:
                        # size_hint: None, None
                        size: "350dp", "200dp"
                        # pos_hint: {"center_x": .5, "center_y": 1.2}
                        MDList:
                            OneLineListItem:
                                text: "DOCK 123"
                            OneLineListItem:
                                text: "DOCK 124"
                            OneLineListItem:
                                text: "DOCK 125"
                            OneLineListItem:
                                text: "DOCK 126"                
                                    
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: 20
                        Button:
                            text: 'OK'
                            size_hint_y: 1
                            on_press: Clock.schedule_once(lambda x: app.set_screen(screen_manager, "article"), .3)
                        Button:
                            text: 'Cancel'
                            size_hint_y: 1
                            on_press: Clock.schedule_once(lambda x: app.set_screen(screen_manager, "menu"), .3)


            Screen_article:
                name:  'article'
                id: screen_article
            
                BoxLayout:
                    orientation: 'vertical'
                    id: menuBox
                    numeric: 'articleid'
                    padding: 20
                    Widget:

                    MDTextField:
                        id: articleid
                        icon_left: "account-check"
                        hint_text: "Article"
                        pos_hint: {"center_x": .5 }
                        width: 50
                        font_size: 48
                        on_text: screen_article.num(self.text)
                    MDLabel:
                        text: "Selected:"
                        font_style: "H4"
                        size_hint_y: None
                        height: '260dp'    
                    # ScrollView:
                    #     size_hint: None, None
                    #     size: "350dp", "200dp"
                    #     # pos_hint: {"center_x": .5, "center_y": 1.2}
                    #     MDList:
                    #         OneLineListItem:
                    #             text: ""
                    #         OneLineListItem:
                    #             text: ""
                    #         OneLineListItem:
                    #             text: ""
                    #         OneLineListItem:
                    #             text: ""                
                              
                    BoxLayout:
                        orientation: 'horizontal'
                        padding: 10
                        Button:
                            text: 'OK'
                            size_hint_y: 1
                        Button:
                            text: 'List'
                            size_hint_y: 1    
                        Button:
                            text: 'Cancel'
                            size_hint_y: 1
                            on_press: Clock.schedule_once(lambda x: app.set_screen(screen_manager, "menu"), .3)
    
        MDNavigationDrawer:
            id: nav_drawer
            scrim_color: [0, 0, 0, 0.0]
            elevation: 0

            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"
                Image:
                    id: avatar
                    size_hint: (.5,.5)
                    source: "bol.png"
                MDLabel:
                    text: "Mobile App"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]
              
                ScrollView:
                    MDlist:
                        id: md_list
                        
                        OneLineIconListItem:
                            text: "Info"
                            IconLeftWidget:
                                icon: "information-outline"
                                
                        OneLineIconListItem:
                            text: "Login"
                            on_release: Clock.schedule_once(lambda x: app.set_screen_nav(screen_manager, nav_drawer, "inlog"), .3)
                            IconLeftWidget:
                                icon: "login"
                                
                        OneLineIconListItem:
                            text: "Afsluiten"
                            on_release: exit()
                            IconLeftWidget:
                                icon: "logout"
                                    
                              
"""

class ContentNavigationDrawer(BoxLayout):
    pass
class Screen_inlog(Screen):
    userId = ObjectProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
         
        card = MDCard(orientation='vertical', pos_hint={
                        'center_x': .5, 'center_y': .5}, size_hint=(.9, .6))

        # self.add_widget(card)

    def handle_ok(self, screenLogin , manager, name_screen):
        print( self.userId.text ) 
        if self.userId.text != 'admin':
            close_button = MDFlatButton (text="Close",on_press=Screen_inlog.close_dialog)
            more_button = MDFlatButton(text="More")
            dialog = MDDialog(   title = 'Authentification',
                                 text='input:' + self.userId.text ,
                                 size_hint=( .3, None),
                                 buttons=[ close_button ]
                            )
            dialog.open()
        else:
            manager.current = name_screen
    
    def close_dialog(self):
        # screen.dialog.dismiss()
        self.parent.parent.parent.parent.dismiss() 

    def on_enter_user( self ):
        print ( self )    

    def num(self, name):
        if len(name) and name[-1] not in ('0123456789'):        
            # fieldObj = self.root.ids.numeric 
            # fieldObj.text = name.rstrip(name[-1])
            self.root.ids.numeric.text = name.rstrip(name[-1]) 
            

class Screen_menu(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Screen_receiving(Screen):
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    
    def on_enter_receiveId( self ):
        print ( self )

class Screen_article(Screen):
    numeric = ObjectProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def num(self, name):
        # paul
        if len(name) and name[-1] not in ('0123456789'):        
            # fieldObj = self.root.ids.numeric 
            # fieldObj.text = name.rstrip(name[-1])
            
            print ( self.parent.parent.parent.parent.root.ids.numeric )
            # my_obj.text = name.rstrip(name[-1]) 

# class nodig voor hamburgermenu
class MDlist(MDList):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # voeg dynamic list item toe       
        # self.add_widget(OneLineListItem( text= 'dynamic'))
            
class MainApp(MDApp):
    userId = ObjectProperty()
    menuBoxObj = ObjectProperty()
    def build(self):
        self.theme_cls.theme_style = "Light" 
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.accent_palette = "Blue"

        sm = ScreenManager()
        sm.add_widget(Screen_menu(name='menu'))
    
        screen = Builder.load_string(KV)
     
        card = MDCard(orientation='vertical', pos_hint={
                        'center_x': .5, 'center_y': .5}, size_hint=(.9, .6))
   
        return screen

    def set_screen_nav(self, manager, nav_drawer, name_screen):
        manager.current = name_screen
        nav_drawer.set_state("toggle")
    def set_screen(self, manager, name_screen):
        print ( name_screen )
        manager.current = name_screen
   
   

MainApp().run()