## TODO: TP should be HERE
import numpy as np
import time
import tracemalloc

import pandas as pd

## TODO: Data Generation

lenghts =[10,100,1000]

# TODO : Use numpy
random_arrays= []
# TODO : Use range
sorted_arrays= []
# TODO : Use range
inverse_sorted_arrays = []

nbr_experiments = 10


def selection_sort(arr):
    comparisons = 0
    swaps = 0
    arr = arr.copy()

    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        comparisons += 1
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1

    return comparisons, swaps

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
random_arrays = [np.random.randint(0, 1000, size=n).tolist() for n in lenghts]
sorted_arrays = [list(range(n)) for n in lenghts]
inverse_sorted_arrays = [list(range(n, 0, -1)) for n in lenghts]
for func in funcs:
    for arr_type, arrays in zip(["Random", "Sorted", "Inverse Sorted"],
                                [random_arrays, sorted_arrays, inverse_sorted_arrays]):
        for n, base_array in zip(lenghts, arrays):
            total_comparisons = 0
            total_swaps = 0
            total_time = 0
            total_memory = 0
            for _ in range(nbr_experiments):
                tracemalloc.start()
                start_time = time.perf_counter()

                comparisons, swaps = func(base_array)

                end_time = time.perf_counter()
                _, peak_memory = tracemalloc.get_traced_memory()
                tracemalloc.stop()
                total_comparisons += comparisons
                total_swaps += swaps
                total_time += (end_time - start_time)
                total_memory += peak_memory
            avg_comparisons = total_comparisons / nbr_experiments
            avg_swaps = total_swaps / nbr_experiments
            avg_time = total_time / nbr_experiments
            avg_memory = total_memory / nbr_experiments
            results.append({
                "Algorithm": func.__name__,
                "Array Type": arr_type,
                "Length": n,
                "Average Comparisons": avg_comparisons,
                "Average Swaps": avg_swaps,
                "Average Time (s)": avg_time,
                "Average Memory (KB)": avg_memory / 1024
            })
df = pd.DataFrame(results)
print(df)
df.to_csv("sorting_algorithms_results.csv", index=False)