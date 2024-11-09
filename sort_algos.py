from complexity import time_and_space_profiler
from tqdm import tqdm, trange
import numpy as np
import pandas as pd

# Initialization logic
np.random.seed(42)

tests = []

# Array lengths for tests
lengths = np.array(range(10, 100, 2000))
tests_per_length = 5

for length in lengths:
    for _ in range(tests_per_length):
        val = np.random.randint(1, 4 * length, size=length)  # Generate random array
        tests.append((length, val))

# Sorting function definitions

# @time_and_space_profiler
def bubble_sort(arr):
    n = len(arr)
    comparison = 0
    for i in range(n):
        for j in range(0, n - i - 1):
            comparison += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr, comparison

# @time_and_space_profiler
def merge_sort(arr):
    comparison = [0]  # Using a list to mutate in recursive calls

    def merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparison[0] += 1
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    def recursive_sort(array):
        if len(array) <= 1:
            return array
        mid = len(array) // 2
        left = recursive_sort(array[:mid])
        right = recursive_sort(array[mid:])
        return merge(left, right)

    sorted_arr = recursive_sort(arr)
    return sorted_arr, comparison[0]

# @time_and_space_profiler
def quick_sort(arr):
    comparison = [0]

    def partition(low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            comparison[0] += 1
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def recursive_sort(low, high):
        if low < high:
            pi = partition(low, high)
            recursive_sort(low, pi - 1)
            recursive_sort(pi + 1, high)

    recursive_sort(0, len(arr) - 1)
    return arr, comparison[0]

# List of functions to test
funcs = [bubble_sort, merge_sort, quick_sort]

results = []
for i, (length, val) in tqdm(enumerate(tests), ncols=100):
    for func in funcs:
        sorted_val, comparison = func(val.copy())  # Use a copy to avoid modifying the original array
        results.append((i, func.__name__, length, comparison))

# Convert results to DataFrame and save to CSV
df = pd.DataFrame(results, columns=['id_test', 'function_name', 'array_length', 'comparison'])
print(df)

df.to_csv('results_sorting.csv', index=False)
