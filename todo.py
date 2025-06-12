t0_do_tasks = []
def options():
    print("\n<<<<<To-Do List>>>>>")
    print("1. Add new Task")
    print("2. View Tasks")
    print("3. Mark as Complete")
    print("4. Delete a Task")
    print("5. Exit the application")

while True:
    options()
    choice = input("Choose an option (1-5): ")

    if choice == '1':
        task = input("Enter a new task: ")
        t0_do_tasks.append({'task': task, 'completed': False})
        print("Task has been added.")
    elif choice == '2':
        if not t0_do_tasks:
            print("No tasks are found.")
        for i, t in enumerate(t0_do_tasks):
            status = "✓" if t['completed'] else "✗"
            print(f"{i + 1}. [{status}] {t['task']}")
    elif choice == '3':
        index = int(input("Enter task number to mark as complete: ")) - 1
        if 0 <= index < len(t0_do_tasks):
            t0_do_tasks[index]['completed'] = True
            print("Task is marked as complete.")
    elif choice == '4':
        index = int(input("Enter task number to be deleted: ")) - 1
        if 0 <= index < len(t0_do_tasks):
            t0_do_tasks.pop(index)
            print("Task is succesfully deleted.")
    elif choice == '5':
        print("You exited the program, Thankyou!")
        break
    else:
        print("Enter a valid number.")
