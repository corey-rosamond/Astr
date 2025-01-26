from command import Command


class QuitCommand(Command):
    """Command to quit the application."""

    def execute(self, app, text):
        response = "Goodbye!"
        app.ui.append_transcription(response)
        app.tts.speak(response)
        app.root.quit()
