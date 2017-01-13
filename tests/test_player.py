from unittest.mock import patch

from main import Player


@patch('kivy.core.audio.Sound')
@patch('main.SoundLoader.load')
def test_play_method_calls_soundloader_play(mock_load, MockSound):
    player = Player()
    player.play()

    mock_load.assert_called_with('music.mp3')
    mock_load.return_value.play.assert_called_with()
