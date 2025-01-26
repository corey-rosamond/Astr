# Aster - A Local Voice Assistant

Aster is a local, privacy-first voice assistant designed to work entirely offline. It leverages cutting-edge technologies such as OpenAI Whisper for speech-to-text (STT) and Coqui TTS for text-to-speech (TTS). The application is designed to be modular and extendable, allowing developers to add new commands seamlessly.

---

## Features

- **Local Operation**: No internet connection required; all operations are performed locally to ensure user privacy.
- **English-only STT**: Speech recognition is restricted to English for better accuracy.
- **Command System**: Dynamically loads commands from a `commands/` directory. Each command is a separate file and extends a base `Command` class.
- **Reminders**: Includes support for time-based reminders and relative reminders (e.g., "Remind me in 10 minutes to drink water").
- **Customizable Wake Word**: Uses "aster" as the wake word by default.
- **Interactive GUI**: Built with Tkinter, provides real-time transcription and a visual listening indicator.

---

## Project Structure

```
Aster/
├── main.py              # Entry point for the application
├── astr_ui.py           # GUI implementation
├── stt.py               # Speech-to-text processing
├── tts.py               # Text-to-speech implementation
├── command.py           # Base Command class
├── commands/            # Directory for individual command files
│   ├── greet_command.py # Example greet command
│   ├── quit_command.py  # Command to quit the application
│   ├── reminder_command.py # Handles reminders
├── requirements.txt     # Dependencies for the project
├── readme.md            # Documentation
├── .gitignore           # Ignored files for version control
```

---

## Setup and Installation

### Prerequisites
- Python 3.10 or higher
- Ubuntu 22.04 or compatible Linux system

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/aster.git
   cd aster
   ```

2. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

---

## Adding New Commands

1. Create a new Python file in the `commands/` directory, e.g., `my_command.py`.
2. Extend the `Command` class from `command.py`.
3. Implement the `execute` method:

```python
from command import Command

class MyCommand(Command):
    def execute(self, app, text):
        response = "This is my custom command."
        app.ui.append_transcription(response)
        app.tts.speak(response)
```

4. The command will be loaded automatically when the application starts.

---

## Key Dependencies

- [OpenAI Whisper](https://github.com/openai/whisper): Speech-to-text engine
- [Coqui TTS](https://github.com/coqui-ai/TTS): Text-to-speech engine
- [Tkinter](https://docs.python.org/3/library/tk.html): GUI framework

---

## .gitignore

The following `.gitignore` file is included to exclude unnecessary files from version control:

```
# Byte-compiled / optimized / DLL files
__pycache__/
*.py[cod]
*$py.class

# C extensions
*.so

# Distribution / packaging
.Python
build/
dist/
*.egg-info/
.eggs/

# PyCharm project files
.idea/
*.iml

# Virtual environments
venv/

# Logs
*.log

# OS files
.DS_Store
Thumbs.db
```

---

## Future Enhancements

- Add multi-language support.
- Implement additional commands (e.g., weather updates, task management).
- Improve TTS voices for more natural sound.
- Enhance the GUI for better user interaction.

---

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

---

## License
This project is licensed under the MIT License. See the LICENSE file for details.
