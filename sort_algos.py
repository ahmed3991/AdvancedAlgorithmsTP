## TODO: TP should be HERE


## TODO: Data Generation


## TODO: Sort Algorithms implementations
def selection_sort(arr):
    comparison_count = 0
    move_count = 0
    arr = arr.copy()

    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            comparison_count += 1
            if arr[j] < arr[min_index]:
                min_index = j
        comparison_count += 1
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            move_count += 1

    return comparison_count, move_count

## TODO: Complete the code
# Bubble Sort
def bubble_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swaps += 2
    return array


# Insertion Sort by Shifting
def insertion_sort_shifting(array):
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            comparisons += 1
            array[j + 1] = array[j]
            swaps += 1
            j -= 1
        array[j + 1] = key
        swaps += 1
    return array

# Insertion Sort by Exchanges
def insertion_sort_exchanges(array):
    n = len(array)
    for i in range(1, n):
        for j in range(i, 0, -1):
            comparisons += 1
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
                swaps += 2
            else:
                break
    return array

## TODO: make Benchmarks

print('hello')

