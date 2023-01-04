class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        self.items.append(value)

    def pop(self):
        try:
            return self.items.pop()
        except IndexError:
            print("Stack is empty.")
    
    def top(self):
        try:
            return self.items[-1]
        except IndexError:
            print("Stack is empty.")

    def __len__(self):
        return len(self.items)

    def isEmpty(self):
        return len(self) == 0



def parChec(parSeq):
    stack = Stack()

    for s in parSeq:
        if s == "(":
            stack.push(s)
        else:
            if stack.isEmpty():
                return False
            else:
                stack.pop()
    
    if stack.isEmpty():
        return True
    else:
        return False