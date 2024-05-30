class Task:
    def __init__(self, name, due_date):
        self.name = name
        self.due_date = due_date
        self.completed = False

class TaskScheduler:
    def __init__(self):
        self.tasks = []

    def add_task(self, name, due_date):
        task = Task(name, due_date)
        self.tasks.append(task)

    def mark_task_as_completed(self, task_name):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True
                break

    def view_tasks(self):
        for task in self.tasks:
            status = "Completed" if task.completed else "Pending"
            print(f"{task.name} (Due: {task.due_date}) - {status}")

scheduler = TaskScheduler()

# Example usage:
scheduler.add_task("Finish report", "2024-06-05")
scheduler.add_task("Prepare presentation", "2024-06-10")
scheduler.add_task("Review documentation", "2024-06-08")

scheduler.mark_task_as_completed("Finish report")

scheduler.view_tasks()
