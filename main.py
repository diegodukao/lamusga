from kivy.app import App
from kivy.core.audio import SoundLoader
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen
from kivymd.theming import ThemeManager


class Player(Screen):
    playing = ObjectProperty()

    def play(self):
        try:
            state = self.playing.state
        # tests missing
        except AttributeError:
            state = "stop"

        if state == "stop":
            self.playing = SoundLoader.load('music.mp3')
            self.playing.play()

    def stop(self):
        self.playing.stop()


class Lamusga(App):
    theme_cls = ThemeManager()


if __name__ == "__main__":
    Lamusga().run()
