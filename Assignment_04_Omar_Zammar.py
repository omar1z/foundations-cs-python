# Task Manager

class Task:
    task_id = 0

    def __init__(self, description, priority: int, completed=False):
        Task.task_id += 1
        self.task_id = Task.task_id
        self.description = description
        self.priority = priority
        self.completed = completed
        self.next = None

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


class PriorityQueue:

    def __init__(self):
        self.header = None
        self.size = 0

    def displayQueue(self):
        current = self.header
        while current.next is not None:
            print(current.description, end="--")
            current = current.next

        print(current.description)

    def enqueue(self, description, priority):

        node = Task(description, priority)

        if self.size == 0:
            self.header = node
            self.size += 1
        else:
            if node.priority > self.header.priority:
                node.next = self.header
                self.header = node
                self.size += 1

            else:
                current = self.header
                previous = current

                while current != None and current.priority >= node.priority:
                    previous = current
                    current = current.next

                previous.next = node
                node.next = current
                self.size += 1

    def dequeue(self):
        if self.size == 0:
            print("Your Queue is Empty! Enqueue first.")
        elif self.size == 1:
            print("We are removing:", self.header.description)
            self.header = None
            self.size -= 1
        else:
            print("We are removing:", self.header.description)
            current = self.header
            self.header = self.header.next
            current.next = None
            self.size -= 1


class Stack:

    def __init__(self):
        self.header = None
        self.size = 0

    def isEmpty(self):
        return self.header is None

    def displayStack(self):

        current = self.header

        while current is not None:
            print("|" + str(current.description) + "|")
            current = current.next

        print("---")

    def push(self, description, priority):
        node_to_add = Task(description, priority)

        node_to_add.next = self.header
        self.header = node_to_add
        self.size += 1

    def pop(self):

        if self.isEmpty():
            print("Cannot pop from an empty stack")
        else:
            temp = self.header
            self.header = self.header.next
            temp.next = None
            self.size -= 1
            return temp.description


