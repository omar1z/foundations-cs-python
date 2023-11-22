# Task Manager

class Task:
    task_id = 0

    def __init__(self, description, priority: int, completed=False):
        Task.task_id += 1
        self.task_id = Task.task_id
        self.description = description
        self.priority = priority
        self.completed = completed

    def getId(self):
        return self.task_id

    def getDescription(self):
        return self.description

    def getPriority(self):
        return self.priority

    def getStatus(self):
        return self.completed

    # I won't define a method setter for task_id because id is stable & incremented

    def setDescription(self, description):
        self.description = description

    def setPriority(self, priority):
        self.priority = priority

    def setStatus(self, completed):
        self.completed = completed



