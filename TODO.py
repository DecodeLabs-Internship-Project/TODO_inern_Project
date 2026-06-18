tasks = []


def add_task():
    task = input("Enter the task: ")
    tasks.append(task)
    print("Task added:\n", task)


def view_tasks():
    if not tasks:
        print("No tasks in the list.")
        return
    print("Your tasks:")
    for task in tasks:
        print("1.", task)
def delete_task():
    task = input("Enter the task to delete: ")
    if task in tasks:
        tasks.remove(task)
        print("Task deleted:\n", task)
    else:
        print("Task not found in the list.")
def edit_task():
    old_task=input("enter which task you want to edit")
    if old_task in  tasks:
        new_task=input("enter a new task")
        index=tasks.index(old_task)
        tasks[index]=new_task
        print("Task edited:\n", new_task)
    else:
            print("Task not found in the list.")

while True:
    print("Welcome to the To-Do List App!")
    print("1. - Add a task")
    print("2. - View all tasks")
    print("3. - Delete a task")
    print("4. - Edit a task")
    print("5. - Exit the app")

    command = input("Enter a command (1, 2, 3, 4, 5): ")

    if command == "1":
     add_task()
    elif command == "2":
        view_tasks()
    elif command == "3":
        delete_task()
    elif command == "4":
        edit_task()
    elif command == "5":
        print("Exiting the app...")
        break
    else:
        print("Invalid command. Please try again.")

