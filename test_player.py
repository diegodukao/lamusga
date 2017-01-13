from unittest.mock import patch

from main import Player


@patch('main.SoundLoader.load')
def test_play_method_calls_soundloader_play(mock_load):
    player = Player()
    player.play()

    mock_load.assert_called_with('music.mp3')
    mock_load.return_value.play.assert_called_with()
