## TODO: TP should be HERE


## TODO: Data Generation


## TODO: Sort Algorithms implementations
## TODO: Selection Sort is our task now
def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr
arr = [64, 25, 12, 22, 11]
arr1 = selection_sort(arr)
print("arr", arr1)




## TODO: make Benchmarks

print('Hello')