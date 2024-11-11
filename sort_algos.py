## TODO: TP should be HERE


## TODO: Data Generation


## TODO: Sort Algorithms implementations
#Selection Sort
def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
    return array
## TODO: Selection Sort is our task now


## TODO: make Benchmarks

print('hello')