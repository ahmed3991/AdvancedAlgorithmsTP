from memory_profiler import memory_usage
import time
import numpy as np
from complexity import time_and_space_profiler, get_complexity
from tabulate import tabulate

# Section: Data Generation
def generate_random_data(size, low=1, high=100):
    """Generates random integer data within a specified range.

    Args:
        size (int): Number of elements to generate.
        low (int): Minimum value of elements (inclusive).
        high (int): Maximum value of elements (exclusive).

    Returns:
        np.array: Array of random integers.
    """
    return np.random.randint(low, high, size)

def bubble_sort(arr):
    """Sorts an array using the bubble sort algorithm.

    Args:
        arr (list): Unsorted list of elements.

    Returns:
        list: Sorted list of elements.
    """
    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def insertion_sort(arr):
    """Sorts an array using the insertion sort algorithm.

    Args:
        arr (list): Unsorted list of elements.

    Returns:
        list: Sorted list of elements.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def selection_sort(arr):
    """Sorts an array using the selection sort algorithm.

    Args:
        arr (list): Unsorted list of elements.

    Returns:
        list: Sorted list of elements.
    """
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

# Function to benchmark algorithms on multiple input sizes
def benchmark_algorithm(algorithm, sizes):
    times, memories = [], []
    for size in sizes:
        test_data = generate_random_data(size)
        name, result, exec_time, mem_usage = time_and_space_profiler(algorithm)(test_data)
        times.append(exec_time)
        memories.append(mem_usage)

    time_complexity = get_complexity(np.array(sizes), np.array(times))
    memory_complexity = get_complexity(np.array(sizes), np.array(memories))

    return {
        "Algorithm": algorithm.__name__,
        "Time Complexity": time_complexity,
        "Memory Complexity": memory_complexity,
        "Avg Execution Time (s)": f"{np.mean(times):.4f}",
        "Avg Memory Usage (MiB)": f"{np.mean(memories):.4f}"
    }

# Section: Running Benchmarks and Displaying Results
if __name__ == "__main__":
    input_sizes = [100, 500, 5000, 10000]
    algorithms = [bubble_sort, insertion_sort, selection_sort]

    results = [benchmark_algorithm(algo, input_sizes) for algo in algorithms]
    headers = ["Algorithm", "Time Complexity", "Memory Complexity", "Avg Execution Time (s)", "Avg Memory Usage (MiB)"]

    print(tabulate(results, headers="keys", tablefmt="grid"))
