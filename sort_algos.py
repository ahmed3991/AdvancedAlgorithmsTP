## TODO: TP should be HERE


## TODO: Data Generation


## TODO: Sort Algorithms implementations


## TODO: make Benchmarks
import numpy as np
import pandas as pd
from time import time
from tqdm import tqdm

## TODO: TP should be HERE


## TODO: Data Generation


## TODO: Sort Algorithms implementations


## TODO: make Benchmarks

# Test data preparation
np.random.seed(42)
sizes = [1000, 10000, 100000]  # Add more sizes if desired
scenarios = ['random', 'ascending', 'descending']
tests = []

# Generate test cases for each scenario
for size in sizes:
    for scenario in scenarios:
        if scenario == 'random':
            array = np.random.randint(1, size * 10, size)
        elif scenario == 'ascending':
            array = np.arange(size)
        else:  # descending
            array = np.arange(size, 0, -1)
        tests.append((size, scenario, array.copy()))

# Sorting Algorithms with Profiling

def selection_sort(arr):
    comparisons, moves = 0, 0
    start_time = time()
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        moves += 2
    return comparisons, moves, time() - start_time

def bubble_sort(arr):
    comparisons, moves = 0, 0
    start_time = time()
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                moves += 2
    return comparisons, moves, time() - start_time

def insertion_sort_exchange(arr):
    comparisons, moves = 0, 0
    start_time = time()
    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            comparisons += 1
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                moves += 2
            else:
                break
    return comparisons, moves, time() - start_time

def insertion_sort_shift(arr):
    comparisons, moves = 0, 0
    start_time = time()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        comparisons += 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            moves += 1
            comparisons += 1
            j -= 1
        arr[j + 1] = key
        moves += 1
    return comparisons, moves, time() - start_time

# Run the sorting algorithms on all tests
results = []
algorithms = {
    'Selection Sort': selection_sort,
    'Bubble Sort': bubble_sort,
    'Insertion Sort (Exchange)': insertion_sort_exchange,
    'Insertion Sort (Shift)': insertion_sort_shift
}

for size, scenario, array in tqdm(tests, desc="Testing sorting algorithms"):
    for name, func in algorithms.items():
        arr_copy = array.copy()  # Copy array for each sort
        comparisons, moves, exec_time = func(arr_copy)
        results.append({
            'Algorithm': name,
            'Array Size': size,
            'Scenario': scenario,
            'Comparisons': comparisons,
            'Moves': moves,
            'Time (s)': exec_time
        })

# Store results in a DataFrame and save to CSV
df = pd.DataFrame(results)
print(df)
df.to_csv('sorting_algorithm_results.csv', index=False)
