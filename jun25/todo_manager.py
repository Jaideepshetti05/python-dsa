tasks = []

while True:
    print("\n===== TO DO MANAGER =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nTasks:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        if tasks:
            index = int(input("Enter task number: ")) - 1
            if 0 <= index < len(tasks):
                removed = tasks.pop(index)
                print(f"Removed: {removed}")
            else:
                print("Invalid task number.")
        else:
            print("No tasks to delete.")

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid choice.")