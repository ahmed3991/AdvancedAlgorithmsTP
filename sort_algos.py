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
    
 n = len(arr)
    for i in range(n):
       
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
            
                arr[j], arr[j+1] = arr[j+1], arr[j]

def insertion_sort_by_shifting(arr):

     n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        # Shift elements of arr[0..i-1], that are greater than key, to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

def insertion_sort_by_exchanges(arr):
    
 n = len(arr)
    for i in range(1, n):
        for j in range(i, 0, -1):
            if arr[j] < arr[j-1]:
                # Swap the elements
                arr[j], arr[j-1] = arr[j-1], arr[j]
            else:
                break
## TODO: make Benchmarks

print('hello')