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
    task_id = int(input("Task ID to complete: "))
    task = manager.complete_task(task_id)
    if task:
        print(f"Task {task_id} marked as completed.")
    else:
        print("Task not found.")


def delete_task_ui(manager):
    raw = input("Task ID to delete: ").strip()
    if not raw.isdigit():
        print("Error: please enter a task ID number, e.g. 2.")
        return
    try:
        task = manager.delete_task(int(raw))
    except ValueError as error:
        print(f"Error: {error}")
        return
    print(f"Deleted task {task['id']}: {task['title']}")

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
