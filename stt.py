import numpy as np
import speech_recognition as sr
import whisper
import torch
from scipy.signal import butter, lfilter
from datetime import datetime, timedelta
from queue import Queue
from time import sleep
from sys import platform

class AstrSTT:
    def __init__(self, ui, model="medium", non_english=False, energy_threshold=1000, record_timeout=2.0, phrase_timeout=3.0, default_microphone='pulse'):
        self.ui = ui
        self.model = model
        self.non_english = non_english
        self.energy_threshold = energy_threshold
        self.record_timeout = record_timeout
        self.phrase_timeout = phrase_timeout
        self.default_microphone = default_microphone
        self.phrase_time = None
        self.data_queue = Queue()
        self.transcription = []
        self.displayed_transcription = set()
        self.recorder = sr.Recognizer()
        self.source = self.setup_microphone()
        if self.source:
            self.audio_model = self.load_model()
            self.initialize_recorder()

    def load_model(self):
        model_name = self.model
        if self.model != "large" and not self.non_english:
            model_name += ".en"
        return whisper.load_model(model_name)

    def setup_microphone(self):
        if 'linux' in platform:
            mic_name = self.default_microphone
            if mic_name is None or mic_name == 'list':
                print("Available microphone devices are:")
                for index, name in enumerate(sr.Microphone.list_microphone_names()):
                    print(f"Microphone with name \"{name}\" found")
                return None
            else:
                for index, name in enumerate(sr.Microphone.list_microphone_names()):
                    if mic_name in name:
                        return sr.Microphone(sample_rate=16000, device_index=index)
        return sr.Microphone(sample_rate=16000)

    def initialize_recorder(self):
        self.recorder.energy_threshold = self.energy_threshold
        self.recorder.dynamic_energy_threshold = False
        with self.source:
            self.recorder.adjust_for_ambient_noise(self.source)

    @staticmethod
    def butter_bandpass(lowcut, highcut, fs, order=2):
        nyquist = 0.5 * fs
        low = max(min(lowcut / nyquist, 0.99), 0.01)
        high = max(min(highcut / nyquist, 0.99), 0.01)
        if not (0 < low < high):
            raise ValueError(f"Invalid bandpass filter frequencies: low={low}, high={high} (normalized). Ensure 0 < low < high < Nyquist.")
        b, a = butter(order, [low, high], btype='band')
        return b, a

    @staticmethod
    def bandpass_filter(data, lowcut=50, highcut=8000, fs=16000, order=2):
        try:
            b, a = AstrSTT.butter_bandpass(lowcut, highcut, fs, order=order)
            filtered_data = lfilter(b, a, data)
            return filtered_data.astype(np.float32)
        except ValueError as e:
            print(f"Error in bandpass_filter: {e}")
            return data

    @staticmethod
    def record_callback(data_queue):
        def callback(_, audio: sr.AudioData):
            data = audio.get_raw_data()
            data_queue.put(data)
        return callback

    def process_transcription(self):
        now = datetime.utcnow()
        phrase_complete = False

        if not self.data_queue.empty():
            if self.phrase_time and now - self.phrase_time > timedelta(seconds=self.phrase_timeout):
                phrase_complete = True

            self.phrase_time = now

            audio_data = b''
            while not self.data_queue.empty():
                audio_data += self.data_queue.get()

            audio_np = np.frombuffer(audio_data, dtype=np.int16).astype(np.float32) / 32768.0

            audio_np = self.bandpass_filter(audio_np)

            result = self.audio_model.transcribe(audio_np, fp16=torch.cuda.is_available())
            text = result['text'].strip()

            if phrase_complete and text:
                if text not in self.displayed_transcription:
                    self.transcription.append(text)
                    self.displayed_transcription.add(text)
                    self.ui.append_transcription(text)

    def run(self):
        if not self.source:
            return

        self.recorder.listen_in_background(self.source, self.record_callback(self.data_queue),
                                           phrase_time_limit=self.record_timeout)
        self.ui.update_listening_status(True)

        while True:
            try:
                self.process_transcription()
                sleep(0.25)
            except KeyboardInterrupt:
                break

        self.ui.update_listening_status(False)
