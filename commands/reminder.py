import threading
import datetime
from command import Command

class ReminderCommand(Command):
    """Command to set reminders."""
    def execute(self, app, text):
        try:
            if "remind me" in text.lower():
                if "in" in text.lower():
                    # Handle "remind me in X time"
                    self._handle_relative_reminder(app, text)
                elif "at" in text.lower():
                    # Handle "remind me at HH:MM"
                    self._handle_absolute_reminder(app, text)
                else:
                    response = "Please specify either a specific time with 'at' or a duration with 'in'."
                    app.ui.append_transcription(response)
                    app.tts.speak(response)
            else:
                response = "I can set reminders if you say something like 'remind me to...' with a time or duration."
                app.ui.append_transcription(response)
                app.tts.speak(response)

        except Exception as e:
            response = f"An error occurred while setting the reminder: {str(e)}"
            app.ui.append_transcription(response)
            app.tts.speak(response)

    def _handle_relative_reminder(self, app, text):
        """Set a reminder for a relative duration (e.g., 'in 10 minutes')."""
        try:
            parts = text.lower().split("remind me in")
            if len(parts) > 1:
                details = parts[1].strip()
                words = details.split()
                if len(words) >= 3:
                    # Extract time amount and unit
                    time_amount = int(words[0])
                    time_unit = words[1].lower()
                    reminder_text = " ".join(words[2:])

                    # Convert the time unit to seconds
                    if "minute" in time_unit:
                        delay = time_amount * 60
                    elif "hour" in time_unit:
                        delay = time_amount * 3600
                    else:
                        response = "I can only understand minutes and hours for reminders."
                        app.ui.append_transcription(response)
                        app.tts.speak(response)
                        return

                    # Schedule the reminder
                    threading.Timer(delay, self.deliver_reminder, args=(app, reminder_text)).start()
                    response = f"Reminder set for {time_amount} {time_unit}(s): {reminder_text}"
                else:
                    response = "I didn't catch the details of the reminder. Please try again."
            else:
                response = "I didn't catch the duration or what you want to be reminded about. Please try again."

        except ValueError:
            response = "I couldn't understand the time duration. Please try again using a number of minutes or hours."
        except Exception as e:
            response = f"An error occurred while setting the reminder: {str(e)}"

        # Provide feedback to the user
        app.ui.append_transcription(response)
        app.tts.speak(response)

    def _handle_absolute_reminder(self, app, text):
        """Set a reminder for an absolute time (e.g., 'at HH:MM')."""
        try:
            parts = text.lower().split("remind me")
            if len(parts) > 1:
                reminder_details = parts[1].strip()
                if "at" in reminder_details:
                    reminder_text, time_part = reminder_details.split("at", 1)
                    reminder_text = reminder_text.strip()
                    time_part = time_part.strip()

                    # Convert time to a datetime object
                    reminder_time = datetime.datetime.strptime(time_part, "%H:%M")
                    now = datetime.datetime.now()
                    reminder_time = reminder_time.replace(year=now.year, month=now.month, day=now.day)

                    # Check if the time is valid (in the future)
                    if reminder_time < now:
                        response = "I cannot set a reminder in the past. Please try again."
                    else:
                        # Schedule the reminder
                        delay = (reminder_time - now).total_seconds()
                        threading.Timer(delay, self.deliver_reminder, args=(app, reminder_text)).start()
                        response = f"Reminder set for {reminder_time.strftime('%I:%M %p')}: {reminder_text}"
                else:
                    response = "Please specify a time using 'at', like 'remind me to drink water at 3:30 PM'."
            else:
                response = "I didn't catch the details of the reminder. Please try again."

        except ValueError:
            response = "I couldn't understand the time format. Please use 'HH:MM' in 24-hour format."
        except Exception as e:
            response = f"An error occurred while setting the reminder: {str(e)}"

        # Provide feedback to the user
        app.ui.append_transcription(response)
        app.tts.speak(response)

    def deliver_reminder(self, app, reminder_text):
        """Deliver the reminder."""
        response = f"Reminder: {reminder_text}"
        app.ui.append_transcription(response)
        app.tts.speak(response)
