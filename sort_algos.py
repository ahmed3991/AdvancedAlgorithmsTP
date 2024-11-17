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

    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i - 1):
            comparison_count += 1
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                move_count += 1
                swapped = True
        # If no two elements were swapped, the array is sorted
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
        
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0:
            comparison_count += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]  # Shift element to the right
                move_count += 1
                j -= 1
            else:
                break
        
        # Insert the key at the correct position
        arr[j + 1] = key
        move_count += 1  # Account for the final placement of the key

    return comparison_count, move_count


def insertion_sort_by_exchanges(arr):
    comparison_count = 0
    move_count = 0
    arr = arr.copy()

    for i in range(1, len(arr)):
        j = i
        while j > 0:
            comparison_count += 1
            if arr[j] < arr[j - 1]:
                # Swap the elements
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                move_count += 1
                j -= 1
            else:
                break

    return comparison_count, move_count


## TODO: make Benchmarks

print('hello')