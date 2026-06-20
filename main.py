tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)

        with open("tasks.txt", "a") as file:
            file.write(task + "\n")

        print("Task added successfully!")

    elif choice == "2":
        print("\nYour Tasks:")

        if len(tasks) == 0:
            print("No tasks available.")

        else:
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif choice == "3":
        print("Program terminated.")
        break

    else:
        print("Invalid choice!")
