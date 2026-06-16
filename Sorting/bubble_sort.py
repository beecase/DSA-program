def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
arr=[20,3,12,21,10,1,8]
print(f"Initial array:{arr}")
sorted_arr=bubble_sort(arr)
print(f'After bubble sort: {sorted_arr}')