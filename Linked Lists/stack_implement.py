from singlylinked_list import SinglyLinkedList  

class Stack:
    def __init__(self):
        self.sll = SinglyLinkedList()

    
    def push(self, data):
        self.sll.insert_beginning(data)
        print(f"Pushed {data} onto stack")

    
    def pop(self):
        if self.is_empty():
            print("Stack is empty. Cannot pop.")
            return None
        top_value = self.sll.head.data
        self.sll.delete_beginning()
        print(f"Popped {top_value} from stack")
        return top_value

    
    def peek(self):
        if self.is_empty():
            print("Stack is empty.")
            return None
        return self.sll.head.data

    
    def is_empty(self):
        return self.sll.head is None

    
    def display(self):
        print("Stack from top to bottom:")
        self.sll.traverse()


# Driver Program
stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.display()

print("\nPeek top element:", stack.peek())

stack.pop()
stack.display()

stack.pop()
stack.pop()
stack.pop()  # trying to pop from empty stack