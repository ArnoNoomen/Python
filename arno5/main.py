from threading import Thread
from time import sleep

from kivy.app import App
from kivy.lang import Builder
from kivy.factory import Factory
from kivy.clock import mainthread
from kivy.properties import ListProperty, BooleanProperty



KV = '''
FloatLayout:
    Label:
        opacity: 1 if app.refreshing or rv.scroll_y > 1 else 0
        size_hint_y: None
        pos_hint: {'top': 1}
        text: 'Refreshing…' if app.refreshing else 'Pull down to refresh'
    RecycleView:
        id: rv
        data: app.data
        viewclass: 'Row'
        do_scroll_y: True
        do_scroll_x: False
        on_scroll_y: app.check_pull_refresh(self, grid)
        RecycleGridLayout:
            id: grid
            cols: 1
            size_hint_y: None
            height: self.minimum_height
            default_size: 0, 36
            default_size_hint: 1, None
<Row@Label>:
    _id: 0
    text: ''
    canvas:
        Line:
            rectangle: self.pos + self.size
            width: 0.6
'''

class Application(App):
    data = ListProperty([])
    refreshing = BooleanProperty()

    def build(self):
        self.refresh_data()
        return Builder.load_string(KV)

    def check_pull_refresh(self, view, grid):

        max_pixel = 200
        to_relative = max_pixel / (grid.height - view.height)
        if view.scroll_y < 1.0 + to_relative or self.refreshing:
            return

        self.refresh_data()

    def refresh_data(self):
        Thread(target=self._refresh_data).start()

    def _refresh_data(self):
        self.refreshing = True
        sleep(2)

        self.append_data([
            {'_id': i, 'text': 'hello {}'.format(i)}
            for i in range(len(self.data), len(self.data) + 50)
        ])
        self.refreshing = False

    @mainthread
    def append_data(self, data):
        self.data = self.data + data


if __name__ == "__main__":
    Application().run()
