import numpy as np
import time
import pandas as pd
import matplotlib.pyplot as plt

# Selection Sort
def selection_sort(arr):
    comparisons = [0]
    moves = [0]
    for i in range(len(arr)):
        min_idx = i
        for j in range(i+1, len(arr)):
            comparisons[0] += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        moves[0] += 1
    return comparisons[0], moves[0]

# Bubble Sort
def bubble_sort(arr):
    comparisons = [0]
    moves = [0]
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            comparisons[0] += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                moves[0] += 1
    return comparisons[0], moves[0]

# Insertion Sort (by shifting)
def insertion_sort_shift(arr):
    comparisons = [0]
    moves = [0]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            comparisons[0] += 1
            arr[j + 1] = arr[j]
            moves[0] += 1
            j -= 1
        arr[j + 1] = key
    return comparisons[0], moves[0]

# Merge Sort
def merge_sort(arr):
    comparisons = [0]
    moves = [0]

    def merge(left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparisons[0] += 1
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                moves[0] += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def sort(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = sort(arr[:mid])
        right = sort(arr[mid:])
        return merge(left, right)

    sorted_arr = sort(arr)
    return comparisons[0], moves[0]

# Function to analyze and compare algorithms
def analyze_algorithms():
    results = []
    sizes = [1000, 5000, 10000]

    for size in sizes:
        random_array = np.random.randint(0, 10000, size)
        sorted_array = np.sort(random_array)
        reverse_sorted_array = sorted_array[::-1]

        for algo_name, algo in [("Selection Sort", selection_sort),
                                ("Bubble Sort", bubble_sort),
                                ("Insertion Sort (Shift)", insertion_sort_shift),
                                ("Merge Sort", merge_sort)]:
            for array_type, array in [("Random", random_array),
                                      ("Sorted", sorted_array),
                                      ("Reverse Sorted", reverse_sorted_array)]:
                arr_copy = array.copy()
                start_time = time.perf_counter()
                comparisons, moves = algo(arr_copy)
                end_time = time.perf_counter()
                execution_time = end_time - start_time
                results.append({
                    "Algorithm": algo_name,
                    "Array Type": array_type,
                    "Size": size,
                    "Comparisons": comparisons,
                    "Moves": moves,
                    "Execution Time (s)": execution_time
                })

    # Convert results into DataFrame
    df = pd.DataFrame(results)
    print(df)
    df.to_csv("sorting_algorithms_comparison_results.csv", index=False)

    # Plotting the results
    plot_comparison(df)

# Plotting function for execution time comparison
def plot_comparison(df):
    df_pivot = df.pivot_table(index='Size', columns='Algorithm', values='Execution Time (s)', aggfunc='mean')
    df_pivot.plot(kind='bar', figsize=(10,6))
    plt.title('Comparison of Sorting Algorithms')
    plt.ylabel('Execution Time (seconds)')
    plt.xlabel('Array Size')
    plt.show()

# Run the analysis
if __name__ == "__main__":
    analyze_algorithms()
