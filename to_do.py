# List to store tasks, each task is a dictionary with a name and priority
tasks = []

def show_tasks():
    if not tasks:
        print("Your task list is empty.")
    else:
        print("Your tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['name']} - Priority: {task['priority']}")

def add_task(task_name, priority="Medium"):
    task = {"name": task_name, "priority": priority}
    tasks.append(task)
    print(f"Added task: '{task_name}' with priority '{priority}'")

def remove_task(task_number):
    if 0 < task_number <= len(tasks):
        removed_task = tasks.pop(task_number - 1)
        print(f"Removed task: '{removed_task['name']}'")
    else:
        print("Invalid task number.")

def change_priority(task_number, new_priority):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["priority"] = new_priority
        print(f"Priority of task '{tasks[task_number - 1]['name']}' changed to '{new_priority}'")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nOptions:")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Change task priority")
        print("5. Exit")

        choice = input("Choose an option: ")
        
        if choice == "1":
            show_tasks()
        elif choice == "2":
            task_name = input("Enter task name: ")
            priority = input("Enter priority (Low, Medium, High): ")
            add_task(task_name, priority)
        elif choice == "3":
            show_tasks()
            task_number = int(input("Enter task number to remove: "))
            remove_task(task_number)
        elif choice == "4":
            show_tasks()
            task_number = int(input("Enter task number to change priority: "))
            new_priority = input("Enter new priority (Low, Medium, High): ")
            change_priority(task_number, new_priority)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

