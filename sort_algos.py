## TODO: TP should be HERE


## TODO: Data Generation


## TODO: Sort Algorithms implementations
## TODO: Selection Sort is our task now\
def selection_sort(arr):
    comparison = 0
    moves = 0
    arr = arr.copy()

    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            comparison += 1
            if arr[j] < arr[min_index]:
                min_index = j
        comparison += 1
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            moves += 1

    return comparison, moves

## TODO: make Benchmarks

print('hello')