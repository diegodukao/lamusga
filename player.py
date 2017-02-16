from kivy.core.audio import SoundLoader
from kivy.lang import Builder
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import Screen

Builder.load_file('ui/player.kv')


class FileDialog(FloatLayout):
    load = ObjectProperty()
    cancel = ObjectProperty()


class Player(Screen):
    playing = ObjectProperty()
    state = StringProperty("stop")

    def play_pause(self):
        try:
            self.state = self.playing.state
        except AttributeError:
            self.state = "stop"

        if self.state == "stop":
            self.playing.play()
            self.state = "play"
        else:
            self.playing.stop()
            self.state = "stop"

    def play(self, filepath):
        self.playing = SoundLoader.load(filepath)
        self.playing.bind(on_stop=self.on_stop_callback)
        self.playing.volume = 0.1
        self.playing.play()
        self.state = "play"

    def dismiss_popup(self):
        self._popup.dismiss()

    def open_file_dialog(self):
        content = FileDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load File", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        self.play(filename[0])
        self.dismiss_popup()

    def on_stop_callback(self, obj):
        self.state = "stop"
