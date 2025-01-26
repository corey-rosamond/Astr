import logging
from datetime import datetime
import sounddevice as sd
from TTS.api import TTS


class AstrTTS:
    def __init__(self, model_name="tts_models/en/ljspeech/tacotron2-DDC"):
        """Initialize the Text-to-Speech (TTS) module using Coqui TTS."""
        # Setup logging
        log_filename = f"astr_tts_log_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"
        logging.basicConfig(filename=log_filename, level=logging.INFO, format='%(asctime)s - %(message)s')

        self.model_name = model_name
        self.tts = None

        # Initialize the TTS model
        self._initialize_tts()

    def _initialize_tts(self):
        """Load the TTS model."""
        try:
            logging.info(f"Loading TTS model: {self.model_name}")
            self.tts = TTS(self.model_name)
            logging.info("TTS model loaded successfully.")
        except Exception as e:
            logging.error(f"Failed to load TTS model: {e}")
            raise RuntimeError("Failed to initialize TTS.")

    def speak(self, text):
        """Speak the given text using Coqui TTS with real-time audio playback."""
        try:
            logging.info(f"Speaking: {text}")

            # Generate audio data; return waveform only (default sample rate)
            waveform = self.tts.tts(text, return_type="np")
            sample_rate = 22050  # Common default for TTS models; adjust if needed

            # Log output for debugging
            logging.info(f"Generated waveform with length {len(waveform)}")

            # Play audio using sounddevice
            sd.play(waveform, samplerate=sample_rate)
            sd.wait()  # Wait until playback is finished
            logging.info("Audio playback finished.")
        except Exception as e:
            logging.error(f"Error while speaking: {e}")
            print(f"Error while speaking: {e}")


if __name__ == "__main__":
    tts = AstrTTS()
    try:
        tts.speak("Hello, this is a test of the Aster text-to-speech module using Coqui TTS.")
    except KeyboardInterrupt:
        logging.info("Program interrupted.")
