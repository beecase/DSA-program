from singlylinked_list import SinglyLinkedList 

class Queue:
    def __init__(self):
        self.sll = SinglyLinkedList()

    # Enqueue
    def enqueue(self, data):
        self.sll.insert_end(data)
        print(f"Enqueued {data} to queue")

    # Dequeue
    def dequeue(self):
        if self.is_empty():
            print("Queue is empty. Cannot dequeue.")
            return None
        front_value = self.sll.head.data
        self.sll.delete_beginning()
        print(f"Dequeued {front_value} from queue")
        return front_value

    # Peek front element
    def peek(self):
        if self.is_empty():
            print("Queue is empty.")
            return None
        return self.sll.head.data

    
    def is_empty(self):
        return self.sll.head is None

    
    def display(self):
        print("Queue from front to rear:")
        self.sll.traverse()


# Example Usage
queue = Queue()
queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)
queue.display()

print("\nPeek front element:", queue.peek())

queue.dequeue()
queue.display()

queue.dequeue()
queue.dequeue()
queue.dequeue()  # trying to dequeue from empty queue