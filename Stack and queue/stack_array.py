class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.stack = [None] * capacity
        self.top = -1

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.capacity - 1

    def push(self, item):
        if self.is_full():
            raise Exception("Stack Overflow")
        self.top += 1
        self.stack[self.top] = item
        print(f"Pushed {item} to stack.")

    def pop(self):
        if self.is_empty():
            raise Exception("Stack Underflow")
        item = self.stack[self.top]
        self.stack[self.top] = None
        self.top -= 1
        return item

    def peek(self):
        if self.is_empty():
            raise Exception("Stack is Empty.")
        return self.stack[self.top]

    def size(self):
        return self.top + 1

