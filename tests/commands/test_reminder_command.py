import unittest
from unittest.mock import Mock
from commands.reminder_command import ReminderCommand


class TestReminderCommand(unittest.TestCase):
    def test_execute_valid(self):
        app = Mock()
        command = ReminderCommand()
        command.execute(app, "remind me in 10 seconds to check the oven")

        app.ui.append_transcription.assert_called_with("Reminder set for 10 seconds.")
        app.tts.speak.assert_called_with("Reminder set for 10 seconds.")

    def test_execute_invalid(self):
        app = Mock()
        command = ReminderCommand()
        command.execute(app, "remind me to check the oven")

        app.ui.append_transcription.assert_called_with("Sorry, I couldn't understand the time for the reminder.")
        app.tts.speak.assert_called_with("Sorry, I couldn't understand the time for the reminder.")


if __name__ == '__main__':
    unittest.main()
