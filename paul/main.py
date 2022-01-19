from calendar import Calendar
from logging import root
import os
import re
from tkinter import Widget
from kivymd.app import MDApp
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.list import OneLineListItem, TwoLineListItem, IconLeftWidget, MDList, ImageLeftWidget, OneLineAvatarIconListItem
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
from kivy.clock import Clock

# OpenCart Api
# https://www.letscms.com/documents/api/opencart-rest-api.html


# Urls kivy': en cursussen
# Layout: https://kivy.org/doc/stable/guide/widgets.html#
# course: https://www.udemy.com/user/johnelder3/
# course: https://www.udemy.com/course/kivy-mobile-app/learn/lecture/7865250?components=available_coupons%2Cbuy_button%2Cbuy_for_team%2Ccacheable_add_to_cart%2Ccacheable_buy_button%2Ccacheable_deal_badge%2Ccacheable_discount_expiration%2Ccacheable_price_text%2Ccacheable_purchase_text%2Ccurated_for_ufb_notice_context%2Cdeal_badge%2Cdiscount_expiration%2Cgift_this_course%2Cincentives_context%2Cinstructor_links%2Clifetime_access_context%2Cmoney_back_guarantee%2Cprice_text%2Cpurchase_tabs_context%2Cpurchase%2Crecommendation%2Credeem_coupon%2Csidebar_container%2Csubscribe_team_modal_context%2Ctop_companies_notice_context#overview
# course: https://www.udemy.com/course/kivymd-python-build-mobile-apps-using-material-design/learn/lecture/28108484#overview


# https://www.youtube.com/watch?v=sa4AVMjjzNo ( keyboard )
Window.keyboard_anim_args = {'t': 'in_out_expo', 'd': .2 } # in_out_quart
Window.softinput_mode = 'below_target'
Window.size = (400, 600)

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
                        # on_text_validate: screen_inlog.on_enter_user

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
                            on_press: Clock.schedule_once(lambda x: screen_inlog.handle_ok(screen_inlog, screen_manager, "leeg"), .3)
            Screen_menu:
                name: 'menu'
                id: screen_menu
                menuBoxObj: menuBox

                BoxLayout:
                    orientation: 'vertical'
                    id: menuBox
                    padding: 20
                    Widget:
                    MDTextField:
                        id: searchmenu
                        icon_right: "text-search"
                        hint_text: "Search menu"
                        width: 20
                        font_size: 48

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
                            OneLineListItem:
                                text: "Picking Mini PickBatches"
                            OneLineListItem:
                                text: "Unloading LCL"
                            OneLineListItem:
                                text: "Relocate RCT"
                            OneLineListItem:
                                text: "Relocate RPT"
                            OneLineListItem:
                                text: "Real-time count"
                            OneLineListItem:
                                text: "LDA"
                            OneLineListItem:
                                text: "Replenishment RT"
                            OneLineListItem:
                                text: "New item procedure"
                            OneLineListItem:
                                text: "Putaway CT"
                            OneLineListItem:
                                text: "Picking CT"
                            OneLineListItem:
                                text: "Palletisation"

                            # maak uitklap
                            # Putaway CT
                            #         TR
                            #         EPT
                            #         RPT
                            #         NCK Returns
                            # Picking HCT
                            #         RT
                            #         RPT

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
                        height: '200dp'

                    Spinner:
                        id: spinner_dock
                        size_hint: 1,.3
                        text: "Dock"
                        background_color: 0,255,255,255
                        color: 0,0,0,1
                        values: [ "DOCK 130", "DOCK131","DOCK 132", "DOCK133","DOCK 134", "DOCK135","DOCK 136", "DOCK137", "DOCK138" ]
                    # ScrollView:
                    #     # size_hint: None, None
                    #     size: "350dp", "200dp"
                    #     # pos_hint: {"center_x": .5, "center_y": 1.2}
                    #     MDList:
                    #         OneLineListItem:
                    #             text: "DOCK 123"
                    #         OneLineListItem:
                    #             text: "DOCK 124"
                    #         OneLineListItem:
                    #             text: "DOCK 125"
                    #         OneLineListItem:
                    #             text: "DOCK 126"

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
                    padding: 20

                    Widget:

                    MDTextField:
                        icon_left: "account-check"
                        hint_text: "Article"
                        pos_hint: {"center_x": .5 }
                        width: 50
                        font_size: 48
                        on_text: screen_article.num( self )
                    MDLabel:
                        text: "Selected:"
                        font_style: "H4"
                        size_hint_y: None
                        height: '260dp'


                    BoxLayout:
                        orientation: 'horizontal'
                        padding: 10
                        Button:
                            text: 'OK'
                            size_hint_y: 1
                        Button:
                            text: 'List'
                            size_hint_y: 1
                            on_press: Clock.schedule_once(lambda x: app.set_screen(screen_manager, "articlelist"), .3)
                        Button:
                            text: 'Cancel'
                            size_hint_y: 1
                            on_press: Clock.schedule_once(lambda x: app.set_screen(screen_manager, "menu"), .3)

            Screen_articlelist:
                name:  'articlelist'
                id: screen_articlelist
                mylist: list

                BoxLayout:
                    orientation: 'vertical'
                    id: menuBox
                    padding: 20

                    Widget:
                    # paul
                    ScrollView:
                        size_hint: None, None
                        size: "350dp", "400dp"
                        # pos_hint: {"center_x": .5, "center_y": 1.2}
                        MDList:
                            id: list
                            TwoLineAvatarListItem:
                                text: "Sony laptop"
                                secondary_text: "Model x68 "
                                ImageLeftWidget:
                                    source: "sony.jpg"
                            TwoLineAvatarListItem:
                                text: "Iphone 6"
                                secondary_text: "Model 6-I5"
                                ImageLeftWidget:
                                    source: "iPhone.jpg"
                            TwoLineAvatarListItem:
                                text: "Palm"
                                secondary_text: "Model Palm philips"
                                ImageLeftWidget:
                                    source: "palm.jpg"
                            TwoLineAvatarListItem:
                                text: "MacBookAir"
                                secondary_text: "MacBookAir model 3"
                                ImageLeftWidget:
                                    source: "MacBookAir.jpg"


                    BoxLayout:
                        orientation: 'horizontal'
                        padding: 10
                        Button:
                            text: 'OK'
                            size_hint_y: 1
                            text: 'Cancel'
                            size_hint_y: 1
                            on_press: Clock.schedule_once(lambda x: app.set_screen(screen_manager, "menu"), .3)

            Screen_leeg: # dynamic screen
                name:  'leeg'
                id: screen_leeg


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

                ScrollView: # Hamburger menu
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

        manager.current = name_screen

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
        print (self.parent )
        self.parent.parent.parent.parent.dismiss()

    def on_enter_user( self ):
        pass


class Screen_articlelist(Screen):
   mylist = ObjectProperty()
   def __init__(self, **kwargs):
        super(Screen_articlelist,self).__init__(**kwargs)

class Screen_leeg(Screen):
    def __init__(self, **kwargs):
        super(Screen_leeg,self).__init__(**kwargs)

        button = MDFlatButton( text='jaja',
                               on_press=self.doeiets
        )

        card = MDCard(orientation='vertical', pos_hint={
                        'center_x': .5, 'center_y': .5}, size_hint=(.9, .75))
        box = BoxLayout( orientation='horizontal', padding=20)
        self.add_widget(card)
        self.add_widget(box)
        card.add_widget(button)


    def doeiets( *args, **kwargs ):
        sm = args[1].parent.parent.parent

        print ( args[1].parent )
        button = MDFlatButton( text='Paulus')
        obj = args[1].parent
        obj.add_widget(button)



class Screen_menu(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

class Screen_receiving(Screen):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def on_enter_receiveId( self ):
        pass

class Screen_article(Screen):
    numeric = ObjectProperty()
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def num(self, fieldobj):
        input = fieldobj.text
        if len(input) and input[-1] not in ('0123456789'):
            fieldobj.text = input.rstrip(input[-1])

# class nodig voor hamburgermenu
class MDlist(MDList):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

# class test(MDList):
#     def __init__(self, **kwargs):
#         super().__init__(**kwargs)
#         self.add_widget(TwoLineListItem( text= 'dynamic'))

class MainApp(MDApp):
    userId = ObjectProperty()
    menuBoxObj = ObjectProperty()
    def build(self):
        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.accent_palette = "Blue"

        sm = ScreenManager()
        sm.add_widget(Screen_menu(name='menu'))
        sm.add_widget(Screen_menu(name='article'))
        sm.add_widget(Screen_menu(name='receive'))
        sm.add_widget(Screen_menu(name='leeg'))

        screen = Builder.load_string(KV)
        # screen = Builder.load_file('bol.kv')

        return screen

    def set_screen_nav(self, manager, nav_drawer, name_screen):
        manager.current = name_screen
        nav_drawer.set_state("toggle")
    def set_screen(self, manager, name_screen):
        manager.current = name_screen


MainApp().run()