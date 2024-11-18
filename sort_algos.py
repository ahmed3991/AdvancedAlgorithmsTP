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
    for i in range(n - 1):  
        for j in range(n - i - 1):  
            if arr[j] > arr[j + 1]:  
                arr[j], arr[j + 1] = arr[j + 1], arr
    print("Bubble Sort Result:", arr)

arr1 = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr1)


def insertion_sort_by_shifting(arr):

    n = len(arr)
    for i in range(1, n):  
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  
    print("Insertion Sort by Shifting Result:", arr)
arr2 = [64, 34, 25, 12, 22, 11, 90]
insertion_sort_by_shifting(arr2)


def insertion_sort_by_exchanges(arr):

    n = len(arr)
    for i in range(1, n):  
        for j in range(i, 0, -1):  
            if arr[j] < arr[j - 1]: 
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
            else:
                break 
    print("Insertion Sort by Exchanges Result:", arr)
arr3 = [64, 34, 25, 12, 22, 11, 90]
insertion_sort_by_exchanges(arr3)


print('hello')