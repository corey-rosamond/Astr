from handlers.command import Command


class QuitCommand(Command):
    """Command to quit the application."""
    keywords = ["quit", "exit", "close", "goodbye"]

    def execute(self, app, text: str):
        response = "Goodbye!"
        app.ui.append_transcription(response)
        app.tts.speak(response)
        app.root.quit()
