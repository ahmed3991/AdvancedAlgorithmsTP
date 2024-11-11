## TODO: TP should be HERE


## TODO: Data Generation


## TODO: Sort Algorithms implementations
## TODO: Selection Sort is our task now

# Selection Sort with Shifting
def selection_sort_shift(arr):
    comparisons = 0
    shifts = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            min_val = arr[min_idx]
            for k in range(min_idx, i, -1):
                arr[k] = arr[k - 1]
                shifts += 1
            arr[i] = min_val
    return comparisons, shifts

# Selection Sort with Swapping
def selection_sort_swap(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
    return comparisons, swaps

## TODO: make Benchmarks

print('hello')