## TODO: TP should be HERE


## TODO: Data Generation

import numpy as np
import pandas as pd
import time

lengths = [10, 100, 1000, 10000]
nbr_experiments = 10

# TODO : Use numpy
random_arrays = [
    [np.random.randint(0, 1000, size=length) for _ in range(nbr_experiments)]
    for length in lengths
]

# TODO : Use range
sorted_arrays = [
    [np.arange(length) for _ in range(nbr_experiments)]
    for length in lengths
]


# TODO : Use range
inverse_sorted_arrays = [
    [np.arange(length - 1, -1, -1) for _ in range(nbr_experiments)]
    for length in lengths
]

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



funcs =[
    ("selection_sort", selection_sort),
    ("bubble_sort", bubble_sort),
    ("insertion_sort_shifting", insertion_sort_shifting),
    ("insertion_sort_exchange", insertion_sort_exchange),
]

array_types = {
    "random": random_arrays,
    "sorted": sorted_arrays,
    "inverse_sorted": inverse_sorted_arrays,
}

results = []

id_test = 1

for array_type, arrays_by_length in test_arrays.items():
    for length_idx, arrays in enumerate(arrays_by_length):
        array_length = lengths[length_idx]
        for arr in arrays:
            for func_name, func in functions.items():

                start_time = time.time()
                comparisons, swaps = func(arr)
                elapsed_time = time.time() - start_time

                results.append([
                    test_id, func_name, array_length, comparisons, swaps, elapsed_time, array_type
                ])
                test_id += 1

# Save results to CSV
df = pd.DataFrame(results, columns=['id_test', 'function_name', 'array_length', 'comparison', 'swaps', 'time', 'array_type'])
df.to_csv('results.csv', index=False)

print("Results saved to 'results.csv'.")

# TODO: Complete the benchmark code
