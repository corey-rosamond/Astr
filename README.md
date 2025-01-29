# Astr Voice Assistant

Astr is a voice assistant application that uses speech-to-text (STT) and text-to-speech (TTS) technologies to interact with users through voice commands.

## Features

- **Speech Recognition**: Uses Whisper and SpeechRecognition libraries to transcribe spoken words into text.
- **Text-to-Speech**: Utilizes Coqui TTS for converting text responses into speech.
- **Command Handling**: Supports a variety of voice commands to perform different actions.

## New Commands

### Good Morning Command

- **Keywords**: "good morning"
- **Description**: Responds with a friendly morning greeting.
- **Response**: "Good morning! How can I assist you today?"

### Good Night Command

- **Keywords**: "good night"
- **Description**: Responds with a friendly night farewell.
- **Response**: "Good night! Sleep well and sweet dreams!"

## Existing Commands

### Greet Command

- **Keywords**: "hello", "hi", "greet", "hey"
- **Description**: Greets the user.
- **Response**: "Hello! How can I assist you today?"

### Quit Command

- **Keywords**: "quit", "exit", "close", "goodbye"
- **Description**: Exits the application.
- **Response**: "Goodbye!"

### Time Command

- **Keywords**: "time", "current time", "what time is it"
- **Description**: Provides the current time.
- **Response**: "The current time is [time]."

### Reminder Command

- **Keywords**: "remind", "reminder", "set a reminder"
- **Description**: Sets a reminder for a specified time.
- **Response**: "Reminder set for [amount] [unit]."

## How It Works

1. **Initialization**: The application initializes the STT and TTS components and loads all available commands.
2. **Listening**: The application listens for a wake word ("aster") to start processing commands.
3. **Command Execution**: Once activated, the application processes the spoken command and executes the corresponding action.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/astr-voice-assistant.git
   cd astr-voice-assistant
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python main.py
   ```

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue.

## License

This project is licensed under the MIT License.
