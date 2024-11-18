## TODO: TP should be HERE
pass

## TODO: Data Generation
pass

## TODO: Sort Algorithms implementations
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


## TODO: Selection Sort is our task now
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):       
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  
    return arr



## TODO: make Benchmarks
import time

def benchmark_sorting(sort_function, array):
    start_time = time.time()
    sort_function(array.copy())  
    end_time = time.time()
    return end_time - start_time


print('hello')