todo_list = []

def add_task(task):
    todo_list.append(task)
    print("Task added successfully")

def remove_tak(task):
    if task in todo_list:
        todo_list.remove(task)
        print("Task removed successfully")
    else:
        print("Task not found in the list")

def view_task():
    if todo_list:
        print("Task:")
        for task in todo_list:
            print(task)
        else:
            print("No task in the To Do List.")
while True:
    print("\n--- To-Do List App")
    print("1. Add task")
    print("2. Remove task ")
    print("3. View task")
    print("4. Exit")

    choice = input("Enter your choice from 1-4: ")

    if choice == "1":
        task = input()
        add_task(task)
    elif choice == "2":
        remove_tak(task)
    elif choice == "3":
        view_task()
    elif choice == "4":
        print("Exit the program!")
        break
    else:
        print("Invalid choice please try again")

