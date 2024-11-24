## TODO: TP should be HER
from tqdm import tqdm
import numpy as np
import pandas as pd

# Data Generation
lengths = [10, 100, 1000, 10000]

# Generate random arrays using NumPy
random_arrays = [np.random.randint(0, 100, size=length) for length in lengths]

# Generate sorted arrays using range
sorted_arrays = [np.array(range(length)) for length in lengths]

# Generate inverse sorted arrays
inverse_sorted_arrays = [np.array(range(length - 1, -1, -1)) for length in lengths]

nbr_experiments = 10

# Sorting Functions
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

    return comparisons, swaps


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

    return comparisons, swaps


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

    return comparisons, swaps


# Sorting functions to test
funcs = [selection_sort, bubble_sort, insertion_sort_shifting, insertion_sort_exchange]

# Running Experiments
results = []

for length, random_array, sorted_array, inverse_sorted_array in tqdm(
    zip(lengths, random_arrays, sorted_arrays, inverse_sorted_arrays), 
    total=len(lengths), 
    desc="Processing Experiments"
):
    for func in funcs:
        for experiment_type, array in [
            ("Random", random_array), 
            ("Sorted", sorted_array), 
            ("Inverse Sorted", inverse_sorted_array)
        ]:
            comparisons, swaps = func(array)
            results.append({
                "Function": func.__name__,
                "Array Type": experiment_type,
                "Array Length": length,
                "Comparisons": comparisons,
                "Swaps": swaps,
            })

df_results = pd.DataFrame(results)
print(df_results)
df_results.to_csv("sorting_experiment_results.csv", index=False)
