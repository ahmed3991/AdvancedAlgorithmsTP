## TODO: TP should be HERE


## TODO: Data Generation


## TODO: Sort Algorithms implementations
## TODO: Selection Sort is our task now
@time_and_space_profiler
def tri_selection(t):
    comparisons, moves = 0, 0
    n = len(t)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if t[j] < t[min_index]:
                min_index = j
        if min_index != i:
            t[i], t[min_index] = t[min_index], t[i]
            moves += 1
    return comparisons, moves

## TODO: make Benchmarks

print('hello')