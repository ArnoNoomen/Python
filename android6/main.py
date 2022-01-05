from kivy.app import App
from kivy.uix.relativelayout import RelativeLayout

class Test ( RelativeLayout ):

    def _init_(self, **kwargs ):
        super(Test, self )._init_( **kwargs )

class TestApp(App):
    def build(self):
        return Test()

if __name__ == '__main__':
    TestApp().run()