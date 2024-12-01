## TODO: TP should be HERE


## TODO: Data Generation
import csv
import numpy as np
lenghts =[10,100,1000,10000]

# TODO : Use numpy
random_arrays= [np.random.randint(0, 10000, size=l).tolist() for l in lenghts]
# TODO : Use range
sorted_arrays= [list(range(l)) for l in lenghts]
# TODO : Use range
inverse_sorted_arrays = [list(range(l, 0, -1)) for l in lenghts]

nbr_experiments = 10


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
funcs = [selection_sort, bubble_sort, insertion_sort_shifting, insertion_sort_exchange]


results = []

for func in funcs:
    print(f"Testing function: {func.__name__}")
    
   
    for array_type, arrays in zip(["Random", "Sorted", "Inverse Sorted"], [random_arrays, sorted_arrays, inverse_sorted_arrays]):
        
       
        for arr in arrays:
            print(f"Running on {array_type} array of length {len(arr)}")
            
            
            for _ in range(nbr_experiments):
                performance = func(arr)
                results.append((func.__name__, array_type, len(arr), performance))


print("\nBenchmark Results:")
for result in results:
    algorithm, array_type, length, performance = result
    comparisons, swaps = performance
    print(f"Algorithm: {algorithm}, Array Type: {array_type}, Length: {length}, Comparisons: {comparisons}, Swaps: {swaps}")
   
    with open("benchmark_results.csv", mode="w", newline='') as file:
      writer = csv.writer(file)
      writer.writerow(["Algorithm", "Array Type", "Length", "Comparisons", "Swaps"])  # Header row
      for result in results:
        writer.writerow(result)

print("Results saved to benchmark_results.csv")