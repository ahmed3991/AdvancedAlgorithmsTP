## TODO: TP should be HERE


## TODO: Data Generation

lenghts =[10,100,1000,10000]

# TODO : Use numpy
random_arrays= []
import numpy as np
array_10 = np.random.rand(10)
array_100 = np.random.rand(100)
array_1000 = np.random.rand(1000)
array_10000 = np.random.rand(10000)

sorted_arrays= []
import numpy as np
array_10 = np.linspace(1, 10, 10) 
array_100 = np.linspace(1, 100, 100)  
array_1000 = np.linspace(1, 1000, 1000)  
array_10000 = np.linspace(1, 10000, 10000)  

inverse_sorted_arrays = []
import numpy as np
array_10 = np.linspace(1, 10, 10)[::-1] 
array_100 = np.linspace(1, 100, 100)[::-1] 
array_1000 = np.linspace(1, 1000, 1000)[::-1]  
array_10000 = np.linspace(1, 10000, 10000)[::-1] 



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
    comparisons = 0
    swaps = 0
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return  comparisons, swaps


def insertion_sort_shifting(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]  # Shift
            swaps += 1
            j -= 1
        arr[j + 1] = key

        if j != i - 1:
            comparisons += 1

    return  comparisons, swaps
def insertion_sort_exchange(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)

    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            comparisons += 1
            arr[j], arr[j - 1] = arr[j - 1], arr[j]  # Swap
            swaps += 1
            j -= 1

        if j > 0:
            comparisons += 1

    return  comparisons, swaps



funcs = [selection_sort, bubble_sort,insertion_sort_shifting,insertion_sort_exchange]

results = []
 
# TODO: Complete the benchmark code