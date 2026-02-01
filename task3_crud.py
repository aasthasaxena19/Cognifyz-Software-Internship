tasks = []

def show_menu():
    print("\n--- TASK MANAGER ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Exit")

def add_task():
    task = input("Enter new task: ")
    tasks.append(task)
    print("✅ Task added successfully")

def view_tasks():
    if not tasks:
        print("No tasks available")
    else:
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def update_task():
    view_tasks()
    try:
        index = int(input("Enter task number to update: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index] = input("Enter new task: ")
            print("✏️ Task updated")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")

def delete_task():
    view_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("🗑️ Task deleted")
        else:
            print("Invalid task number")
    except ValueError:
        print("Please enter a valid number")

while True:
    show_menu()
    choice = input("Choose option: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        update_task()
    elif choice == "4":
        delete_task()
    elif choice == "5":
        break
    else:
        print("Invalid choice")
