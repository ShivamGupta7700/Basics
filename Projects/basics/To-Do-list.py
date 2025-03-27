def add_task(newTask, taskList):
    taskList.append({"task": newTask, "completed": False})


def remove_task(task, taskList):
    for t in taskList:
        if t["task"] == task:
            taskList.remove(t)
            break


def mark_complete(task, taskList):
    for t in taskList:
        if t["task"] == task:
            t["completed"] = True
            break


def mark_incomplete(task, taskList):
    for t in taskList:
        if t["task"] == task:
            t["completed"] = False
            break


def show_tasks(taskList):
    print("\n--- Your To-Do List ---")
    if not taskList:
        print("Nothing to do, you are free")
    else:
        for idx, task in enumerate(taskList, 1):
            status = "✅" if task["completed"] else "❌"
            print(f"{idx}. {task['task']} [{status}]")
    print("-----------------------\n")


todoList = []

while True:
    print('''
    1 --> Add task
    2 --> Remove task
    3 --> Mark as Complete
    4 --> Mark as Incomplete
    5 --> Show tasks
    6 --> Exit (Data will be cleared)
    ''')

    user_input = int(input("Enter the operation: "))

    if user_input == 1:
        task = input("Enter your task > ")
        add_task(task, todoList)

    elif user_input == 2:
        task = input("Enter the task to remove > ")
        remove_task(task, todoList)

    elif user_input == 3:
        task = input("Enter the task to mark complete > ")
        mark_complete(task, todoList)

    elif user_input == 4:
        task = input("Enter the task to mark incomplete > ")
        mark_incomplete(task, todoList)

    elif user_input == 5:
        show_tasks(todoList)

    elif user_input == 6:
        print("Exiting... All tasks will be cleared.")
        break

    else:
        print("Invalid input. Please enter a number between 1-6.")

    show_tasks(todoList)
    print(todoList) #If you want how its working