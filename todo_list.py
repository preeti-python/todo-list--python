
# todo_list.py

tasks = []

def show_menu():
    print("\n=== TO-DO LIST MENU ===")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Remove Task")
    print("4. Exit")

def show_tasks():
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Your Tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")

def remove_task():
    show_tasks()
    try:
        task_num = int(input("Enter task number to remove: "))
        if 0 < task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == '1':
        show_tasks()
    elif choice == '2':
        add_task()
    elif choice == '3':
        remove_task()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
