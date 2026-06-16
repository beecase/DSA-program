def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr=[20,3,12,21,10,1,8]
print(f"Initial array:{arr}")
sorted_arr= insertion_sort(arr)
print(f'After Insertion sort: {sorted_arr}')