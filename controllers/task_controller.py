from models.task import Task


class TaskController:
    """Contrôleur principal gérant les opérations sur les tâches."""

    def __init__(self):
        self.tasks = []

    def add_task(self, title: str, description: str = ""):
        task = Task(title, description)
        self.tasks.append(task)
        return task

    def list_tasks(self):
        return self.tasks

    def get_task_by_id(self, task_id: str):
        for task in self.tasks:
            if task.id.startswith(task_id):
                return task
        return None

    def complete_task(self, task_id: str):
        task = self.get_task_by_id(task_id)
        if task:
            task.mark_as_done()
            return task
        return None

    def delete_task(self, task_id: str):
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return task
        return None