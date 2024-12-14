from abc import ABC, abstractmethod
from typing import Any
import random
import networkx as nx
import time
import sys

# Helper function to generate sorted arrays
def generate_sorted_array(size):
    return sorted(random.uniform(0, 10000) for _ in range(size))

# Simple Sequential Search
def simple_sequential_search(arr, target):
    comparisons = 0
    for item in arr:
        comparisons += 1
        if item == target:
            return comparisons, True
    return comparisons, False

# Optimized Sequential Search
def optimized_sequential_search(arr, target):
    comparisons = 0
    for item in arr:
        comparisons += 1
        if item == target:
            return comparisons, True
        if item > target:
            break
    return comparisons, False

# Iterative Binary Search
def iterative_binary_search(arr, target):
    comparisons = 0
    low, high = 0, len(arr) - 1
    while low <= high:
        comparisons += 1
        mid = (low + high) // 2
        if arr[mid] == target:
            return comparisons, True
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return comparisons, False

# Recursive Binary Search
def recursive_binary_search(arr, target, low, high, comparisons=0):
    if low > high:
        return comparisons, False
    comparisons += 1
    mid = (low + high) // 2
    if arr[mid] == target:
        return comparisons, True
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, high, comparisons)
    else:
        return recursive_binary_search(arr, target, low, mid - 1, comparisons)

# Performance Evaluation
def evaluate_algorithm(algorithm, arr, target, *args):
    start_time = time.perf_counter()
    if algorithm == recursive_binary_search:
        comparisons, found = algorithm(arr, target, 0, len(arr) - 1, *args)
    else:
        comparisons, found = algorithm(arr, target, *args)
    execution_time = time.perf_counter() - start_time
    return comparisons, execution_time, found

# Main Test Function
def test_search_algorithms():
    array_sizes = [10**3, 10**4, 10**5, 10**6]
    num_tests = 30
    results = []

    for size in array_sizes:
        print(f"Testing with array size: {size}")
        arr = generate_sorted_array(size)
        
        for algorithm in [simple_sequential_search, optimized_sequential_search, 
                          iterative_binary_search, recursive_binary_search]:
            total_comparisons = 0
            total_time = 0
            for _ in range(num_tests):
                target = random.uniform(0, 10000)
                comparisons, exec_time, _ = evaluate_algorithm(algorithm, arr, target)
                total_comparisons += comparisons
                total_time += exec_time

            avg_comparisons = total_comparisons / num_tests
            avg_time = total_time / num_tests
            results.append({
                'Algorithm': algorithm.__name__,
                'Array Size': size,
                'Average Comparisons': avg_comparisons,
                'Average Time (s)': avg_time
            })

    for result in results:
        print(result)

if __name__ == "__main__":
    test_search_algorithms()
