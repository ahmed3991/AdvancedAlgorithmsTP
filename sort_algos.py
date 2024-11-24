## TODO: TP should be HERE
import numpy as np
import pandas as pd
import time

## TODO: Data Generation

lengths =[10,100,1000]

# TODO : Use numpy
random_arrays = [np.random.randint(0, 1000, size=l).tolist() for l in lengths]
# TODO : Use range
sorted_arrays = [list(range(l)) for l in lengths]
# TODO : Use range
inverse_sorted_arrays = [list(range(l, 0, -1)) for l in lengths]

nbr_experiments = 10


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



funcs = [selection_sort, bubble_sort,insertion_sort_shifting,insertion_sort_exchange]

results = []
 
# TODO: Complete the benchmark code
for func in funcs:  # Iterate over sorting functions
    for arr_type, arrays in [("Random", random_arrays), 
                              ("Sorted", sorted_arrays), 
                              ("Inverse Sorted", inverse_sorted_arrays)]:
        for length, arr in zip(lengths, arrays):  # Iterate over array lengths
            total_comparisons = 0
            total_swaps = 0
            total_time = 0
            total_space = 0  # Placeholder for space complexity (optional)
            
            for _ in range(nbr_experiments):  # Perform multiple experiments
                arr_copy = arr.copy()  # To prevent altering the original array
                start_time = time.time()  # Start timer for time complexity
                comparisons, swaps = func(arr_copy)
                end_time = time.time()  # End timer for time complexity

                total_comparisons += comparisons
                total_swaps += swaps
                total_time += (end_time - start_time)  # Time taken for one run
                
                # Calculate space complexity: roughly O(n) space due to copy
                total_space += len(arr_copy)  # We assume space complexity is proportional to array size

            # Calculate average comparisons, swaps, time, and space
            avg_comparisons = total_comparisons / nbr_experiments
            avg_swaps = total_swaps / nbr_experiments
            avg_time = total_time / nbr_experiments
            avg_space = total_space / nbr_experiments

            # Store results with the new columns
            results.append({
                "id_test": f"{func.__name__}",  # Unique test identifier
                "type": arr_type,
                "function_name": func.__name__,
                "array_length": length,
                "comparison": avg_comparisons,
                "time": avg_time,  # Average time per experiment
                "space": avg_space  # Average space per experiment
            })

# Convert results to a DataFrame with the new columns
df = pd.DataFrame(results, columns=['id_test', 'type', 'function_name', 'array_length', 'comparison', 'time', 'space'])

# Save the DataFrame to a CSV file
df.to_csv("benchmark_results.csv", index=False)