import tkinter as tk
from threading import Thread
from time import sleep
from astr_ui import AstrUI
from stt import AstrSTT
from tts import AstrTTS

class AstrApp:
    def __init__(self):
        """Main class to initialize the application and manage components."""
        self.root = tk.Tk()
        self.ui = AstrUI(self.root)
        self.tts = AstrTTS()
        self.stt = AstrSTT(self.ui, model="medium")

        # Wake word and commands
        self.wake_word = "aster"
        self.commands = {
            "what is your name": self.handle_name,
            "quit": self.handle_quit,
        }

    def handle_name(self):
        """Respond to the name query."""
        response = "My name is Aster, your assistant."
        self.ui.append_transcription(response)
        self.tts.speak(response)

    def handle_quit(self):
        """Handle the quit command."""
        response = "Goodbye!"
        self.ui.append_transcription(response)
        self.tts.speak(response)
        self.root.quit()

    def process_command(self, text):
        """Process the user's command after the wake word."""
        for command, handler in self.commands.items():
            if command in text.lower():
                handler()
                return
        # Default response for unrecognized commands
        response = "I'm sorry, I didn't understand that."
        self.ui.append_transcription(response)
        self.tts.speak(response)

    def listen_for_wake_word(self):
        """Listen for the wake word and process commands."""
        self.stt.recorder.listen_in_background(
            self.stt.source, self.stt.record_callback(self.stt.data_queue),
            phrase_time_limit=self.stt.record_timeout
        )
        self.ui.update_listening_status(True)

        while True:
            try:
                self.stt.process_transcription()
                if self.stt.transcription:
                    latest_text = self.stt.transcription[-1].lower()
                    if self.wake_word in latest_text:
                        self.ui.append_transcription("Wake word detected. Listening for command...")
                        self.tts.speak("I'm listening.")

                        # Process the next command
                        sleep(1)  # Allow a slight delay before command processing
                        if len(self.stt.transcription) > 1:
                            command_text = self.stt.transcription[-1]
                            self.process_command(command_text)

            except KeyboardInterrupt:
                break

    def run(self):
        """Run the application."""
        stt_thread = Thread(target=self.listen_for_wake_word, daemon=True)
        stt_thread.start()
        self.root.mainloop()


if __name__ == "__main__":
    app = AstrApp()
    app.run()
