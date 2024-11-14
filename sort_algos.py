## TODO: TP should be HERE


## TODO: Data Generation


## TODO: Sort Algorithms implementations
## TODO: Selection Sort is our task now
def selection_sort(arr):
    """Sorts an array using the selection sort algorithm.
    Args:
        arr (list): Unsorted list of elements.
    Returns:
        list: Sorted list of elements.
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


## TODO: make Benchmarks

print('hello')