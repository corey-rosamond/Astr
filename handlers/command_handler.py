import importlib
import os
from pathlib import Path
from handlers.command import Command


class CommandHandler:
    """Handles command execution."""

    def __init__(self, app):
        self.app = app
        self.commands = {}
        self.keywords_to_commands = {}  # Map keywords to command instances
        self.load_commands()

    def load_commands(self):
        """Dynamically load all commands from the commands directory."""
        commands_dir = Path("commands")
        for file in commands_dir.glob("*.py"):
            module_name = file.stem
            try:
                module = importlib.import_module(f"commands.{module_name}")
                for attr in dir(module):
                    cls = getattr(module, attr)
                    if isinstance(cls, type) and issubclass(cls, Command) and cls is not Command:
                        instance = cls()
                        self.commands[module_name] = instance
                        # Collect keywords
                        for keyword in instance.keywords:
                            self.keywords_to_commands[keyword.lower()] = instance
            except Exception as e:
                print(f"Error loading command {module_name}: {e}")

    def execute_command(self, text: str):
        """Execute the command corresponding to the text."""
        for keyword, command in self.keywords_to_commands.items():
            if keyword in text.lower():
                command.execute(self.app, text)
                return True

        # No matching command
        return False
