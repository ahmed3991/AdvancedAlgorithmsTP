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
    comparison_count = 0
    move_count = 0
    arr = arr.copy()
    
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - 1 - i):  
            comparison_count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                move_count += 1
                swapped = True
        if not swapped:
            break

    return comparison_count, move_count


def insertion_sort_by_shifting(arr):
    comparison_count = 0
    move_count = 0
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparison_count += 1
            arr[j + 1] = arr[j]
            move_count += 1
            j -= 1
        comparison_count += 1
        arr[j + 1] = key

    return comparison_count, move_count


def insertion_sort_by_exchanges(arr):
    comparison_count = 0
    move_count = 0
    arr = arr.copy()
    
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            comparison_count += 1
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            move_count += 1
            j -= 1
        comparison_count += 1

    return comparison_count, move_count


## TODO: make Benchmarks

print('hello')