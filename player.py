from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.screenmanager import Screen

Builder.load_file('ui/player.kv')


class Player(Screen):
    playing = ObjectProperty()
    state = StringProperty("stop")

    def play_pause(self):
        try:
            self.state = self.playing.state
        except AttributeError:
            self.state = "stop"

        if self.state == "stop":
            self.playing = SoundLoader.load('music.mp3')
            self.playing.volume = 0
            self.playing.play()
            self.state = "play"
        else:
            self.playing.stop()
            self.state = "stop"

    def stop(self):
        self.playing.stop()
        self.state = "stop"
