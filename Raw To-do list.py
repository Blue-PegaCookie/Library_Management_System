# I'll be building a command-line to-do list application
# Users can add, view, and delete tasks

tasks = []

def menu():

    print("Select operation:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Delete a task")

    choice = input("Enter choice (1/2/3/4): ")

    if choice == '1':
        add_task()
    elif choice == '2':
        view_tasks()
    elif choice == '3':
        delete_task()
    else:
        print("Invalid input")
        menu()


def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")
    to_do_list_application()

def view_tasks():
    if len(tasks) == 0:
        print("No tasks available")
    else:
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
    to_do_list_application()

def delete_task():
    if len(tasks) == 0:
        print("No tasks available")
    else:
        view_tasks()
        task_number = int(input("Enter task number to delete: "))
        if task_number > len(tasks):
            print("Invalid task number")
        else:
            tasks.pop(task_number - 1)
            print("Task deleted successfully!")
    to_do_list_application()


def to_do_list_application():
    print("Welcome to the to-do list app!")

    option = input("Do you want to access the menu or exit the app?")

    if option.lower() == "menu":
        menu()
    elif option.lower() == "exit":
        print("Goodbye!")
        exit()
    else:
        print("Invalid input")
        to_do_list_application()

to_do_list_application()


# The above code is a simple to-do list application
# I'll be using a text file to store the tasks to make sure they exist even after the programme finishes running


