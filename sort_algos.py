## TODO: TP should be HERE


## TODO: Data Generation


## TODO: Sort Algorithms implementations
def selection_sort(arr):
    comparison_count = 0
    moves = 0
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
            moves += 1

    return comparison_count, moves

## TODO: Complete the code

def bubble_sort(arr):  
    comparison = 0
    moves = 0
    arr = arr.copy()

    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            comparison += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                moves += 1

    return comparison, moves

def insertion_sort_by_shifting(arr):
    comparison = 0
    moves = 0
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparison += 1
            arr[j + 1] = arr[j]
            j -= 1
            moves += 1
        arr[j + 1] = key

    return comparison, moves

def insertion_sort_by_exchanges(arr):
    comparison = 0
    moves = 0
    arr = arr.copy()

    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            comparison += 1
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                moves += 1
            else:
                break

    return comparison, moves

## TODO: make Benchmarks

print('hello')