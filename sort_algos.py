## TODO: TP should be HERE
import time

## TODO: Data Generation


## TODO: Sort Algorithms implementations
## TODO: Selection Sort is our task now
def selection_sort(data):
    comparisons = 0
    moves = 0
    start_time = time.time()
    n = len(data)
    for i in range(n):
        min_eidx = i
        for j in range(i + 1, n):
            comparisons += 1
            if data[j] < data[min_idx]:
                min_idx = j
        if min_idx != i:
            data[i], data[min_idx] = data[min_idx], data[i]
            moves += 1
    cpu_time = time.time() - start_time
    return comparisons, moves, cpu_time


## TODO: make Benchmarks

print('hello')