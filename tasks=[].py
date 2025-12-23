# QuickTask Manager: A simple CRUD (Create, Read, Update, Delete) application
import os

def main():
    tasks = []
    
    # Check if a saved file exists and load tasks
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as f:
            tasks = [line.strip() for line in f.readlines()]

    while True:
        print("\n--- QUICKTASK MANAGER ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Save & Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            print("\nYOUR TASKS:")
            if not tasks:
                print("No tasks found!")
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")

        elif choice == '2':
            new_task = input("Enter the task: ")
            tasks.append(new_task)
            print("Task added successfully!")

        elif choice == '3':
            # Show tasks first so user knows what to delete
            for index, task in enumerate(tasks, start=1):
                print(f"{index}. {task}")
            task_num = int(input("Enter the number to delete: "))
            if 0 < task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Removed: {removed}")
            else:
                print("Invalid number.")

        elif choice == '4':
            # Save tasks to a file so they aren't lost when the program closes
            with open("tasks.txt", "w") as f:
                for task in tasks:
                    f.write(task + "\n")
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()