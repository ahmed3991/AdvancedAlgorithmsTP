import numpy as np
import time
import csv

# Array lengths
lenghts = [10, 100, 1000]

# Number of experiments per array type
nbr_experiments = 3

# Sorting algorithms
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
            arr[j + 1] = arr[j]
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
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            swaps += 1
            j -= 1
        if j > 0:
            comparisons += 1
    return comparisons, swaps

funcs = [selection_sort, bubble_sort, insertion_sort_shifting, insertion_sort_exchange]

# Generate arrays
random_arrays = [np.random.randint(0, 1000, size=l).tolist() for l in lenghts]
sorted_arrays = [list(range(l)) for l in lenghts]
inverse_sorted_arrays = [list(range(l, 0, -1)) for l in lenghts]

# Initialize results
results = []

# Benchmark the algorithms
for func in funcs:
    for l, random_arr, sorted_arr, inverse_sorted_arr in zip(lenghts, random_arrays, sorted_arrays, inverse_sorted_arrays):
        for _ in range(nbr_experiments):
            # Random array
            start_time = time.time()
            rand_comp, rand_moves = func(random_arr.copy())
            elapsed_time = time.time() - start_time
            results.append({
                'Function': func.__name__,
                'Array Type': 'Random',
                'Length': l,
                'Comparisons': rand_comp,
                'Moves': rand_moves,
                'Time (s)': elapsed_time
            })
            
            # Sorted array
            start_time = time.time()
            sorted_comp, sorted_moves = func(sorted_arr.copy())
            elapsed_time = time.time() - start_time
            results.append({
                'Function': func.__name__,
                'Array Type': 'Sorted',
                'Length': l,
                'Comparisons': sorted_comp,
                'Moves': sorted_moves,
                'Time (s)': elapsed_time
            })
            
            # Inverse sorted array
            start_time = time.time()
            inv_comp, inv_moves = func(inverse_sorted_arr.copy())
            elapsed_time = time.time() - start_time
            results.append({
                'Function': func.__name__,
                'Array Type': 'Inverse Sorted',
                'Length': l,
                'Comparisons': inv_comp,
                'Moves': inv_moves,
                'Time (s)': elapsed_time
            })

# Save results to a CSV file
with open('sorting_results.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=results[0].keys())
    writer.writeheader()
    writer.writerows(results)

print("Results saved to sorting_results.csv")
