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
    for i in range(0, len(arr)-1):#i for minus from array long
        for j in range(0, len(arr)-1-i):
            if  arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1],  arr[j]

def insertion_sort_by_shifting(arr):
    for i in range(1, len(arr)):
        k = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > k :
            arr[j+1] = arr[j]
            j = j - 1
            arr[j+1] = k

def insertion_sort_by_exchanges(arr):
        for i in range(1, len(arr)):
            j = i - 1
        while j >= 0 and arr[j]>arr[j+1]:
            arr[j], arr[j+1] = arr[j+1],  arr[j]
            j=j-1

## TODO: make Benchmarks

print('hello')