class PriorityQueue:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    # Insert (enqueue)
    def enqueue(self, value):
        self.heap.append(value)
        self._heapify_up(len(self.heap) - 1)

    def _heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    # Remove highest priority (dequeue)
    def dequeue(self):
        if not self.heap:
            print("Priority Queue is empty")
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_down(self, i):
        smallest = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify_down(smallest)

    # Peek highest priority
    def peek(self):
        return self.heap[0] if self.heap else None

    # Display
    def display(self):
        print(self.heap)


#EXAMPLE USAGE
if __name__ == "__main__":
    pq = PriorityQueue()

    pq.enqueue(10)
    pq.enqueue(5)
    pq.enqueue(20)
    pq.enqueue(2)

    print("Priority Queue:", pq.heap)

    print("Peek (highest priority):", pq.peek())

    print("Dequeue:", pq.dequeue())
    print("After dequeue:", pq.heap)