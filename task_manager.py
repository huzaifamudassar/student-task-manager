

import json
import os


class TaskManager:
    """Keeps a list of tasks. Each task is a dictionary.

    If data_file is given, tasks are saved to that JSON file so they are
    still there the next time the program runs.
    """

    def __init__(self, data_file=None):
        self.data_file = data_file
        self.tasks = []
        self.next_id = 1
        self.load()

    def add_task(self, title):
        title = (title or "").strip()
        if not title:
            raise ValueError("Task title cannot be empty.")
        task = {"id": self.next_id, "title": title, "completed": False}
        self.tasks.append(task)
        self.next_id += 1
        self.save()
        return task

    def list_tasks(self):
        return list(self.tasks)

    def complete_task(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    raise ValueError(f"Task {task_id} is already completed.")
                task["completed"] = True
                self.save()
                return task
        raise ValueError(f"No task found with ID {task_id}.")

    def delete_task(self, task_id):
        if not isinstance(task_id, int) or task_id < 1:
            raise ValueError("Task ID must be a positive whole number.")
        for task in self.tasks:
            if task["id"] == task_id:
                self.tasks.remove(task)
                self.save()
                return task
        raise ValueError(f"No task found with ID {task_id}.")

    def save(self):
        if self.data_file is None:
            return
        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump({"next_id": self.next_id, "tasks": self.tasks}, file, indent=2)

    def load(self):
        if self.data_file is None or not os.path.exists(self.data_file):
            return
        with open(self.data_file, encoding="utf-8") as file:
            data = json.load(file)
        self.tasks = data.get("tasks", [])
        self.next_id = data.get("next_id", len(self.tasks) + 1)
