# Task Manager

class Task:
    task_id = 0

    def __init__(self, description, priority, completed=False):
        Task.task_id += 1
        self.task_id = Task.task_id
        self.description = description
        self.priority = priority
        self.completed = completed

        



