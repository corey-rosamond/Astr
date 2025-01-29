import unittest
from unittest.mock import Mock
from commands.greet_command import GreetCommand


class TestGreetCommand(unittest.TestCase):
    def test_execute(self):
        app = Mock()
        command = GreetCommand()
        command.execute(app, "hello")

        app.ui.append_transcription.assert_called_with("Hello! How can I assist you today?")
        app.tts.speak.assert_called_with("Hello! How can I assist you today?")


if __name__ == '__main__':
    unittest.main()

