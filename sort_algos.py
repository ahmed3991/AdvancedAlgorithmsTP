import time
import random

## TODO: Data Generation

def generate_data(size):
    """Generate random data of the given size."""
    return [random.randint(1, 1000) for _ in range(size)]

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

    return arr, comparison_count, move_count


def bubble_sort(arr):  
    comparison_count = 0
    move_count = 0
    arr = arr.copy()

    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparison_count += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                move_count += 1
                swapped = True
        if not swapped:
            break

    return arr, comparison_count, move_count


def insertion_sort_by_shifting(arr):
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
        move_count += 1

    return arr, comparison_count, move_count


def insertion_sort_by_exchanges(arr):
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

    return arr, comparison_count, move_count

## TODO: make Benchmarks

def benchmark_sorting_algorithm(sort_func, data):
    start_time = time.time()
    sorted_data, comparison_count, move_count = sort_func(data)
    end_time = time.time()
    execution_time = end_time - start_time

    return sorted_data, comparison_count, move_count, execution_time

# Test benchmark with data of different sizes
data_sizes = [100, 1000, 5000]

for size in data_sizes:
    data = generate_data(size)
    print(f"\nBenchmarking for data size: {size}")

    # Test Selection Sort
    print("Selection Sort:")
    sorted_data, comparison_count, move_count, execution_time = benchmark_sorting_algorithm(selection_sort, data)
    print(f"Execution time: {execution_time:.6f}s | Comparisons: {comparison_count} | Moves: {move_count}")

    # Test Bubble Sort
    print("Bubble Sort:")
    sorted_data, comparison_count, move_count, execution_time = benchmark_sorting_algorithm(bubble_sort, data)
    print(f"Execution time: {execution_time:.6f}s | Comparisons: {comparison_count} | Moves: {move_count}")

    # Test Insertion Sort by Shifting
    print("Insertion Sort (Shifting):")
    sorted_data, comparison_count, move_count, execution_time = benchmark_sorting_algorithm(insertion_sort_by_shifting, data)
    print(f"Execution time: {execution_time:.6f}s | Comparisons: {comparison_count} | Moves: {move_count}")

    # Test Insertion Sort by Exchanges
    print("Insertion Sort (Exchanges):")
    sorted_data, comparison_count, move_count, execution_time = benchmark_sorting_algorithm(insertion_sort_by_exchanges, data)
    print(f"Execution time: {execution_time:.6f}s | Comparisons: {comparison_count} | Moves: {move_count}")

print('hello')
