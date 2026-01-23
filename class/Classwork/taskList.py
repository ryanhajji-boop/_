from datetime import datetime

task_list = []  # define a task list


def addTask():
    task = input("Enter a task that you would like to do: ")
    priority = input("Enter priority (High/Medium/Low): ").capitalize()
    deadline = input("Enter deadline (YYYY-MM-DD) or leave blank: ")

    # Validate deadline
    if deadline:
        try:
            deadline = datetime.strptime(deadline, "%Y-%m-%d").date()
        except ValueError:
            print("Invalid date format. Saving without deadline.")
            deadline = None
    else:
        deadline = None

    task_list.append({
        "task": task,
        "priority": priority,
        "deadline": deadline
    })
    print("Task added successfully!\n")


def displayAllTasks(task_list):
    while True:
        response = input("Would you like to display all the tasks? (Y/N): ").strip().upper()
        if response == "Y":
            if not task_list:
                print("No tasks yet!")
                break

            # Sort by priority (High → Medium → Low)
            priority_order = {"High": 1, "Medium": 2, "Low": 3}
            sorted_tasks = sorted(task_list, key=lambda t: priority_order.get(t["priority"], 4))

            print("\nYour Tasks:")
            for i, task in enumerate(sorted_tasks, 1):
                deadline_str = task["deadline"].strftime("%Y-%m-%d") if task["deadline"] else "No deadline"
                print(f"{i}. {task['task']} | Priority: {task['priority']} | Deadline: {deadline_str}")
            print()
            break
        elif response == "N":
            print("Okay, not displaying tasks.")
            break
        else:
            print("Please try again. Answer with 'Y' or 'N'.")


def checkTask():
    while True:
        try:
            pos = int(input("What task would you like to check? (Type its position i.e. A number) "))
            if 1 <= pos <= len(task_list):
                task = task_list[pos - 1]
                deadline_str = task["deadline"].strftime("%Y-%m-%d") if task["deadline"] else "No deadline"
                print(f"Task: {task['task']} | Priority: {task['priority']} | Deadline: {deadline_str}")
                break
            else:
                print("This task's position does not exist!")
        except ValueError:
            print("Please enter a valid number.")


def completeNextTask():
    while True:
        try:
            for i, task in enumerate(task_list):
                deadline_str = task["deadline"].strftime("%Y-%m-%d") if task["deadline"] else "No deadline"
                print(f"{i}: {task['task']} | Priority: {task['priority']} | Deadline: {deadline_str}")

            completedIndex = int(input("\nWhich task have you completed? Enter the index: "))

            if 0 <= completedIndex < len(task_list):
                removed_task = task_list.pop(completedIndex)
                print(f"Removed: {removed_task['task']}")
                print("Remaining tasks:", len(task_list))
                break
            else:
                print("Invalid index. Try again.")
        except ValueError:
            print('Please enter a valid number.')


def menu():
    while True:
        choice = input(
            "What would you like to do? \n 1. Create a task \n 2. Display all tasks "
            "\n 3. Check task \n 4. Complete a task \n 5. Exit \n"
        )
        if choice == "1":
            addTask()
        elif choice == "2":
            displayAllTasks(task_list)
        elif choice == "3":
            checkTask()
        elif choice == "4":
            completeNextTask()
        elif choice == "5":
            break
        else:
            print("Enter a valid numbered choice")


menu()
