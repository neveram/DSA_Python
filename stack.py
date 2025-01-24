class Stack:
    def __init__(self, size):
        self.items = [0] * size
        self.capacity = size
        self.top = -1
    
    def push(self, item):
        if self.is_full():
            print("Stack overflow")
            return
        self.top += 1
        self.items[self.top] = item
    
    def pop(self):
        if self.is_empty():
            print("Stack underflow")
            return None
        item = self.items[self.top]
        self.top -= 1
        return item
    
    def is_empty(self):
        return self.top == -1
    
    def is_full(self):
        return self.top == self.capacity - 1

# Usage
stack = Stack(5)
stack.push(5)
stack.push(1)
stack.push(2)
stack.push(3)
stack.push(4)
stack.push(9)