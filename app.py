import json

TASKS_FILE = "tasks.json"


def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except:
        return []


def save_tasks(tasks):
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)


def show_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    for index, task in enumerate(tasks, start=1):
        status = "✅" if task["done"] else "❌"
        print(f"{index}. {task['title']} {status}")


def add_task(tasks):
    title = input("Enter task title: ")

    task = {
        "title": title,
        "done": False
    }

    tasks.append(task)
    save_tasks(tasks)

    print("Task added successfully!")


def complete_task(tasks):
    show_tasks(tasks)

    number = int(input("Task number to complete: "))

    tasks[number - 1]["done"] = True

    save_tasks(tasks)

    print("Task completed!")


def main():
    tasks = load_tasks()

    while True:
        print("\n--- TASK MANAGER ---")
        print("1. Show Tasks")
        print("2. Add Task")
        print("3. Complete Task")
        print("4. Exit")

        choice = input("Choose: ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            add_task(tasks)

        elif choice == "3":
            complete_task(tasks)

        elif choice == "4":
            break

        else:
            print("Invalid choice")


main()
