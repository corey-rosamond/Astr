# File: commands/good_morning_command.py

from handlers.command import Command


class GoodMorningCommand(Command):
    """Command to respond to 'good morning'."""
    keywords = ["good morning"]

    def execute(self, app, text: str):
        response = "Good morning! How can I assist you today?"
        app.ui.append_transcription(response)
        app.tts.speak(response)
