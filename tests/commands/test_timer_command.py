import unittest
from unittest.mock import Mock, patch
from commands.reminder_command import ReminderCommand


class TestReminderCommand(unittest.TestCase):
    def setUp(self):
        self.app = Mock()
        self.command = ReminderCommand()

    @patch('commands.reminder_command.Timer')
    def test_execute_valid_reminder(self, mock_timer):
        # Test a valid reminder command
        self.command.execute(self.app, "remind me in 10 seconds to check the oven")

        # Check if the transcription and TTS were called with the correct response
        self.app.ui.append_transcription.assert_called_with("Reminder set for 10 seconds.")
        self.app.tts.speak.assert_called_with("Reminder set for 10 seconds.")

        # Check if the Timer was set correctly
        mock_timer.assert_called_once_with(10, self.command.deliver_reminder, args=[self.app, "check the oven"])

    def test_execute_invalid_reminder(self):
        # Test an invalid reminder command
        self.command.execute(self.app, "remind me to check the oven")

        # Check if the transcription and TTS were called with the correct response
        self.app