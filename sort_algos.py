import time
import random
import numpy as np
import pandas as pd
## TODO: TP should be HERE

np.random.seed(42)
## TODO: Data Generation

# Reset performance metrics
def reset_metrics():
    global comparisons, swaps
    comparisons = 0
    swaps = 0

## TODO: Sort Algorithms implementations

# Selection Sort
def selection_sort(array):
    global comparisons, swaps
    reset_metrics()
    n = len(array)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if array[j] < array[min_idx]:
                min_idx = j
        array[i], array[min_idx] = array[min_idx], array[i]
        swaps += 2
    return array

# Bubble Sort
def bubble_sort(array):
    global comparisons, swaps
    reset_metrics()
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                swaps += 2
    return array

# Insertion Sort by Exchanges
def insertion_sort_exchanges(array):
    global comparisons, swaps
    reset_metrics()
    n = len(array)
    for i in range(1, n):
        for j in range(i, 0, -1):
            comparisons += 1
            if array[j] < array[j - 1]:
                array[j], array[j - 1] = array[j - 1], array[j]
                swaps += 2
            else:
                break
    return array

# Insertion Sort by Shifting
def insertion_sort_shifting(array):
    global comparisons, swaps
    reset_metrics()
    n = len(array)
    for i in range(1, n):
        key = array[i]
        j = i - 1
        while j >= 0 and array[j] > key:
            comparisons += 1
            array[j + 1] = array[j]
            swaps += 1
            j -= 1
        array[j + 1] = key
        swaps += 1
    return array



## TODO: measure_performance

def measure_performance(algorithme, array):
    reset_metrics()
    start_time = time.time()
    copy_array = array[:]  # Create a shallow copy of the array
    sorted_array = algorithme(copy_array)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    return execution_time, comparisons, swaps


## TODO: make Benchmarks

def analyze_algorithms():
    data = []
    array_sizes = [1000, 5000, 10000]
    tests = 5
    for size in array_sizes:
        random_array = random.sample(range(size * 10), size)
        ascending_array = sorted(random_array)
        descending_arr = sorted(random_array, reverse=True)

    for array_type, arr in [('Random', random_array), ('Ascending', ascending_array), ('Descending', descending_arr)]:
        for algo_name, algo_function in [
            ('Selection Sort', selection_sort),
            ('Bubble Sort', bubble_sort),
            ('Insertion Sort (Exchanges)', insertion_sort_exchanges),
            ('Insertion Sort (Shifting)', insertion_sort_shifting)
        ]:
            comparisons_list = []
            swaps_list = []
            time_list = []
            
            for _ in range(tests):
                exec_time, comparisons, swaps = measure_performance(algo_function, arr)
                comparisons_list.append(comparisons)
                swaps_list.append(swaps)
                time_list.append(exec_time)

            Avg_comparisons = np.mean(comparisons_list)
            Avg_swaps = np.mean(swaps_list)
            Avg_time = np.mean(time_list)
            
            data.append({
                'Algorithme': algo_name,
                'Array Type': array_type,
                'Array Size': size,
                'Avg Comparisons': Avg_comparisons,
                'Avg Swaps': Avg_swaps,
                'Avg Time (ms)': Avg_time
            })

    df = pd.DataFrame(data)
    return df

data_frame = analyze_algorithms()
print(data_frame)
data_frame.to_csv('results.csv', index=False)
