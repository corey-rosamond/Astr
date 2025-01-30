# /commands/timer_command.py

import re
from threading import Timer
from handlers.command import Command

class TimerCommand(Command):
    """Command to set a timer."""
    keywords = ["timer", "set a timer", "start timer"]

    def execute(self, app, text: str):
        match = re.search(r"in (\d+) (seconds|minutes|hours)", text.lower())
        if match:
            amount, unit = int(match.group(1)), match.group(2)

            # Calculate delay
            if unit == "seconds":
                delay = amount
            elif unit == "minutes":
                delay = amount * 60
            elif unit == "hours":
                delay = amount * 3600

            # Schedule timer
            Timer(delay, self.timer_finished, args=[app]).start()
            response = f"Timer set for {amount} {unit}."
        else:
            response = "Sorry, I couldn't understand the time for the timer."

        app.ui.append_transcription(response)
        app.tts.speak(response)

    @staticmethod
    def timer_finished(app):
        """Notify when the timer is finished."""
        response = "Timer finished!"
        app.ui.append_transcription(response)
        app.tts.speak(response)
