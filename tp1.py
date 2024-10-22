import numpy as np
import time
from memory_profiler import memory_usage

def generate_sorted_array(size):
    return np.sort(np.random.uniform(low=0.0, high=100.0, size=size))

sizes = [10**3, 10**4, 10**5, 10**6]
arrays = [generate_sorted_array(size) for size in sizes]

def simple_sequential_search(arr, target):
    comparisons = 0
    for item in arr:
        comparisons += 1
        if item == target:
            return True, comparisons
    return False, comparisons

def optimized_sequential_search(arr, target):
    comparisons = 0
    for item in arr:
        comparisons += 1
        if item == target:
            return True, comparisons
        elif item > target:
            return False, comparisons
    return False, comparisons

def iterative_binary_search(arr, target):
    comparisons = 0
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        comparisons += 1
        if arr[mid] == target:
            return True, comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return False, comparisons

def recursive_binary_search(arr, target, left, right, comparisons=0):
    if left > right:
        return False, comparisons
    
    mid = left + (right - left) // 2
    comparisons += 1
    
    if arr[mid] == target:
        return True, comparisons
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, right, comparisons)
    else:
        return recursive_binary_search(arr, target, left, mid - 1, comparisons)

def measure_execution_time(search_func, *args):
    start_time = time.time()
    result, comparisons = search_func(*args)
    end_time = time.time()
    exec_time = (end_time - start_time) * 1000  
    return result, comparisons, round(exec_time, 2)  

def measure_memory_usage(search_func, *args):
    mem_usage = memory_usage((search_func, args), max_usage=True)
    return round(mem_usage, 2)

if __name__ == '__main__':
    target_value = np.random.choice(arrays[0]) 

    print("Simple Sequential Search:")
    result, comparisons, exec_time = measure_execution_time(simple_sequential_search, arrays[0], target_value)
    mem_usage = measure_memory_usage(simple_sequential_search, arrays[0], target_value)
    print(f"Result: {result}, Comparisons: {comparisons}, Execution Time: {exec_time} ms, Memory Usage: {mem_usage} MB")

    print("\nOptimized Sequential Search:")
    result, comparisons, exec_time = measure_execution_time(optimized_sequential_search, arrays[0], target_value)
    mem_usage = measure_memory_usage(optimized_sequential_search, arrays[0], target_value)
    print(f"Result: {result}, Comparisons: {comparisons}, Execution Time: {exec_time} ms, Memory Usage: {mem_usage} MB")

    print("\nIterative Binary Search:")
    result, comparisons, exec_time = measure_execution_time(iterative_binary_search, arrays[0], target_value)
    mem_usage = measure_memory_usage(iterative_binary_search, arrays[0], target_value)
    print(f"Result: {result}, Comparisons: {comparisons}, Execution Time: {exec_time} ms, Memory Usage: {mem_usage} MB")

    print("\nRecursive Binary Search:")
    result, comparisons, exec_time = measure_execution_time(recursive_binary_search, arrays[0], target_value, 0, len(arrays[0])-1)
    mem_usage = measure_memory_usage(recursive_binary_search, arrays[0], target_value, 0, len(arrays[0])-1)
    print(f"Result: {result}, Comparisons: {comparisons}, Execution Time: {exec_time} ms, Memory Usage: {mem_usage} MB")
