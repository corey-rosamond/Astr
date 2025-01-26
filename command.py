class Command:
    """Base class for commands."""

    def execute(self, app, text):
        raise NotImplementedError("Execute method must be implemented in subclasses.")

