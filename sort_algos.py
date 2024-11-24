## TODO: TP should be HERE


## TODO: Data Generation
import numpy as np
import pandas as pd
from time import time
from complexity import time_and_space_profiler
from tqdm import tqdm

lengths =[10,100,1000,10000]
nbr_experiments = 10
# TODO : Use numpy
np.random.seed(42)
random_arrays= []
for length in lengths:
    for _ in range(nbr_experiments):
        arr = np.random.randint(1, 4 * length, size=length)
        random_arrays.append((length, arr))
# TODO : Use range
sorted_arrays= []
for length in lengths:
    for _ in range(nbr_experiments):
        sorted_arr = list(range(1, length + 1))
        sorted_arrays.append((length, sorted_arr))
# TODO : Use range
inverse_sorted_arrays = []
for length in lengths:
    for _ in range(nbr_experiments):
        inverse_sorted_arr = list(range(length, 0, -1))
        inverse_sorted_arrays.append((length, inverse_sorted_arr))
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
def benchmark_sorting_algorithm(arr, func):
    start_time = time()
    comparisons, swaps = func(arr)
    end_time = time()
    execution_time = end_time - start_time
    space_usage = np.array(arr).nbytes
    return comparisons, swaps, execution_time, space_usage
def run_benchmark_for_array_type(arrays, array_type):
    for length, arr in tqdm(arrays, ncols=70):#, desc=f"Benchmarking {array_type} Arrays"):
        for func in funcs:
            func_name = func.__name__
            comparisons, swaps, execution_time, space_usage = benchmark_sorting_algorithm(arr.copy(), func)
            results.append((func_name, length, comparisons, swaps, execution_time, space_usage, array_type))


run_benchmark_for_array_type(random_arrays, "random")
run_benchmark_for_array_type(sorted_arrays, "sorted")
run_benchmark_for_array_type(inverse_sorted_arrays, "inverse_sorted")

df = pd.DataFrame(results, columns=['function_name', 'array_length', 'comparisons', 'moves', 'execution_time', 'space_usage', 'array_type'])

print(df)
df.to_csv('results_for_sort_algos.csv', index=False)