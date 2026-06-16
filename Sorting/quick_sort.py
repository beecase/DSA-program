def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pivot = arr[len(arr) // 2]  # choosing middle element as pivot
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quick_sort(left) + middle + quick_sort(right)


# Example usage

data =[20,3,12,21,10,1,8]
print("Original array:", data)

sorted_data = quick_sort(data)
print("After quick sort:", sorted_data)