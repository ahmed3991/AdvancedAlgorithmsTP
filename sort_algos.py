import numpy as np
import pandas as pd
from tqdm import tqdm

## TODO: TP should be HERE


## TODO: Data Generation

lengths =[10,100,1000,10000]

# TODO : Use numpy
random_arrays= [np.random.randint(0, 10000, size=l).tolist() for l in lengths]
# TODO : Use range
sorted_arrays= [list(range(l)) for l in lengths]
# TODO : Use range
inverse_sorted_arrays = [list(range(l, 0, -1)) for l in lengths]

nbr_experiments = 10

## TODO: Sort Algorithms implementations
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


# Benchmarking code
funcs = [selection_sort, bubble_sort, insertion_sort_shifting, insertion_sort_exchange]

results = []

for func in tqdm(funcs, desc="Algorithms"):
    for arr_type, arrays in zip(
        ["Random", "Sorted", "Inverse Sorted"],
        [random_arrays, sorted_arrays, inverse_sorted_arrays],
    ):
        for arr in arrays:
            total_comparisons = 0
            total_swaps = 0

            # Repeat experiment
            for _ in range(nbr_experiments):
                comparisons, swaps = func(arr)
                total_comparisons += comparisons
                total_swaps += swaps

            # Average results
            avg_comparisons = total_comparisons / nbr_experiments
            avg_swaps = total_swaps / nbr_experiments

            results.append(
                {
                    "Algorithm": func.__name__,
                    "Array Type": arr_type,
                    "Array Length": len(arr),
                    "Avg Comparisons": avg_comparisons,
                    "Avg Swaps": avg_swaps,
                }
            )

df_results = pd.DataFrame(results)

print(df_results)