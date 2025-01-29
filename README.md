# Astr Voice Assistant

Astr is a voice assistant application that uses speech-to-text (STT) and text-to-speech (TTS) technologies to interact with users through voice commands.

## Project Structure

- **`commands/`**: Contains command modules that define specific actions the assistant can perform.
- **`handlers/`**: Contains the command handler logic for loading and executing commands.
- **`assets/`**: Contains audio files for start and stop listening sounds.
- **`stt.py`**: Handles speech-to-text functionality.
- **`tts.py`**: Handles text-to-speech functionality.
- **`main.py`**: The main application file that initializes and runs the assistant.
- **`requirements.txt`**: Lists the Python dependencies required for the project.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/astr-voice-assistant.git
   cd astr-voice-assistant
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   ```bash
   python main.py
   ```

## Command Instructions

The assistant can respond to the following commands:

- **Greet Command**: Responds to greetings like "hello", "hi", "greet", "hey".
- **Good Morning Command**: Responds to "good morning".
- **Good Night Command**: Responds to "good night".
- **Quit Command**: Responds to "quit", "exit", "close", "goodbye" and closes the application.
- **Reminder Command**: Sets a reminder. Example: "Remind me in 10 minutes to check the oven."
- **Time Command**: Tells the current time. Example: "What time is it?"

## Additional Information

- **Wake Word**: The assistant listens for the wake word "aster" to start processing commands.
- **Audio Feedback**: The assistant plays a sound when it starts and stops listening for commands.
- **Logging**: The TTS module logs its activity to a file for debugging purposes.

- **`commands/`**: Contains command modules that define specific actions the assistant can perform.
- **`handlers/`**: Contains the command handler logic for loading and executing commands.
- **`assets/`**: Contains audio files for start and stop listening sounds.
- **`stt.py`**: Handles speech-to-text functionality.
- **`tts.py`**: Handles text-to-speech functionality.
- **`main.py`**: The main application file that initializes and runs the assistant.
- **`requirements.txt`**: Lists the Python dependencies required for the project.

## Setup Instructions

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/astr-voice-assistant.git
   cd astr-voice-assistant
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Application**

   ```bash
   python main.py
   ```

## Command Instructions

The assistant can respond to the following commands:

- **Greet Command**: Responds to greetings like "hello", "hi", "greet", "hey".
- **Good Morning Command**: Responds to "good morning".
- **Good Night Command**: Responds to "good night".
- **Quit Command**: Responds to "quit", "exit", "close", "goodbye" and closes the application.
- **Reminder Command**: Sets a reminder. Example: "Remind me in 10 minutes to check the oven."
- **Time Command**: Tells the current time. Example: "What time is it?"

## Additional Information

- **Wake Word**: The assistant listens for the wake word "aster" to start processing commands.
- **Audio Feedback**: The assistant plays a sound when it starts and stops listening for commands.
- **Logging**: The TTS module logs its activity to a file for debugging purposes.

## Contributing

We welcome contributions to the Astr Assistant project! If you're interested in contributing, please follow these guidelines:

### Getting Started

1. **Fork the Repository**: Click the "Fork" button at the top right of this page to create a copy of the repository under your GitHub account.

2. **Clone the Repository**: Clone the forked repository to your local machine using the following command:
   ```bash
   git clone https://github.com/your-username/astr-assistant.git
   ```

3. **Create a Branch**: Create a new branch for your feature or bug fix:
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. **Install Dependencies**: Install the required dependencies using `pip`:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Application**: Ensure everything is working by running the application:
   ```bash
   python main.py
   ```

### Making Changes

- Follow the existing code style and conventions.
- Write clear, concise commit messages.
- Test your changes thoroughly.

### Submitting Changes

1. **Commit Your Changes**: Commit your changes to your branch:
   ```bash
   git commit -m "Add feature: description of your feature"
   ```

2. **Push to GitHub**: Push your changes to your forked repository:
   ```bash
   git push origin feature/your-feature-name
   ```

3. **Create a Pull Request**: Go to the original repository and click the "New Pull Request" button. Select your branch and submit your pull request for review.

### Code of Conduct

Please note that this project is released with a [Contributor Code of Conduct](CODE_OF_CONDUCT.md). By participating in this project, you agree to abide by its terms.

Thank you for your interest in contributing to the Astr Assistant project!
