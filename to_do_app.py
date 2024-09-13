tasks =[]
def add_task(task):
    tasks.append(task)
    print(f"Task '{task}' added successfully.")

def remove_task(task):
    if task in tasks:
        tasks.remove(task)
        print(f"Task '{task}' removed successfully.")
    else:
        print(f"Task '{task}' not found.")

def update_task(task,new_task):
    if task in tasks:
        tasks[tasks.index(task)] = new_task
        print(f"Task '{task}' updated to '{new_task}' successfully.")
    else:
        print(f"Task '{task}' not found.")

def display_tasks():
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

def main_menu():
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. Display Tasks")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == "1":
            task = input("Enter the task: ")
            add_task(task)
        elif choice == "2":
            task = input("Enter the task to remove: ")
            remove_task(task)
        elif choice == "3":
            task = input("Enter the task to update: ")
            new_task = input("Enter the new task: ")
            update_task(task, new_task)
        elif choice == "4":
            display_tasks()
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

main_menu()