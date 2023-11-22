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


def main():
    pq = PriorityQueue()

    pq.enqueue("task1", 3)
    pq.enqueue("task2", 7)
    pq.enqueue("task3", 1)
    pq.enqueue("task4", 2)
    pq.enqueue("task5", 5)
    pq.enqueue("task6", 4)

    pq.displayQueue()

    pq.dequeue()
    pq.dequeue()
    pq.dequeue()

    pq.displayQueue()


main()
