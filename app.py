
import json
from pathlib import Path

TASKS_FILE = Path(__file__).parent / "tasks.json"


def load_tasks():
    """Load tasks from the JSON file."""
    if not TASKS_FILE.exists():
        return []

    try:
        with TASKS_FILE.open("r", encoding="utf-8") as file:
            tasks = json.load(file)

        if not isinstance(tasks, list):
            print("Error: tasks.json must contain a list.")
            return []

        for task in tasks:
            if (
                not isinstance(task, dict)
                or not isinstance(task.get("title"), str)
                or not isinstance(task.get("done"), bool)
            ):
                print("Error: tasks.json contains invalid task data.")
                return []

        return tasks

    except json.JSONDecodeError:
        print("Error: tasks.json contains invalid JSON.")
        return []

    except OSError as error:
        print(f"Error reading tasks: {error}")
        return []


def save_tasks(tasks):
    """Save tasks to the JSON file."""
    try:
        with TASKS_FILE.open("w", encoding="utf-8") as file:
            json.dump(tasks, file, indent=4, ensure_ascii=False)
        return True

    except (OSError, TypeError) as error:
        print(f"Error saving tasks: {error}")
        return False


def show_tasks(tasks):
    """Display all tasks."""
    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "Done" if task["done"] else "Pending"
        print(f"{index}. {task['title']} [{status}]")


def add_task(tasks):
    """Add a new task."""
    title = input("Enter task title: ").strip()

    if not title:
        print("Task title cannot be empty.")
        return

    task = {"title": title, "done": False}
    tasks.append(task)

    if save_tasks(tasks):
        print("Task added successfully!")
    else:
        tasks.pop()
        print("Task was not added because saving failed.")


def complete_task(tasks):
    """Mark a task as completed."""
    if not tasks:
        print("No tasks available to complete.")
        return

    show_tasks(tasks)
    choice = input("Task number to complete: ").strip()

    try:
        number = int(choice)
    except ValueError:
        print("Please enter a valid number.")
        return

    if number < 1 or number > len(tasks):
        print("Invalid task number.")
        return

    task = tasks[number - 1]

    if task["done"]:
        print("This task is already completed.")
        return

    task["done"] = True

    if save_tasks(tasks):
        print("Task completed successfully!")
    else:
        task["done"] = False
        print("Could not save the task status.")


def main():
    """Run the task manager menu."""
    tasks = load_tasks()

    while True:
        print("\n--- TASK MANAGER ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            show_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please choose 1-4.")


if __name__ == "__main__":
    main()
