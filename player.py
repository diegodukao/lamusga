from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen

Builder.load_file('ui/player.kv')


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
            # self.playing.play()

    def stop(self):
        self.playing.stop()
