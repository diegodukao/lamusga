from unittest.mock import patch

from main import Player


class PlayerScreenTest:

    @patch('kivy.core.audio.Sound')
    @patch.object('main.SoundLoader', 'load')
    def test_play_method_calls_soundloader_play(self, mock_load, MockSound):
        player = Player()
        player.play()

        mock_sound = MockSound.return_value
