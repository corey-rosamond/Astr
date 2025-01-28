import tkinter as tk
from threading import Thread
from time import sleep
from playsound import playsound
from astr_ui import AstrUI
from stt import AstrSTT
from tts import AstrTTS
from handlers.command_handler import CommandHandler


class AstrApp:
    def __init__(self):
        """Main class to initialize the application and manage components."""
        self.root = tk.Tk()
        self.ui = AstrUI(self.root)
        self.tts = AstrTTS()
        self.stt = AstrSTT(self.ui, model="medium")

        # Wake word and commands
        self.wake_word = "aster"
        self.is_listening = False

        self.start_listening_sound = "assets/start_listening.mp3"
        self.stop_listening_sound = "assets/stop_listening.mp3"

        self.command_handler = CommandHandler(self)

    def process_transcription(self):
        """Process transcription for wake word and commands."""
        if not self.stt.transcription:
            return  # No transcription to process

        latest_text = self.stt.transcription[-1].strip().lower()

        if not self.is_listening and self.wake_word in latest_text:
            # Wake word detected
            self.is_listening = True
            playsound(self.start_listening_sound)
            self.ui.append_transcription("Wake word detected. Listening for command...")

        elif self.is_listening:
            # Process command
            self.command_handler.execute_command(latest_text)
            self.is_listening = False
            playsound(self.stop_listening_sound)

    def start_stt_thread(self):
        """Start the STT process in a background thread."""

        def run_stt():
            self.stt.run()

        stt_thread = Thread(target=run_stt, daemon=True)
        stt_thread.start()

    def update_ui(self):
        """Update the UI regularly to process transcriptions."""
        self.process_transcription()
        self.root.after(100, self.update_ui)  # Schedule the next UI update

    def run(self):
        """Run the main application."""
        self.start_stt_thread()  # Start STT in the background
        self.update_ui()  # Start UI update loop
        self.root.mainloop()  # Run the main loop in the main thread


if __name__ == "__main__":
    app = AstrApp()
    app.run()
