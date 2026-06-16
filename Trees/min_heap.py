class MinHeap:
    def __init__(self):
        self.heap = []

    # Get parent index
    def parent(self, i):
        return (i - 1) // 2

    # Get left child index
    def left_child(self, i):
        return 2 * i + 1

    # Get right child index
    def right_child(self, i):
        return 2 * i + 2

    # Insert element
    def insert(self, key):
        self.heap.append(key)
        self._heapify_up(len(self.heap) - 1)

    # Heapify up (for insert)
    def _heapify_up(self, i):
        while i > 0 and self.heap[self.parent(i)] > self.heap[i]:
            # Swap
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    # Remove minimum element (root)
    def extract_min(self):
        if len(self.heap) == 0:
            print("Heap is empty")
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # Move last to root
        self._heapify_down(0)
        return root

    # Heapify down (for delete)
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

    # Get minimum element
    def get_min(self):
        return self.heap[0] if self.heap else None

    # Display heap
    def display(self):
        print(self.heap)


#EXAMPLE USAGE
if __name__ == "__main__":
    h = MinHeap()

    h.insert(10)
    h.insert(5)
    h.insert(20)
    h.insert(2)

    print("Heap:", h.heap)

    print("Min element:", h.get_min())

    print("Extract Min:", h.extract_min())
    print("Heap after extraction:", h.heap)