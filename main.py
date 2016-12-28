from kivy.app import App
from kivymd.theming import ThemeManager


class Lamusga(App):
    theme_cls = ThemeManager()


if __name__ == "__main__":
    Lamusga().run()
