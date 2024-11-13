## TODO: TP should be HERE

import random
import time
import numpy as np
import matplotlib.pyplot as plt
from memory_profiler import memory_usage


## TODO: Data Generation

def generate_sorted_array(size):
    array = sorted(random.uniform(0, 100) for _ in range(size))
    return array
    
array_sizes = [10**3, 10**4, 10**5, 10**6]
arrays = {size: generate_sorted_array(size) for size in array_sizes}

## TODO: Sort Algorithms implementations

# Simple Sequential Search
def simple_sequential_search(arr, target):
    comparisons = 0
    for i, value in enumerate(arr):
        comparisons += 1
        if value == target:
            return i, comparisons
    return -1, comparisons

# Optimized Sequential Search
def optimized_sequential_search(arr, target):
    comparisons = 0
    for i, value in enumerate(arr):
        comparisons += 1
        if value == target:
            return i, comparisons
        elif value > target:
            break
    return -1, comparisons

# Iterative Binary Search
def iterative_binary_search(arr, target):
    left, right = 0, len(arr) - 1
    comparisons = 0
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons

# Recursive Binary Search
def recursive_binary_search(arr, target, left=0, right=None, comparisons=0):
    if right is None:
        right = len(arr) - 1
    if left > right:
        return -1, comparisons
    
    mid = (left + right) // 2
    comparisons += 1
    if arr[mid] == target:
        return mid, comparisons
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, right, comparisons)
    else:
        return recursive_binary_search(arr, target, left, mid - 1, comparisons)

def test_algorithm(algorithm, arr, target):
    start_time = time.time()
    mem_usage = memory_usage((algorithm, (arr, target)), max_usage=True)
    result, comparisons = algorithm(arr, target)
    end_time = time.time()
    
    exec_time = end_time - start_time
    return comparisons, exec_time, mem_usage

def run_tests():
    target = 50.0  
    num_tests = 30
    results = {alg: {size: [] for size in array_sizes} for alg in ["simple", "optimized", "iterative", "recursive"]}
    
    for size, arr in arrays.items():
        for _ in range(num_tests):
            for alg_name, algorithm in [
                ("simple", simple_sequential_search),
                ("optimized", optimized_sequential_search),
                ("iterative", iterative_binary_search),
                ("recursive", recursive_binary_search)
            ]:
                comparisons, exec_time, mem_usage = test_algorithm(algorithm, arr, target)
                results[alg_name][size].append({
                    "comparisons": comparisons,
                    "exec_time": exec_time,
                    "mem_usage": mem_usage
                })
    return results


test_results = run_tests()

def analyze_results(results):
    for alg, data in results.items():
        comparisons, times, memory = [], [], []
        
        for size in array_sizes:
            comp_data = [test["comparisons"] for test in data[size]]
            time_data = [test["exec_time"] for test in data[size]]
            mem_data = [test["mem_usage"] for test in data[size]]
            
            comparisons.append((np.mean(comp_data), np.var(comp_data)))
            times.append((np.mean(time_data), np.var(time_data)))
            memory.append((np.mean(mem_data), np.var(mem_data)))

    
        plt.figure()
        plt.errorbar(array_sizes, [x[0] for x in comparisons], yerr=[x[1] for x in comparisons], fmt='-o')
        plt.title(f"{alg.capitalize()} Search: Comparisons")
        plt.xlabel("Array Size")
        plt.ylabel("Average Comparisons")
        plt.show()

       
        plt.figure()
        plt.errorbar(array_sizes, [x[0] for x in times], yerr=[x[1] for x in times], fmt='-o')
        plt.title(f"{alg.capitalize()} Search: Execution Time")
        plt.xlabel("Array Size")
        plt.ylabel("Average Execution Time (s)")
        plt.show()

        
        plt.figure()
        plt.errorbar(array_sizes, [x[0] for x in memory], yerr=[x[1] for x in memory], fmt='-o')
        plt.title(f"{alg.capitalize()} Search: Memory Usage")
        plt.xlabel("Array Size")
        plt.ylabel("Average Memory Usage (MB)")
        plt.show()


analyze_results(test_results)

## TODO: make Benchmarks

## hey there , i am Oussama Tamma from Group 2 , this is my Tp . 

print('hello')
