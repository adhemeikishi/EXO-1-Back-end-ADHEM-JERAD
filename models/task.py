from datetime import datetime
import uuid


class Task:
    """Représente une tâche dans la ToDoList."""

    def __init__(self, title: str, description: str = ""):
        self.id = str(uuid.uuid4())
        self.title = title
        self.description = description
        self.created_at = datetime.now()
        self.completed = False

    def mark_as_done(self):
        """Marque la tâche comme terminée."""
        self.completed = True

    def mark_as_undone(self):
        """Marque la tâche comme non terminée."""
        self.completed = False

    def __str__(self):
        status = "✅" if self.completed else "❌"
        return f"[{status}] {self.title} (id: {self.id[:8]})"
