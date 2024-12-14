# TP 2: Experimental Study of Simple Sorting Algorithms

import time
import random

# Helper function to generate arrays
def generate_array(size, order="random"):
    if order == "ascending":
        return list(range(size))
    elif order == "descending":
        return list(range(size, 0, -1))
    else:  # random
        return [random.randint(0, 10000) for _ in range(size)]

# Selection Sort
def selection_sort(arr):
    comparisons = 0
    moves = 0
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            moves += 1
    return comparisons, moves

# Bubble Sort
def bubble_sort(arr):
    comparisons = 0
    moves = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                moves += 1
    return comparisons, moves

# Insertion Sort (by exchanges)
def insertion_sort_exchanges(arr):
    comparisons = 0
    moves = 0
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0:
            comparisons += 1
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                moves += 1
            else:
                break
            j -= 1
    return comparisons, moves

# Insertion Sort (by shifting)
def insertion_sort_shifting(arr):
    comparisons = 0
    moves = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                moves += 1
            else:
                break
            j -= 1
        arr[j + 1] = key
        moves += 1  # For the final insertion of key
    return comparisons, moves

# Merge Sort
def merge_sort(arr):
    comparisons = 0
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        left_comparisons = merge_sort(left)
        right_comparisons = merge_sort(right)
        comparisons += left_comparisons + right_comparisons

        i = j = k = 0

        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return comparisons

# Wrapper for merge sort to track execution time and comparisons
def merge_sort_wrapper(arr):
    start_time = time.perf_counter()
    comparisons = merge_sort(arr)
    execution_time = time.perf_counter() - start_time
    return comparisons, 0, execution_time  # No moves for merge sort

# Performance Evaluation
def evaluate_sorting_algorithm(algorithm, arr):
    start_time = time.perf_counter()
    comparisons, moves = algorithm(arr.copy())
    execution_time = time.perf_counter() - start_time
    return comparisons, moves, execution_time

# Main Test Function
def test_sorting_algorithms():
    array_sizes = [1000, 10000, 100000]
    orders = ["random", "ascending", "descending"]
    num_tests = 30
    results = []

    for size in array_sizes:
        for order in orders:
            print(f"Testing size {size}, order: {order}")
            for algorithm in [selection_sort, bubble_sort, insertion_sort_exchanges, insertion_sort_shifting, merge_sort_wrapper]:
                total_comparisons = 0
                total_moves = 0
                total_time = 0

                for _ in range(num_tests):
                    arr = generate_array(size, order)
                    comparisons, moves, exec_time = evaluate_sorting_algorithm(algorithm, arr)
                    total_comparisons += comparisons
                    total_moves += moves
                    total_time += exec_time

                avg_comparisons = total_comparisons / num_tests
                avg_moves = total_moves / num_tests
                avg_time = total_time / num_tests

                results.append({
                    'Algorithm': algorithm.__name__,
                    'Array Size': size,
                    'Order': order,
                    'Average Comparisons': avg_comparisons,
                    'Average Moves': avg_moves,
                    'Average Time (s)': avg_time
                })

    for result in results:
        print(result)

if __name__ == "__main__":
    test_sorting_algorithms()
