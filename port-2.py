"""
Created on Sep, 2024

@author: Ayoub Wahmane/securityinshadows
"""

from datetime import datetime

# Get a valid date from the user, in the format YYYY-MM-DD
from datetime import datetime
def get_valid_date():
    while True:
        date_str = input("Input the date for the task (YYYY-MM-DD or YYYY/MM/DD): ")
        # Replace slashes with hyphens to normalize the input
        normalized_date_str = date_str.replace('/', '-')
        try:
            # Parse the normalized date string using hyphens
            task_date = datetime.strptime(normalized_date_str, "%Y-%m-%d")
            return task_date  # Return date object
        except ValueError:
            print("Invalid date format. Please enter the date in YYYY-MM-DD or YYYY/MM/DD format.")


# Welcome message
def welcome():
    print("Hello and welcome to our To-do List manager.\n")
    print("1 - Add New Task\n2 - Edit Tasks\n3 - Delete Tasks\n4 - View Task Details\n")
    print("Input 1, 2, 3 or 4 to continue.\n")

# Task storage
task_list = []  # Initialize the task list

# Function to add a new task
def new_task():
    task_name = input("Input a task name: ")
    task_date = get_valid_date()  # Get valid date
    task_content = input("Input a short description of " + task_name + ": ")
    task_place = input("Input the place for " + task_name + ": ")
    return {  # Return the task as a dictionary
        "Task name": task_name,
        "Task date": task_date.strftime("%Y-%m-%d"),  # Store the date as a string
        "Task description": task_content,
        "Task place": task_place
    }

# Add a task to the task list
def add_task():
    task = new_task()
    task_list.append(task)  # Append task to list
    print("Task added successfully.\n")

# Print all task details
def print_task_data():
    if not task_list:
        print("No tasks available.\n")
        return

    print("Here are the task details:\n")
    # To enumerate the tasks
    for index, task in enumerate(task_list, start=1):
        print(f"Task #{index}:")
        for key, value in task.items():
            print(f"  {key}: {value}")
        print("\n") 


# Edit an existing task
def edit_task():
    # In case there are no tasks
    if not task_list:
        print("No tasks to edit.\n")
        return

    print("Here are the tasks:")
    for index, task in enumerate(task_list, start=1):
        print(f"{index}. {task['Task name']}")

    task_number = int(input("Enter the number of the task you wish to edit: "))
    if 0 < task_number <= len(task_list):
        task_data = task_list[task_number - 1]  # Select the task to edit

        print("Which detail do you wish to edit?\n1- Task name\n2- Task date\n3- Task description\n4- Task place\n")
        edit_detail = input().strip()

        if edit_detail == "1":
            task_data["Task name"] = input("Input a new task name: ")
        elif edit_detail == "2":
            task_data["Task date"] = get_valid_date().strftime("%Y-%m-%d")
        elif edit_detail == "3":
            task_data["Task description"] = input("Input a new task description: ")
        elif edit_detail == "4":
            task_data["Task place"] = input("Input a new task place: ")
        else:
            print("Invalid input. No changes made.\n")
            return

        print("Edit saved successfully.\n")
    else:
        print("Invalid task number.\n")

# Remove a task from the list
def remove_task():
    if not task_list:
        print("No tasks to delete.\n")
        return

    print("Here are the tasks:")
    for index, task in enumerate(task_list, start=1):
        print(f"{index}. {task['Task name']}")

    task_number = int(input("Enter the number of the task you want to delete: ").strip())
    if 0 < task_number <= len(task_list):
        del task_list[task_number - 1]  # Delete the selected task
        print("Task deleted successfully.\n")
    else:
        print("Invalid task number.\n")

# Main program execution flow
def main():
    while True:
        welcome()  # Show the welcome message and options
        choice = input("Enter your choice (1, 2, 3, 4): ").strip()

        if choice == "1":
            add_task()
        elif choice == "2":
            edit_task()
        elif choice == "3":
            remove_task()
        elif choice == "4":
            print_task_data()
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.\n")

if __name__ == "__main__":
    main()



