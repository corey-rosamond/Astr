from datetime import datetime
from handlers.command import Command


class TimeCommand(Command):
    """Command to get the current time."""
    keywords = ["time", "current time", "what time is it"]

    def execute(self, app, text: str):
        current_time = datetime.now().strftime("%I:%M %p")
        response = f"The current time is {current_time}."
        app.ui.append_transcription(response)
        app.tts.speak(response)
