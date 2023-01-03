class Queue:
    def __init__(self):
        self.items = []
        self.front_index = 0

    def enqueue(self, value):
        self.items.append(value)

    def dequeue(self):
        if self.front_index == len(self.items):
            print("Queue is empty.")
            return None;
        else:
            x = self.items[self.front_index]
            self.front_index += 1
            return x

    def isEmpty(self):
        return self.front_index == len(self.items)

    def front(self):
        if self.front_index == len(self.items):
            print("Queue is empty.")
            return None;
        else:
            x = self.items[self.front_index]
            return x

    def __len__(self):
        return len(self.items)



def Josephus(n, k):
    queue = Queue()

    for v in range(1, n+1):
        queue.enqueue(v)
    
    while len(queue) > 1:
        for i in range(1, k):
            queue.enqueue(queue.dequeue())
        queue.dequeue()
    
    return queue.dequeue()