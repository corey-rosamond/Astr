from command import Command


class GreetCommand(Command):
    """Command to greet the user."""

    def execute(self, app, text):
        response = "Hello! How can I assist you today?"
        app.ui.append_transcription(response)
        app.tts.speak(response)
