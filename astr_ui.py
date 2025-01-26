import tkinter as tk
from tkinter import ttk


class AstrUI:
    """ This is the base AstrUI object"""

    def __init__(self, root):
        self.root = root
        self.root.title("Astr Assistant")
        self.root.geometry("600x400")

        self.listening_frame = ttk.Frame(self.root)
        self.listening_frame.pack(pady=10)

        self.listening_label = ttk.Label(self.listening_frame, text="Listening Status:", font=("Arial", 14))
        self.listening_label.pack(side=tk.LEFT, padx=10)

        self.listening_indicator = ttk.Label(self.listening_frame, text="OFF", font=("Arial", 14), foreground="red")
        self.listening_indicator.pack(side=tk.LEFT)

        self.transcription_frame = ttk.Frame(self.root)
        self.transcription_frame.pack(fill=tk.BOTH, expand=True, pady=10, padx=10)

        self.transcription_label = ttk.Label(self.transcription_frame, text="Real-Time Transcription:",
                                             font=("Arial", 12))
        self.transcription_label.pack(anchor=tk.W)

        self.transcription_text = tk.Text(self.transcription_frame, wrap=tk.WORD, font=("Arial", 10))
        self.transcription_text.pack(fill=tk.BOTH, expand=True)
        self.transcription_text.config(state=tk.DISABLED)

        self.footer_frame = ttk.Frame(self.root)
        self.footer_frame.pack(fill=tk.X, pady=5)

        self.quit_button = ttk.Button(self.footer_frame, text="Quit", command=self.root.quit)
        self.quit_button.pack(side=tk.RIGHT, padx=10)

    def update_listening_status(self, status):
        if status:
            self.listening_indicator.config(text="ON", foreground="green")
        else:
            self.listening_indicator.config(text="OFF", foreground="red")

    def append_transcription(self, text):
        self.transcription_text.config(state=tk.NORMAL)
        self.transcription_text.insert(tk.END, text + "\n")
        self.transcription_text.see(tk.END)
        self.transcription_text.config(state=tk.DISABLED)
