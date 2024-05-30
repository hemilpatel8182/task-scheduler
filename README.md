# Task Scheduler

This is a simple Python project for a Task Scheduler that allows users to schedule and manage tasks.

## Features

- Add tasks with names and due dates.
- Mark tasks as completed.
- View all tasks along with their status (pending/completed).

## Usage

1. Adding Tasks:
   - To add a new task, use the `add_task` method of the `TaskScheduler` class. Provide the task name and due date as parameters.

2. Marking Tasks as Completed:
   - To mark a task as completed, use the `mark_task_as_completed` method of the `TaskScheduler` class. Provide the task name as a parameter.

3. Viewing Tasks:
   - To view all tasks, use the `view_tasks` method of the `TaskScheduler` class. This will display a list of all tasks along with their due dates and statuses.

## Example

```python
from task_scheduler import TaskScheduler

scheduler = TaskScheduler()

# Adding tasks
scheduler.add_task("Finish report", "2024-06-05")
scheduler.add_task("Prepare presentation", "2024-06-10")
scheduler.add_task("Review documentation", "2024-06-08")

# Marking a task as completed
scheduler.mark_task_as_completed("Finish report")

# Viewing tasks
scheduler.view_tasks()
