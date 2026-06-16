"""Here,Ssmaller number has higher priority"""
class PriorityQueueArray:
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
        self.queue.sort()   # Maintain priority order

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        print("Queue Underflow")

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print(self.queue)

"""Example"""
pq = PriorityQueueArray()
pq.enqueue(30)
pq.enqueue(10)
pq.enqueue(20)
pq.display()
print("Removed:", pq.dequeue())
pq.display()