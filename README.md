# Task Scheduler

This is a simple Python project for a Task Scheduler that allows users to schedule and manage tasks.

## Features
   - Add tasks with names and due dates.
   - Mark tasks as completed.
   - View all tasks along with their status (pending/completed).
   - View past tasks that are overdue.
   - Get reminders for upcoming tasks.
   - Interactive menu for managing tasks.

## Usage

1. Adding Tasks:
   To add a new task, select the option to add a task from the interactive menu. Provide the task name and due date (in YYYY-MM-DD format) as prompted.
   
2. Marking Tasks as Completed:
   To mark a task as completed, select the option to mark a task as completed from the interactive menu. Provide the task name as prompted.
      
3. Viewing Tasks:
   To view all tasks, select the option to view tasks from the interactive menu. This will display a list of all tasks along with their due dates and statuses.
   
4. Viewing Past Tasks:
   To view tasks that are overdue, select the option to view past tasks from the interactive menu.
   
5. Getting Reminders:
   To get reminders for upcoming tasks, select the option to show task reminders from the interactive menu.
   
## Example

from task_scheduler import TaskScheduler

scheduler = TaskScheduler()

# Interactive menu for managing tasks
scheduler.interactive_menu()

# Interactive Menu Options
Add a Task: Allows you to add a new task by providing the task name and due date.
View Tasks: Displays all tasks with their due dates and statuses.
View Past Tasks: Displays tasks that are overdue.
Mark Task as Completed: Marks a specified task as completed by providing the task name.
Show Task Reminders: Provides reminders for upcoming tasks.
Exit: Exits the task scheduler.
