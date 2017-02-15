from kivy.app import App
from kivymd.theming import ThemeManager

from mainwidget import MainWidget


class Lamusga(App):
    theme_cls = ThemeManager()

    def build(self):
        return MainWidget()


if __name__ == "__main__":
    Lamusga().run()
