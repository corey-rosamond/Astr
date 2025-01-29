import unittest
from unittest.mock import Mock
from commands.quit_command import QuitCommand


class TestQuitCommand(unittest.TestCase):
    def test_execute(self):
        app = Mock()
        command = QuitCommand()
        command.execute(app, "quit")

        app.ui.append_transcription.assert_called_with("Goodbye!")
        app.tts.speak.assert_called_with("Goodbye!")
        app.root.quit.assert_called_once()


if __name__ == '__main__':
    unittest.main()
