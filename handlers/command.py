class Command:
    """Base class for all commands."""
    keywords = []

    def execute(self, app, text: str):
        raise NotImplementedError("Each command must implement the execute method.")