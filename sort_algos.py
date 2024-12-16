import pandas as pd
import numpy as np
from tqdm import tqdm
import time

lengths = [10, 100, 1000, 10000]

# Number of experiments per size
# currently set to 10, but i test it in just 1 one example hahaha...
nbr_experiments = 10

# Datasets for benchmarking: Random, Sorted, and Inverse Sorted arrays
datasets = {
    "Random": [np.random.randint(0, 10000, size) for size in lengths for _ in range(nbr_experiments)],
    "Sorted": [list(range(size)) for size in lengths for _ in range(nbr_experiments)],
    "Inverse Sorted": [list(range(size, 0, -1)) for size in lengths for _ in range(nbr_experiments)],
}

def selection_sort(arr: list[int]) -> tuple[int, int]:
    """
    Performs the Selection Sort algorithm on a given list.
    
    Arguments:
    arr : list[int] : The list of integers to be sorted.

    Returns:
    tuple[int, int] : A tuple containing the number of comparisons and swaps made during the sorting process.
    """
    comparisons = 0
    swaps = 0

    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        comparisons += 1
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]  # Swap the elements
            swaps += 1

    return comparisons, swaps


def bubble_sort(arr: list[int]) -> tuple[int, int]:
    """
    Performs the Bubble Sort algorithm on a given list.

    Arguments:
    arr : list[int] : The list of integers to be sorted.

    Returns:
    tuple[int, int] : A tuple containing the number of comparisons and swaps made during the sorting process.
    """
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


def insertion_sort_shifting(arr: list[int]) -> tuple[int, int]:
    """
    Performs the Insertion Sort (Shifting) algorithm on a given list.
    
    Arguments:
    arr : list[int] : The list of integers to be sorted.

    Returns:
    tuple[int, int] : A tuple containing the number of comparisons and shifts made during the sorting process.
    """
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

def insertion_sort_exchange(arr: list[int]) -> tuple[int, int]:
    """
    Performs the Insertion Sort (Exchange) algorithm on a given list.
    
    Arguments:
    arr : list[int] : The list of integers to be sorted.

    Returns:
    tuple[int, int] : A tuple containing the number of comparisons and swaps made during the sorting process.
    """
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

# List of sorting algorithms to benchmark
funcs = [selection_sort, bubble_sort, insertion_sort_shifting, insertion_sort_exchange]

# Calculate the total number of benchmarking steps
total_steps = len(funcs) * len(datasets) * len(lengths)
progress_bar = tqdm(total=total_steps, desc="Benchmarking Progress", unit="task")  # Progress bar setup
results = []

# Print header in the temrinal
print(f"Algorithm,Dataset,Size,Avg Comparisons,Avg Swaps/Moves,Avg Time (s)")

# Benchmarking process: For each algorithm, dataset, and array size
for func in funcs:
    for dataset_name, dataset in datasets.items():
        for length_idx, size in enumerate(lengths):
            comparisons_total, swaps_total, time_total = 0, 0, 0

            for experiment in range(nbr_experiments):
                arr = dataset[length_idx * nbr_experiments + experiment]
                start_time = time.time()  
                try:
                    comparisons, swaps = func(arr.copy())  # Copy the array to avoid in-place sorting interference
                except Exception as e:
                    print(f"Error during benchmarking {func.__name__} on {dataset_name} with size {size}: {e}")
                    continue
                time_total += time.time() - start_time 

                comparisons_total += comparisons
                swaps_total += swaps

            # Calculate averages for comparisons, swaps and time
            averages = {k: v / nbr_experiments for k, v in
                        {"comparisons": comparisons_total, "swaps": swaps_total, "time": time_total}.items()}
            results.append({
                "Algorithm": func.__name__,
                "Dataset": dataset_name,
                "Size": size,
                "Avg Comparisons": averages["comparisons"],
                "Avg Swaps/Moves": averages["swaps"],
                "Avg Time (s)": averages["time"],
            })            
            # Log the results
            print(f"{func.__name__},{dataset_name},{size},{averages['comparisons']:.1f},{averages['swaps']:.1f},{averages['time']:.6f}")

            # update thet bar
            progress_bar.update(1)
            
progress_bar.close()

# Create a pandas DataFrame from the results
df = pd.DataFrame(results)

# print(df) # uncomment this line to print the df, for me it useless because it's already logged on the termial 

# triyin to save the benchamrk result in a CSV file
try:
    df.to_csv("benchmark_results.csv", index=False)
except Exception as e:
    print(f"Error saving results: {e}")