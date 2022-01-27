import os
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.behaviors import button
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.card import MDCard
import helpers
from navigation_drawer import navigation_helper
from kivy.lang import Builder
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget, MDList
from kivymd.uix.button import MDFlatButton
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivy.metrics import dp
from kivy.event import EventDispatcher
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty, NumericProperty, \
    BooleanProperty, AliasProperty, OptionProperty, \
    ListProperty, ObjectProperty, VariableListProperty, ColorProperty



from kivymd.theming import ThemableBehavior

# Urls':
# Layout: https://kivy.org/doc/stable/guide/widgets.html#
# course: https://www.udemy.com/user/johnelder3/
# course: https://www.udemy.com/course/kivy-mobile-app/learn/lecture/7865250?components=available_coupons%2Cbuy_button%2Cbuy_for_team%2Ccacheable_add_to_cart%2Ccacheable_buy_button%2Ccacheable_deal_badge%2Ccacheable_discount_expiration%2Ccacheable_price_text%2Ccacheable_purchase_text%2Ccurated_for_ufb_notice_context%2Cdeal_badge%2Cdiscount_expiration%2Cgift_this_course%2Cincentives_context%2Cinstructor_links%2Clifetime_access_context%2Cmoney_back_guarantee%2Cprice_text%2Cpurchase_tabs_context%2Cpurchase%2Crecommendation%2Credeem_coupon%2Csidebar_container%2Csubscribe_team_modal_context%2Ctop_companies_notice_context#overview
# course: https://www.udemy.com/course/kivymd-python-build-mobile-apps-using-material-design/learn/lecture/28108484#overview

class WindowManager(ScreenManager):
    def navigation_draw( self, *args):
        print ('jaja')

class Toolbar():
    pass

class Login(Screen):

    # def handle_ok(self, *args, **kwargs ): 
    def handle_ok( input ):     
        if input[0] != 'admin':
            close_button = MDFlatButton(text="Close",on_release=Login.close_dialog)
            more_button = MDFlatButton(text="More")
            dialog = MDDialog(   title = 'Authentification',
                                 text='input:' + input[0] ,
                                 size_hint=( .3, None),
                                 buttons=[ close_button ]
                            )
            dialog.open()
        else:
            sm.current = "Info"

    def close_dialog(self):
        self.parent.parent.parent.parent.dismiss()

    def handle_ok_cancel(self, *arg):
        exit()

    

class Info(Screen):
       
    def handle_ok(self, *arg):
        # sm.transition.direction = ""
        sm.current = 'Dock'

    def handle_ok_cancel(self, *arg):
        sm.current = 'Login'
    
    def handle_list( self ):
        if self.text == 'Unloading':
            sm.current = 'Dock'

class Article(Screen):
       
    def handle_ok(self, *arg):
        pass

    def handle_ok_cancel(self, *arg):
        sm.current = 'Dock'


class Articlelist(Screen):
       
    def handle_ok(self, *arg):
        pass

    def handle_ok_cancel(self, *arg):
        sm.current = 'Info'

    def on_row_press(self, *arg):
        pass

    def on_check_press(self, *arg):
        pass

class Dock(Screen):
       
    def handle_ok(self, *arg):
        sm.current = 'Article'

    def handle_ok_cancel(self, *arg):
        sm.current = 'Info'
  
class DemoApp(MDApp):
    class ContentNavigationDrawer(BoxLayout):
        pass
    class NavigationLayout(BoxLayout):
        pass
    class DrawerList(BoxLayout):
        pass

    def __init__(self, **kwargs):
        super(DemoApp, self).__init__(**kwargs)
        
    def build(self):
        self.theme_cls.theme_style = "Light" 
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.accent_palette = "Blue"
        
        tools_path = os.path.dirname(__file__)
        icons_path = os.path.join(tools_path, 'NanumSquareL.ttf')

        #
        # Login screen
        #
        screen_login = Screen()
        screen_login.name = "Login"

        toolbar_demo = Builder.load_string(helpers.toolbar_demo)
        toolbar_demo.title = 'Inloggen'
        screen_login.add_widget(toolbar_demo)
        
        # test = Builder.load_string(helpers.KV)
        # screen_login.add_widget(test)

        usericon =  Builder.load_string(helpers.usericon)
        screen_login.add_widget(usericon)   

        username = Builder.load_string(helpers.username_input)
        screen_login.add_widget(username)
        # username.bind(on_enter=Login.handle_username)
        # username.bind(on_enter=lambda x:self.handle_username2(username))
        
        password = Builder.load_string(helpers.password_input)
        screen_login.add_widget(password)
        
        box = Builder.load_string(helpers.box)

        button_ok = Builder.load_string(helpers.button_ok) 
        screen_login.add_widget(button_ok)
        # button_ok.bind(on_press=Login.handle_ok( username ))    
        button_ok.bind(on_press=lambda x:Login.handle_ok( [ username.text,  password.text ] ))

        button_cancel = Builder.load_string(helpers.button_cancel)
        button_cancel.bind(on_press=Login.handle_ok_cancel) 
        screen_login.add_widget(button_cancel)
            
        #
        # info screen
        #
        screen_info = Screen()
        screen_info.name = "Info"

        toolbar_demo = Builder.load_string(helpers.toolbar_demo)
        screen_info.add_widget(toolbar_demo)

        card = MDCard(orientation='vertical', pos_hint={
                        'center_x': .5, 'center_y': .5}, size_hint=(.9, .6))

        screen_info.add_widget(card)
        scroll = ScrollView()
        list_view = MDList( pos_hint={'center_x': 0.5, 'center_y': 0.5},
                            size_hint=(0.9, 0.1)    
                        )
        
        # items = ThreeLineListItem(text=str(i) + ' item',
        #                          secondary_text='This is ' + str(i) + 'th item',
        #                          tertiary_text='hello')

        #icons = IconLeftWidget(icon="android") 
        items = OneLineIconListItem(text='Unloading',
                                    on_release=Info.handle_list
                                    )
        #items.add_widget(icons)
        list_view.add_widget(items)

        items = OneLineIconListItem(text='Receiving',
                                    on_release=Info.handle_list)
        list_view.add_widget(items)

       
        

        scroll.add_widget(list_view)
        card.add_widget(scroll)

        button_ok = Builder.load_string(helpers.button_ok)
        button_ok.bind(on_press=Info.handle_ok) 
        screen_info.add_widget(button_ok)
        button_cancel = Builder.load_string(helpers.button_cancel)
        button_cancel.bind(on_press=Info.handle_ok_cancel) 
        screen_info.add_widget(button_cancel)


        #
        # Dock screen
        #
        screen_dock = Screen()
        screen_dock.name = "Dock"
        toolbar_demo = Builder.load_string(helpers.toolbar_demo)
        screen_dock.add_widget(toolbar_demo)

        card = MDCard(orientation='vertical', pos_hint={
                        'center_x': .5, 'center_y': .5}, size_hint=(.9, .4))

        screen_dock.add_widget(card)    
        scroll = ScrollView()
        list_view = MDList( pos_hint={'center_x': 0.5, 'center_y': 0.5},
                            size_hint=(0.9, 0.1)    
                        )
        for i in range(10):
            items = OneLineIconListItem(text='DOCK 1' + str(i + 20))
            list_view.add_widget(items)
           
        scroll.add_widget(list_view)
        card.add_widget(scroll)

        receive_input = Builder.load_string(helpers.receive_input)
        screen_dock.add_widget(receive_input)
    

        button_ok = Builder.load_string(helpers.button_ok)
        button_ok.bind(on_press=Dock.handle_ok) 
        screen_dock.add_widget(button_ok)
        button_cancel = Builder.load_string(helpers.button_cancel)
        button_cancel.bind(on_press=Dock.handle_ok_cancel) 
        screen_dock.add_widget(button_cancel)
        
        #
        # info articleList
        #
        screen_article_list = Screen()
        screen_article_list.name = "Articlelist"
        toolbar_demo = Builder.load_string(helpers.toolbar_demo)
        screen_article_list.add_widget(toolbar_demo)

        db_article = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                 size_hint=(0.9, 0.6),
                                 check=False,
                                 rows_num=10,
                                 column_data=[
                                     ("Article", dp(80)),
                                     ("Desc", dp(40))
                                 ],
                                 row_data=[
                                     ("Burger", "300"),
                                     ("Oats", "200"),
                                     ("Oats", "200"),
                                     ("Oats", "200"),
                                     ("Oats", "200"),
                                     ("Oats", "200"),
                                     ("Oats", "200"),
                                     ("Oats", "200")

                                 ]
                                 )
        db_article.bind(on_row_press=Articlelist.on_row_press)
        db_article.bind(on_check_press=Articlelist.on_check_press)
        screen_article_list.add_widget(db_article)

        button_ok = Builder.load_string(helpers.button_ok)
        button_ok.bind(on_press=Articlelist.handle_ok) 
        screen_article_list.add_widget(button_ok)
        button_cancel = Builder.load_string(helpers.button_cancel)
        button_cancel.bind(on_press=Articlelist.handle_ok_cancel) 
        screen_article_list.add_widget(button_cancel)

        #
        # input article
        #
        screen_article = Screen()
        screen_article.name = "Article"
        toolbar_demo = Builder.load_string(helpers.toolbar_demo)
        screen_article.add_widget(toolbar_demo)
    
        # nh = Builder.load_string(navigation_helper)
        # screen_article.add_widget(nh)

        article_input = Builder.load_string(helpers.article_input)
        screen_article.add_widget(article_input)
        # todo
        article_input.bind(on_enter=lambda instance, x: setattr(button_ok, 'text', x))

        button_ok = Builder.load_string(helpers.button_ok)
        button_ok.bind(on_press=Article.handle_ok) 
        screen_article.add_widget(button_ok)
        button_cancel = Builder.load_string(helpers.button_cancel)
        button_cancel.bind(on_press=Article.handle_ok_cancel) 
        screen_article.add_widget(button_cancel)


        #
        # Screen manager
        #
        global sm  
        sm = Builder.load_string(helpers.windows)
        
        sm.add_widget(screen_login)
        sm.add_widget(screen_info)
        sm.add_widget(screen_article_list)
        sm.add_widget(screen_article)
        sm.add_widget(screen_dock)
        sm.current = "Dock"
        return sm
    
DemoApp().run()