import numpy as np
from complexity import time_and_space_profiler
import pandas as pd
from tqdm import tqdm

## TODO: Data Generation

np.random.seed(42)

array_sizes = [1000, 10000, 100000]
array_types = ['random', 'ascending', 'descending']
tests = []

for size in array_sizes:
    for array_type in array_types:
        if array_type == 'random':
            arr = np.random.randint(0, size * 10, size)
        elif array_type == 'ascending':
            arr = np.arange(size)
        elif array_type == 'descending':
            arr = np.arange(size, 0, -1)
        tests.append((size, arr.copy(), array_type))

## TODO: Sort Algorithms implementations

@time_and_space_profiler
def selection_sort(arr):
    comparisons = 0
    moves = 0
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        moves += 1
    return comparisons, moves

@time_and_space_profiler
def bubble_sort(arr):
    comparisons = 0
    moves = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                moves += 1
                swapped = True
        if not swapped:
            break
    return comparisons, moves

@time_and_space_profiler
def insertion_sort_exchanges(arr):
    comparisons = 0
    moves = 0
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            comparisons += 1
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            moves += 1
            j -= 1
        comparisons += 1  # for the last failed comparison
    return comparisons, moves

@time_and_space_profiler
def insertion_sort_shifting(arr):
    comparisons = 0
    moves = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            moves += 1
            j -= 1
        comparisons += 1  # for the last failed comparison
        arr[j + 1] = key
        moves += 1
    return comparisons, moves

## TODO: make Benchmarks

sorting_algorithms = [selection_sort, bubble_sort, insertion_sort_exchanges, insertion_sort_shifting]
results = []

for algo in sorting_algorithms:
    for size, arr, array_type in tqdm(tests, desc=f"Running {algo.__name__}", unit='test'):
        func_name, (comparisons, moves), exec_time, memory = algo(arr.copy())
        results.append((func_name, size, array_type, comparisons, moves, exec_time, memory))

df = pd.DataFrame(results, columns=['Algorithm', 'Array Size', 'Array Type', 'Comparisons', 'Moves', 'Execution Time', 'Memory Usage'])
print(df)

df.to_csv('sorting_results.csv', index=False)
