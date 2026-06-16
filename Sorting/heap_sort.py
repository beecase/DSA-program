def heapify(arr, n, i):
    largest = i        # assume root is largest
    left = 2 * i + 1   # left child
    right = 2 * i + 2  # right child

    # check if left child is larger
    if left < n and arr[left] > arr[largest]:
        largest = left

    # check if right child is larger
    if right < n and arr[right] > arr[largest]:
        largest = right

    # if largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


def heap_sort(arr):
    n = len(arr)

    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extract elements one by one
    for i in range(n - 1, 0, -1):
        # swap current root (largest) with end
        arr[i], arr[0] = arr[0], arr[i]

        # call heapify on reduced heap
        heapify(arr, i, 0)


# Example usage

data = [20,3,12,21,10,1,8]
print("Original array:", data)

heap_sort(data)

print("After heap sort:", data)