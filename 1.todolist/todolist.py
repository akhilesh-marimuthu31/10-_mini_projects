class Task:
    def __init__(self, description):
        self.description = description

class PendingTasks:
    def __init__(self):
        self.pending_list = []

    def add_task(self, task):
        self.pending_list.append(task)
        print(f'Task "{task.description}" added to pending tasks.')

    def mark_task(self, task_index, finished_tasks):
        if 0 <= task_index < len(self.pending_list):
            finished_task = self.pending_list.pop(task_index)
            finished_tasks.add_finished_task(finished_task)
            print(f'Task "{finished_task.description}" marked as finished.')
        else:
            print("Invalid task index!")

    def view_pending(self):
        if self.pending_list:
            print("Pending Tasks:")
            for i, task in enumerate(self.pending_list):
                print(f"{i + 1}. {task.description}")
        else:
            print("No pending tasks!")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.pending_list):
            deleted_task = self.pending_list.pop(task_index)
            print(f'Task "{deleted_task.description}" deleted from pending tasks.')
        else:
            print("Invalid task index!")

class FinishedTasks:
    def __init__(self):
        self.finished_list = []

    def add_finished_task(self, task):
        self.finished_list.append(task)

    def view_finished(self):
        if self.finished_list:
            print("Finished Tasks:")
            for i, task in enumerate(self.finished_list):
                print(f"{i + 1}. {task.description}")
        else:
            print("No finished tasks!")

# Create instances of PendingTasks and FinishedTasks
pending_tasks = PendingTasks()
finished_tasks = FinishedTasks()

# Main program loop
while True:
    print("\nTO DO LIST PROGRAM")
    print('''1. Add a task
2. Mark a task as finished
3. Delete a task
4. View all pending tasks
5. View finished tasks
6. Exit''')

    val = int(input("Your input: "))
    
    if val == 1:
        task_description = input("Enter task description: ")
        new_task = Task(task_description)
        pending_tasks.add_task(new_task)

    elif val == 2:
        pending_tasks.view_pending()
        task_index = int(input("Enter the task number to mark as finished: ")) - 1
        pending_tasks.mark_task(task_index, finished_tasks)

    elif val == 3:
        pending_tasks.view_pending()
        task_index = int(input("Enter the task number to delete: ")) - 1
        pending_tasks.delete_task(task_index)

    elif val == 4:
        pending_tasks.view_pending()

    elif val == 5:
        finished_tasks.view_finished()

    elif val == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid input, please try again.")
