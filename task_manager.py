class TaskManager:
    """Keeps a list of tasks. Each task is a dictionary."""

    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title):
        task = {"id": self.next_id, "title": title, "completed": False}
        self.tasks.append(task)
        self.next_id += 1
        return task

    def list_tasks(self):
        return list(self.tasks)

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                task["completed"] = True
                return task
        return None

    def delete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                return task
        return None