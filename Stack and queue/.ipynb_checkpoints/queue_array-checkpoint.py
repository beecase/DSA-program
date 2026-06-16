class ArrayQueue:
   
    def __init__(self):
        """Initializes an empty queue."""
        self.queue = []

    def is_empty(self):
        """Checks if the queue is empty."""
        return len(self.queue) == 0

    def enqueue(self, item):
        """Adds an item to the rear of the queue.S"""
        self.queue.append(item)
        print(f"Enqueued {item}.")

    def dequeue(self):
        
        if self.is_empty():
            raise Exception("Queue Underflow: Cannot dequeue from an empty queue.")
        return self.queue.pop(0)

    def front_element(self):
        """Returns the front element without removing it."""
        if self.is_empty():
            raise Exception("Queue is empty.")
        return self.queue[0]

    def size(self):
        """Returns the number of items in the queue."""
        return len(self.queue)


print("\n--- Queue Example ---")
q = ArrayQueue()
q.enqueue(10)
q.enqueue(20)
print(f"Dequeued: {q.dequeue()}")
