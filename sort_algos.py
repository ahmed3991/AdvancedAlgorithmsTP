import numpy as np
import pandas as pd
from complexity import time_and_space_profiler
from tqdm import tqdm


ARRAY_SIZES = [100, 500, 1000,10000] 
TEST_REPEATS = 3 


def generate_test_data(array_size, order='random'):
    array = np.random.randint(1, 4 * array_size, size=array_size)
    if order == 'ascending':
        return np.sort(array)
    elif order == 'descending':
        return np.sort(array)[::-1]
    return array

@time_and_space_profiler
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
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            move_count += 1

    return comparison_count, move_count

@time_and_space_profiler
def bubble_sort(arr):
    comparison_count = 0
    move_count = 0
    arr = arr.copy()

    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            comparison_count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                move_count += 1

    return comparison_count, move_count

@time_and_space_profiler
def insertion_sort_exchange(arr):
    comparison_count = 0
    move_count = 0
    arr = arr.copy()

    for i in range(1, len(arr)):
        for j in range(i, 0, -1):
            comparison_count += 1
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                move_count += 1
            else:
                break

    return comparison_count, move_count

@time_and_space_profiler
def insertion_sort_shift(arr):
    comparison_count = 0
    move_count = 0
    arr = arr.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparison_count += 1
            arr[j + 1] = arr[j]
            j -= 1
            move_count += 1
        arr[j + 1] = key

    return comparison_count, move_count

test_data = []
for size in tqdm(ARRAY_SIZES, desc="Generating Data", leave=True):
    for order in ['random', 'ascending', 'descending']:
        for _ in range(TEST_REPEATS):
            test_data.append((size, order, generate_test_data(size, order)))

results = []
for size, order, data in tqdm(test_data, desc="Testing Algorithms", leave=True):
    for sort_func in tqdm([selection_sort, bubble_sort, insertion_sort_exchange, insertion_sort_shift],
                          desc=f"Running Sort Functions on {size}-{order}", leave=False):
        func_name, (comparisons, moves), time, memory = sort_func(data)
        results.append((func_name, size, order, comparisons, moves, time, memory))

df = pd.DataFrame(results, columns=['Algorithm', 'Array Size', 'Order', 'Comparisons', 'Moves', 'Time', 'Memory'])

df.to_csv('sorting_results.csv', index=False)