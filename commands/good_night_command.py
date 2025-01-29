# File: commands/good_night_command.py

from handlers.command import Command


class GoodNightCommand(Command):
    """Command to respond to 'good night'."""
    keywords = ["good night"]

    def execute(self, app, text: str):
        response = "Good night! Sleep well and sweet dreams!"
        app.ui.append_transcription(response)
        app.tts.speak(response)
