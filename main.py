from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.uix.screenmanager import Screen
from kivymd.theming import ThemeManager


class Player(Screen):
    def play(self):
        sound = SoundLoader.load('music.mp3')
        sound.play()


class Lamusga(App):
    theme_cls = ThemeManager()


if __name__ == "__main__":
    Lamusga().run()
