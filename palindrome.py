class Dequeue:
    def __init__(self):
        self.items = []

    def enqueue(self, value):
        self.items.append(value)
    
    def leftEnqueue(self, value):
        self.items.insert(0, value)

    def dequeue(self):
        if len(self.items) == 0:
            print("Dequeue is empty.")
            return None;
        else:
            x = self.items[0]
            self.items.pop(0)
            return x

    def rightDequeue(self):
        if len(self.items) == 0:
            print("Dequeue is empty.")
            return None;
        else:
            x = self.items[len(self.items)-1]
            self.items.pop()
            return x

    def isEmpty(self):
        return len(self.items) == 0

    def front(self):
        if len(self.items) == 0:
            print("Dequeue is empty.")
            return None;
        else:
            x = self.items[0]
            return x

    def back(self):
        if len(self.items) == 0:
            print("Dequeue is empty.")
            return None;
        else:
            x = self.items[len(self.items)-1]
            return x

    def __len__(self):
        return len(self.items)



def isPalindrome(v):
    dequeue = Dequeue()

    for i in v:
        dequeue.enqueue(i)
    
    while len(dequeue) > 1:
        if dequeue.dequeue() != dequeue.rightDequeue():
            return False
    
    return True

