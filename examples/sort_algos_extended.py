import pandas as pd 
from tqdm import tqdm 
import sys 
from pathlib import Path 
from collections import namedtuple 
 
# Add parent directory to path 
sys.path.append(str(Path(__file__).parent.parent)) 
 
from complexity import ( 
    DataGeneratorFactory, 
    RandomDataGenerator, 
    LinearDataGenerator, 
    TimeAndSpaceProfiler, 
    ComplexityAnalyzer, 
    ComplexityVisualizer, 
    ComplexityDashboardVisualizer 
) 
 
# Set up data generators 
factory = DataGeneratorFactory() 
factory.register_generator("random", RandomDataGenerator(0, 100)) 
factory.register_generator("sorted", LinearDataGenerator()) 
 
# Data generation 
lengths = [10, 100, 1000]  # You can add more lengths if needed 
nbr_experiments = 3 
 
# Generate arrays for each length and experiment 
random_arrays = [ 
    [factory.get_generator("random").generate(size) for _ in range(nbr_experiments)] 
    for size in lengths 
] 
 
sorted_arrays = [ 
    [factory.get_generator("sorted").generate(size) for _ in range(nbr_experiments)] 
    for size in lengths 
] 
 
inverse_sorted_arrays = [ 
    [list(reversed(factory.get_generator("sorted").generate(size))) for _ in range(nbr_experiments)] 
    for size in lengths 
] 
 
# Metrics class to store results (n, comparison_count, move_count) 
Metrics = namedtuple('Metrics', ['n', 'comparison_count', 'move_count']) 
 
def selection_sort(arr): 
    comparisons = 0 
    move_count = 0 
    n = len(arr) 
 
    for i in range(len(arr)): 
        min_index = i 
        for j in range(i + 1, len(arr)): 
            comparisons += 1 
            if arr[j] < arr[min_index]: 
                min_index = j 
        if min_index != i: 
            arr[i], arr[min_index] = arr[min_index], arr[i] 
            move_count += 1 
 
    return Metrics(n, comparisons, move_count) 
 
def merge_sort(arr): 
    comparisons = 0 
    move_count = 0 
 
    def merge(left, right): 
        nonlocal comparisons, move_count 
        merged = [] 
        i, j = 0, 0 
 
        # Merge two sorted arrays 
        while i < len(left) and j < len(right): 
            comparisons += 1 
            if left[i] <= right[j]: 
                merged.append(left[i]) 
                i += 1 
            else: 
                merged.append(right[j]) 
                j += 1 
            move_count += 1 
 
        # Append remaining elements 
        merged.extend(left[i:]) 
        merged.extend(right[j:]) 
        move_count += len(left[i:]) + len(right[j:]) 
 
        return merged 
 
    def sort(arr): 
        if len(arr) <= 1: 
            return arr 
        mid = len(arr) // 2 
        left = sort(arr[:mid]) 
        right = sort(arr[mid:]) 
        return merge(left, right) 
 
    sorted_arr = sort(arr[:])  # Make a copy to avoid modifying the input 
    return Metrics(len(arr), comparisons, move_count) 
 
# Algorithms to benchmark 
funcs = [ 
    selection_sort, 
    merge_sort 
] 
 
# Benchmarking 
profiler = TimeAndSpaceProfiler() 
results = [] 
 
# Create a tqdm progress bar for tracking the experiments 
total_iterations = len(funcs) * len(lengths) * nbr_experiments * 3  # 3 for random, sorted, inverse_sorted 
with tqdm(total=total_iterations, desc="Benchmarking", unit="experiment") as pbar: 
 
    for func in funcs: 
        for size, random_experiments, sorted_experiments, inverse_sorted_experiments in zip( 
            lengths, random_arrays, sorted_arrays, inverse_sorted_arrays 
        ): 
            for experiment_idx in range(nbr_experiments): 
                for data, label in [ 
                    (random_experiments[experiment_idx], "random"), 
                    (sorted_experiments[experiment_idx], "sorted"), 
                    (inverse_sorted_experiments[experiment_idx], "inverse_sorted"), 
                ]: 
                    # Run and profile 
                    logs = profiler.profile(func, data) 
                    logs.update({ 
                        "algorithm": func.__name__, 
                        "data_type": label, 
                        "size": size, 
                        "experiment":
experiment_idx + 1, 
                    }) 
                    results.append(logs) 
 
                    # Update tqdm progress bar with custom message 
                    pbar.set_postfix({ 
                        'algorithm': func.__name__, 
                        'data_type': label, 
                        'size': size, 
                        'experiment': experiment_idx + 1, 
                    }) 
                    pbar.update(1) 
