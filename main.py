"""Console interface for the Student Task Manager."""

from task_manager import TaskManager

MENU = """
===== Student Task Manager =====
1. Add task
2. View tasks
3. Complete task
4. Delete task
5. Exit
"""


def add_task_ui(manager):
    title = input("Task title: ")
    task = manager.add_task(title)
    print(f"Added task {task['id']}: {task['title']}")


def view_tasks_ui(manager):
    tasks = manager.list_tasks()
    if not tasks:
        print("No tasks yet.")
        return
    for task in tasks:
        status = "Done" if task["completed"] else "Pending"
        print(f"[{task['id']}] {task['title']} - {status}")


def complete_task_ui(manager):
    view_tasks_ui(manager)
    raw = input("Task ID(s) to complete, e.g. 2 or 1,3: ")
    for part in raw.split(","):
        part = part.strip()
        if not part.isdigit():
            print(f"Error: '{part}' is not a valid task ID.")
            continue
        try:
            task = manager.complete_task(int(part))
            print(f"Task {task['id']} marked as completed.")
        except ValueError as error:
            print(f"Error: {error}")


def delete_task_ui(manager):
    task_id = int(input("Task ID to delete: "))
    task = manager.delete_task(task_id)
    if task:
        print(f"Deleted task {task_id}.")
    else:
        print("Task not found.")


def main():
    manager = TaskManager("tasks.json")
    while True:
        print(MENU)
        choice = input("Choose an option: ").strip()
        if choice == "1":
            add_task_ui(manager)
        elif choice == "2":
            view_tasks_ui(manager)
        elif choice == "3":
            complete_task_ui(manager)
        elif choice == "4":
            delete_task_ui(manager)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")


if __name__ == "__main__":
    main()
