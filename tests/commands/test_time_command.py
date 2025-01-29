import unittest
from unittest.mock import Mock
from commands.time_command import TimeCommand
from datetime import datetime


class TestTimeCommand(unittest.TestCase):
    def test_execute(self):
        app = Mock()
        command = TimeCommand()
        command.execute(app, "what time is it")

        current_time = datetime.now().strftime("%I:%M %p")
        response = f"The current time is {current_time}."

        app.ui.append_transcription.assert_called_with(response)
        app.tts.speak.assert_called_with(response)


if __name__ == '__main__':
    unittest.main()
