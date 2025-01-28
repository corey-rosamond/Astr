import re
from threading import Timer
from handlers.command import Command
from datetime import datetime, timedelta


class ReminderCommand(Command):
    """Command to set a reminder."""
    keywords = ["remind", "reminder", "set a reminder"]

    def execute(self, app, text: str):
        match = re.search(r"in (\d+) (seconds|minutes|hours)", text.lower())
        if match:
            amount, unit = int(match.group(1)), match.group(2)
            reminder_text = text.lower().split("to", 1)[-1].strip()

            # Calculate delay
            if unit == "seconds":
                delay = amount
            elif unit == "minutes":
                delay = amount * 60
            elif unit == "hours":
                delay = amount * 3600

            # Schedule reminder
            Timer(delay, self.deliver_reminder, args=[app, reminder_text]).start()
            response = f"Reminder set for {amount} {unit}."
        else:
            response = "Sorry, I couldn't understand the time for the reminder."

        app.ui.append_transcription(response)
        app.tts.speak(response)

    @staticmethod
    def deliver_reminder(app, reminder_text):
        """Deliver the reminder."""
        response = f"Reminder: {reminder_text}"
        app.ui.append_transcription(response)
        app.tts.speak(response)
