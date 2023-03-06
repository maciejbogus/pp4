class Queue:
    def __init__(self):
        self.queue = []    

    def push(self, value):
        self.queue.append(value)
    
    def pop(self):
        if not self.empty():
            return self.queue.pop(0)
        else:
            return None

    def empty(self):
        return len(self.queue) == 0

    def display(self):
        for i in self.queue:
            print(i, end=" ")
        print()

q1 = Queue()
q1.push("2")
q1.push("3")
q1.push("4")
q1.display()
q1.pop()
q1.display()
q1.pop()
q1.display()
