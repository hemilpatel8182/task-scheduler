import datetime

class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = datetime.datetime.strptime(due_date, "%Y-%m-%d")
        self.completed = False

    def __str__(self):
        status = "Completed" if self.completed else "Pending"
        return f"{self.name} (Due: {self.due_date.strftime('%Y-%m-%d')}) - {status}"

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, due_date):
        task = Task(name, due_date)
        self.tasks.append(task)
        print(f"Task '{name}' added with due date {due_date}.")

    def mark_task_as_completed(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                print(f"Task '{task_name}' marked as completed.")
                return
        print(f"Task '{task_name}' not found.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)

    def view_past_tasks(self):
        past_tasks = [task for task in self.tasks if task.due_date < datetime.datetime.now()]
        if not past_tasks:
            print("No past tasks.")
        else:
            for task in past_tasks:
                print(task)

    def remind_tasks(self):
        for task in self.tasks:
            if not task.completed and task.due_date > datetime.datetime.now():
                print(f"Reminder: Task '{task.name}' is due on {task.due_date.strftime('%Y-%m-%d')}.")

    def interactive_menu(self):
        while True:
            print("\nMenu:")
            print("1. Add a task")
            print("2. View tasks")
            print("3. View past tasks")
            print("4. Mark task as completed")
            print("5. Show task reminders")
            print("6. Exit")
            choice = input("Choose an option: ")

            if choice == '1':
                name = input("Enter the task name: ")
                due_date = input("Enter the due date (YYYY-MM-DD): ")
                self.add_task(name, due_date)
            elif choice == '2':
                self.view_tasks()
            elif choice == '3':
                self.view_past_tasks()
            elif choice == '4':
                task_name = input("Enter the name of the task to mark as completed: ")
                self.mark_task_as_completed(task_name)
            elif choice == '5':
                self.remind_tasks()
            elif choice == '6':
                print("Exiting the task scheduler.")
                break
            else:
                print("Invalid option. Please try again.")

scheduler = TaskScheduler()
scheduler.interactive_menu()
