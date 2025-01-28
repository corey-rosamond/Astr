from handlers.command import Command


class GreetCommand(Command):
    """Command to greet the user."""
    keywords = ["hello", "hi", "greet", "hey"]

    def execute(self, app, text: str):
        response = "Hello! How can I assist you today?"
        app.ui.append_transcription(response)
        app.tts.speak(response)
