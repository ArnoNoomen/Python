from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ListProperty, StringProperty



class MainScreenManager(ScreenManager):
    def build(self):
        pass

class LoginScreen(Screen):
    entered_email_address = StringProperty('')
    entered_password = StringProperty('')

    def check_input(self):
        text_input_email = self.ids['ti_email'].text
        text_input_password = self.ids['ti_password'].text

        self.entered_email_address = text_input_email
        self.entered_password = text_input_password

        """
        the values in this part are printed out
        print self.manager
        print self.manager.screens
        print self.manager.get_screen('HomeScreen').email_address
        print self.manager.get_screen('HomeScreen').password
        """

        self.manager.current = 'HomeScreen'

class HomeScreen(Screen):
    email_address = StringProperty()
    password = StringProperty()

    def __init__(self, *args, **kwargs):
        super(HomeScreen, self).__init__(*args, **kwargs)