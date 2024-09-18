"""
TO DO LIST PROGRAM

This program allows the user to manage tasks in a to-do list. The user can add new tasks to the 
pending list, mark tasks as finished (which moves them to the finished list), delete tasks, 
and view both pending and finished tasks. The program keeps running until the user chooses to exit.

Classes:
- Task: Represents a single task with a description.
- PendingTasks: Manages the list of pending tasks.
- FinishedTasks: Manages the list of finished tasks.
"""

# Class representing a task
class Task:
    def __init__(self, description):
        # Initialize the task with its description
        self.description = description

# Class representing the list of pending tasks
class PendingTasks:
    def __init__(self):
        # Initialize an empty list to store pending tasks
        self.pending_list = []

    # Method to add a new task to the pending tasks list
    def add_task(self, task):
        self.pending_list.append(task)  # Add the task to the list
        print(f'Task "{task.description}" added to pending tasks.')

    # Method to mark a task as finished and move it to the finished tasks list
    def mark_task(self, task_index, finished_tasks):
        # Check if the task index is valid
        if 0 <= task_index < len(self.pending_list):
            # Remove the task from pending tasks and add it to finished tasks
            finished_task = self.pending_list.pop(task_index)
            finished_tasks.add_finished_task(finished_task)
            print(f'Task "{finished_task.description}" marked as finished.')
        else:
            print("Invalid task index!")

    # Method to view all pending tasks
    def view_pending(self):
        if self.pending_list:
            print("Pending Tasks:")
            # Display each pending task with its index
            for i, task in enumerate(self.pending_list):
                print(f"{i + 1}. {task.description}")
        else:
            print("No pending tasks!")

    # Method to delete a task from the pending list
    def delete_task(self, task_index):
        # Check if the task index is valid
        if 0 <= task_index < len(self.pending_list):
            # Remove and display the deleted task
            deleted_task = self.pending_list.pop(task_index)
            print(f'Task "{deleted_task.description}" deleted from pending tasks.')
        else:
            print("Invalid task index!")

# Class representing the list of finished tasks
class FinishedTasks:
    def __init__(self):
        # Initialize an empty list to store finished tasks
        self.finished_list = []

    # Method to add a task to the finished tasks list
    def add_finished_task(self, task):
        self.finished_list.append(task)

    # Method to view all finished tasks
    def view_finished(self):
        if self.finished_list:
            print("Finished Tasks:")
            # Display each finished task with its index
            for i, task in enumerate(self.finished_list):
                print(f"{i + 1}. {task.description}")
        else:
            print("No finished tasks!")

# Create instances of PendingTasks and FinishedTasks to manage tasks
pending_tasks = PendingTasks()
finished_tasks = FinishedTasks()

# Main program loop
while True:
    # Display menu options to the user
    print("\nTO DO LIST PROGRAM")
    print('''1. Add a task
2. Mark a task as finished
3. Delete a task
4. View all pending tasks
5. View finished tasks
6. Exit''')

    # Get user input
    val = int(input("Your input: "))
    
    # Add a new task
    if val == 1:
        task_description = input("Enter task description: ")
        new_task = Task(task_description)  # Create a new task object
        pending_tasks.add_task(new_task)  # Add the new task to the pending list

    # Mark a task as finished
    elif val == 2:
        pending_tasks.view_pending()  # Display pending tasks to the user
        task_index = int(input("Enter the task number to mark as finished: ")) - 1
        pending_tasks.mark_task(task_index, finished_tasks)  # Mark the selected task as finished

    # Delete a task
    elif val == 3:
        pending_tasks.view_pending()  # Display pending tasks to the user
        task_index = int(input("Enter the task number to delete: ")) - 1
        pending_tasks.delete_task(task_index)  # Delete the selected task

    # View all pending tasks
    elif val == 4:
        pending_tasks.view_pending()

    # View finished tasks
    elif val == 5:
        finished_tasks.view_finished()

    # Exit the program
    elif val == 6:
        print("Exiting program...")
        break

    # Handle invalid input
    else:
        print("Invalid input, please try again.")
