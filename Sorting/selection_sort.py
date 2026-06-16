def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

arr=[20,3,12,21,10,1,8]
print(f"Initial array:{arr}")
sorted_arr= selection_sort(arr)
print(f'After Selection sort: {sorted_arr}')