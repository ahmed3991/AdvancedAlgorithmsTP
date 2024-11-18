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

def bubble_sort(arr):
    """Bubble sort implementation."""
    comparison_count = 0
    move_count = 0
    arr = arr.copy()  # Create a copy to avoid modifying the original array

    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            comparison_count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                move_count += 1

    return comparison_count, move_count

def insertion_sort_by_shifting(arr):
    """Insertion sort implementation using shifting."""
    comparison_count = 0
    move_count = 0
    arr = arr.copy()  # Create a copy to avoid modifying the original array

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparison_count += 1
            arr[j + 1] = arr[j]
            move_count += 1
            j -= 1
        comparison_count += 1  # For the failed comparison
        arr[j + 1] = key

    return comparison_count, move_count

def insertion_sort_by_exchanges(arr):
    """Insertion sort implementation using exchanges."""
    comparison_count = 0
    move_count = 0
    arr = arr.copy()  # Create a copy to avoid modifying the original array

    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            comparison_count += 1
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                move_count += 1
            else:
                break

    return comparison_count, move_count


## TODO: make Benchmarks


print('hello') 
