class StackList:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.is_empty():
            print("Stack Underflow")
            return None
        return self.stack.pop()

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def display(self):
        print(self.stack)

#Example
s = StackList()
s.push(5)
s.push(15)
s.push(25)
print("After pushing 3 elements one by one:")
s.display()
print("Popped:", s.pop())
print("After popping elements:")
s.display()