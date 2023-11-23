# Task Manager

class Task:
    task_id = -1

    def __init__(self, description, priority: int, completed: bool):
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
        if current is None:
            return "empty"
        while current.next is not None:
            print(current.priority, ":", current.description, current.completed, end=" -- ")
            current = current.next

        print(current.priority, ":", current.description, current.completed)

    def taskStatus(self):
        current = self.header
        c = []
        while current is not None:
            if current.completed:
                c.append(current.description)
            current = current.next
        print(c)

    def enqueue(self, description, priority, completed):

        node = Task(description, priority, completed)

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

                while current is not None and current.priority >= node.priority:
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


task_queue = PriorityQueue()
task_queue1 = PriorityQueue()


class Stack:

    def __init__(self):
        self.header = None
        self.size = 0

    def isEmpty(self):
        return self.header is None

    def displayStack(self):

        current = self.header

        while current is not None:
            print("|", current.description, "|")
            current = current.next

        print("---")

    def lastTask(self):
        current = self.header
        print(current.description, current.priority, current.completed)

    def push(self, description, priority, completed):
        node_to_add = Task(description, priority, completed)

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


task_history = Stack()


class TaskManager:

    # task_queue = []
    # task_history = []

    def __init__(self):
        self.cls = []
        self.tasks = []

    def adding(self, description):
        self.tasks.append(description)


task_manager = TaskManager()


def main():
    print("1. Adding a new task to the task manager.")
    print("2. Getting a task from the queue given a task id")
    print("3. Marking the highest priority task as completed and putting it in the task history.")
    print("4. Displaying all tasks in order of priority.")
    print("5. Displaying only the tasks that are not completed.")
    print("6. Displaying the last completed task.")
    print("7. EXIT")

    user_input = int(input("Enter your choice : "))
    if user_input == 1:
        task_status = False
        task_description = input("Enter the description for your task : ")
        try:
            task_priority = int(input("Enter the priority (more high more important) :"))
            task = Task(task_description, task_priority, task_status)
            task_manager.adding(task.description)
            task_queue.enqueue(task_description, task_priority, task_status)
            task_queue1.enqueue(task_description, task_priority, task_status)
            print(task_manager.tasks)
        except ValueError:
            print("Invalid input. Please enter a valid choice (integer) : ")

    elif user_input == 2:
        try:
            task_id = int(input("Enter task id : "))
            for task in task_manager.tasks:
                if task == task_manager.tasks[task_id]:
                    print(task)
        except ValueError:
            print("Invalid input. Please enter a valid choice (integer within the id<>) : ")

    elif user_input == 3:
        task1 = Task(task_queue.header.description, task_queue.header.priority, True)
        print(task1.description, task1.priority, task1.completed)
        task_history.push(task1.description, task1.priority, task1.completed)
        task_queue.dequeue()
        task_history.displayStack()

    elif user_input == 4:
        task_queue1.displayQueue()

    elif user_input == 5:
        task_queue.displayQueue()
    elif user_input == 6:
        task_history.lastTask()
    elif user_input == 7:
        exit()


while True:
    main()
