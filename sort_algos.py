import numpy as np
import pandas as pd
from tqdm import tqdm
import time


np.random.seed(42)


lengths = [ 10, 100, 1000]
tests_per_length = 30
scenarios = ['random', 'ascending', 'descending']

tests = []

for length in lengths:
    for scenario in scenarios:
        for _ in range(tests_per_length):
            if scenario == 'random':
                val = np.random.randint(1, 4 * length, size=length)
            elif scenario == 'ascending':
                val = np.sort(np.random.randint(1, 4 * length, size=length))
            elif scenario == 'descending':
                val = np.sort(np.random.randint(1, 4 * length, size=length))[::-1]

            tests.append((length, scenario, val.copy()))


def selection_sort(arr):
    comparisons = 0
    moves = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # swap
        moves += 2  # counting the swap
    return comparisons, moves


def bubble_sort(arr):
    comparisons = 0
    moves = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # swap
                moves += 2  # counting the swap
    return comparisons, moves

def insertion_sort_exchange(arr):
    comparisons = 0
    moves = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            moves += 1
            j -= 1
        arr[j + 1] = key
        moves += 1  # accounting for the insertion
    return comparisons, moves


def insertion_sort_shift(arr):
    comparisons = 0
    moves = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        comparisons += 1  # for the while condition check
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            moves += 1
            j -= 1
            comparisons += 1  # for each comparison in the loop
        arr[j + 1] = key
        moves += 1  # accounting for the insertion
    return comparisons, moves


results = []

for length, scenario, val in tqdm(tests, ncols=100):
    for sort_func in [selection_sort, bubble_sort, insertion_sort_exchange, insertion_sort_shift]:
        arr_copy = val.copy()
        
        start_time = time.time()
        comparisons, moves = sort_func(arr_copy)
        end_time = time.time()

        results.append((sort_func.__name__, length, scenario, comparisons, moves, end_time - start_time))


df = pd.DataFrame(results, columns=['function_name', 'array_length', 'scenario', 'comparisons', 'moves', 'time'])
print(df)


df.to_csv('sorting_results.csv', index=False)
