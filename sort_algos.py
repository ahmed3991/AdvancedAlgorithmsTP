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
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]: 
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


numbers = [64, 34, 25, 12, 22, 11, 90]
print("Before arranging:", numbers)
bubble_sort(numbers)
print("After ranking:", numbers)


def insertion_sort_by_shifting(arr):
    for i in range(1, len(arr)):
        key = arr[i] 
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

numbers = [64, 34, 25, 12, 22, 11, 90]
print("Before arranging :", numbers)
insertion_sort_by_shifting(numbers)
print(" After ranking:", numbers)


def insertion_sort_by_exchanges(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]  
            j -= 1

numbers = [64, 34, 25, 12, 22, 11, 90]
print(" Before arranging:", numbers)
insertion_sort_by_exchanges(numbers)
print(" After ranking:", numbers)


## TODO: make Benchmarks

print('hello')