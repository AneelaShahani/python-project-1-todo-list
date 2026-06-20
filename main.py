# TO-DO LIST FULL VERSION

tasks = []

while True:
    print("\n===== TO-DO LIST MENU =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Done")
    print("5. Exit")

    choice = input("Enter your choice: ")

    # ADD TASK
    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"task": task, "done": False})
        print("Task added successfully!")

    # VIEW TASKS
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks available.")
        else:
            print("\n--- Your Tasks ---")
            for i, t in enumerate(tasks, start=1):
                status = "Done" if t["done"] else "Not Done"
                print(f"{i}. {t['task']} [{status}]")

    # DELETE TASK
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t['task']}")

            try:
                num = int(input("Enter task number to delete: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"Deleted: {removed['task']}")
                else:
                    print("Invalid number!")
            except ValueError:
                print("Please enter a valid number!")

    # MARK AS DONE
    elif choice == "4":
        if len(tasks) == 0:
            print("No tasks to mark.")
        else:
            for i, t in enumerate(tasks, start=1):
                print(f"{i}. {t['task']}")

            try:
                num = int(input("Enter task number to mark as done: "))
                if 1 <= num <= len(tasks):
                    tasks[num - 1]["done"] = True
                    print("Task marked as DONE!")
                else:
                    print("Invalid number!")
            except ValueError:
                print("Please enter a valid number!")

    # EXIT
