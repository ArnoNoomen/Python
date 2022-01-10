from kivy.uix.behaviors import button
from kivymd.app import MDApp
from kivy.uix.screenmanager import ScreenManager, Screen
import helpers
from kivy.lang import Builder
from kivymd.uix.list import OneLineListItem, MDList, TwoLineListItem, ThreeLineListItem
from kivymd.uix.list import OneLineIconListItem, IconLeftWidget
from kivymd.uix.button import MDFlatButton
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog
from kivy.metrics import dp
from kivy.event import EventDispatcher

class WindowManager(ScreenManager):
    pass

class Toolbar():
    def navigation_draw():
        print ('jaja')

class Login(Screen):

    def handle_ok(self, *args): 
        print ( self.root.ids )
        close_button = MDFlatButton(text="Close",on_release=Login.close_dialog)
        more_button = MDFlatButton(text="More")
        dialog = MDDialog( text= 'jaja1' ,
                           buttons=[ close_button ]
                         )
        
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
    
    def build(self):
        self.theme_cls.theme_style = "Light" 
        self.theme_cls.primary_palette = "Indigo"
        self.theme_cls.accent_palette = "Blue"
        
        #
        # Login screen
        #
        screen_login = Screen()
        screen_login.name = "Login"

        toolbar_demo = Builder.load_string(helpers.toolbar_demo)
        toolbar_demo.title = 'Inloggen'
        screen_login.add_widget(toolbar_demo)
        
        test = Builder.load_string(helpers.KV)
        screen_login.add_widget(test)

        username = Builder.load_string(helpers.username_input)
        screen_login.add_widget(username)
        # username.bind(on_enter=Login.handle_username)
        # username.bind(on_enter=lambda x:self.handle_username2(username))
        
        password = Builder.load_string(helpers.password_input)
        screen_login.add_widget(password)
        button_ok = Builder.load_string(helpers.button_ok)
        # button_ok.bind(on_press=Login.handle_ok)    
        button_ok.bind(on_press=lambda x:Login.handle_ok(username))
         
        screen_login.add_widget(button_ok)
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

        db_info = MDDataTable(  pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                size_hint=(0.9, 0.7),
                                check=False,
                                rows_num=10,
                                column_data=[
                                     ("Procedure", dp(80)),
                                     ("Desc", dp(40))
                                 ],
                                 row_data=[
                                     ("Unloading", "300"),
                                     ("Receiving", "200"),
                                     ("Receiving MDA", "200")
                                 ]
                                
                                 )
        db_info.bind(on_row_press=Articlelist.on_row_press)
        db_info.bind(on_check_press=Articlelist.on_check_press)
        screen_info.add_widget(db_info)



        # scroll = ScrollView()
        # list_view = MDList( pos_hint={'center_x': 0.5, 'center_y': 0.5},
        #                     size_hint=(0.9, 0.6)
                            
        #                 )
        # for i in range(20):

        #     # items = ThreeLineListItem(text=str(i) + ' item',
        #     #                          secondary_text='This is ' + str(i) + 'th item',
        #     #                          tertiary_text='hello')

        #     icons = IconLeftWidget(icon="android")
        #     items = OneLineIconListItem(text=str(i) + ' item')
        #     items.add_widget(icons)
        #     list_view.add_widget(items)

        # scroll.add_widget(list_view)
        # screen_info.add_widget(scroll)
        
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

        receive_input = Builder.load_string(helpers.receive_input)
        screen_dock.add_widget(receive_input)
        dock_input = Builder.load_string(helpers.dock_input)
        screen_dock.add_widget(dock_input)
        
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
        toolbar_demo.title = 'Article receipt'
        screen_article.add_widget(toolbar_demo)

        article_input = Builder.load_string(helpers.article_input)
        screen_article.add_widget(article_input)

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
        sm.current = "Login"
        return sm
    
DemoApp().run()