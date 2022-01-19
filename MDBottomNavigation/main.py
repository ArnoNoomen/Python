from kivymd.app import MDApp
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import NumericProperty, StringProperty
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.textfield import MDTextField


class MyContent(BoxLayout):
    pass

popup = Popup(title='Test popup',
    content=Label(text='Hello world'),
    size_hint=(None, None), size=(400, 400)
)

class MDTextFieldPersian(MDTextField):
    max_chars = NumericProperty(5)  # maximum character allowed
    str = StringProperty()

    def __init__(self, **kwargs):
        super(MDTextFieldPersian, self).__init__(**kwargs)
        self.text = "hallo"

    def insert_text(self, substring, from_undo=False):
        print(substring)
        return

class MainApp(MDApp):
    dialog = None
    dropdown = None  
      

    def show_data(self): 
        oke_button = MDFlatButton(text='Oke', on_release=self.close_dialog)
        global arno
        arno = MDDialog(title='MDDialog', text='Helloworld', size_hint=(0.7, 1), buttons=[oke_button])
        arno.open()

    def close_dialog(*args):
         arno.dismiss()
 #       print(args[1].parent)
 #       print(args[1].parent.parent)
 #       print(args[1].parent.parent.parent)
 #       print(args[1].parent.parent.parent.parent)
 #       args[1].parent.parent.parent.parent.dismiss()
 #       #self.dialog.dismiss()

    def check_text(self, text):
        print(text)

    def check_text1(self, text):
        print(text)

    def print_ids(self, ii):
        print(ii)

    def set_text(self, text):
        print(text)
        self.root.ids.mdlabel.text = text
        # self.root.ids.special_gridlayout.ids.special_label.text ?
        print(self.root.ids.mdlabel.text)

    def set_error_message(self, instance_textfield):
        print(instance_textfield)
        self.screen.ids.text_field_error.error = True

    def popup1(self):
        popup.open()
        self.root.ids.label2.text = "jajaja"

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                text=str(self.root.size),
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                    MDFlatButton(
                        text="DISCARD",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                    ),
                ],
            )
        print(self.dialog)

        self.dialog.open()
        

    def on_start(self):
        self.dropdown = MDDropdownMenu(width_mult=4)
        print(self.dropdown)
        for i in range(6):
            self.dropdown.items.append(
                {"viewclass":"MDMenuItem","text":"Option " + str(i), "callback": self.option_callback}
            )
        names = ["Option 1", "Option 2", "Option 3"]

        for name in names:
            panel = MDExpansionPanel(
                content=MyContent(),
                panel_cls=MDExpansionPanelOneLine(text=name))
            self.root.ids.panel_container.add_widget(panel)

    def option_callback(self, text_of_the_option):
        print(text_of_the_option)

MainApp().run()
