## TODO: TP should be HERE
import numpy as np
import pandas as pd
from tqdm import tqdm
import time

## TODO: Data Generation
array_sizes = [1000, 10000, 100000]
data_types = {"Random": lambda n: np.random.randint(0, n, n),
              "Ascending": lambda n: np.arange(n),
              "Descending": lambda n: np.arange(n, 0, -1)}
# Function to count comparisons and swaps
def init_profiler():
    return {"comparisons": 0, "swaps": 0, "start_time": time.time()}

## TODO: Sort Algorithms implementations
# Selection Sort
def selection_sort(arr):
    profiler = init_profiler()
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            profiler["comparisons"] += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        profiler["swaps"] += 1
    profiler["time"] = time.time() - profiler["start_time"]
    return profiler
# Bubble Sort
def bubble_sort(arr):
    profiler = init_profiler()
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - 1 - i):
            profiler["comparisons"] += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                profiler["swaps"] += 1
                swapped = True
        if not swapped:
            break
    profiler["time"] = time.time() - profiler["start_time"]
    return profiler

# Insertion Sort by shifting
def insertion_sort_shift(arr):
    profiler = init_profiler()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            profiler["comparisons"] += 1
            arr[j + 1] = arr[j]
            profiler["swaps"] += 1
            j -= 1
        arr[j + 1] = key
    profiler["time"] = time.time() - profiler["start_time"]
    return profiler


## TODO: make Benchmarks

results = []
for size in array_sizes:
    for label, data_gen in data_types.items():
        arr = data_gen(size)
        for sort_func in [selection_sort, bubble_sort, insertion_sort_shift]:
            
            data_copy = arr.copy()
            metrics = sort_func(data_copy)
            results.append({
                "algorithm": sort_func.name,
                "data_type": label,
                "size": size,
                "comparisons": metrics["comparisons"],
                "swaps": metrics["swaps"],
                "time": metrics["time"]
            })  

# Output Results
df = pd.DataFrame(results)
df.to_csv('sort_benchmarks.csv', index=False)
print(df)