import pandas as pd
from tqdm import tqdm
import random
import sys
from pathlib import Path

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

from collections import namedtuple

# Data Generation
factory = DataGeneratorFactory()
factory.register_generator("random", RandomDataGenerator(0, 100))
factory.register_generator("sorted", LinearDataGenerator())

lengths = [10, 100, 1000]
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
    n = len(arr)
    if n <= 1:
        return Metrics(n, 0, 0)

    mid = n // 2
    left = arr[:mid]
    right = arr[mid:]

    metrics_left = merge_sort(left)
    metrics_right = merge_sort(right)
    i = j = k = 0

    comparisons = metrics_left.comparison_count + metrics_right.comparison_count
    move_count = metrics_left.move_count + metrics_right.move_count

    while i < len(left) and j < len(right):
        comparisons += 1
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
        move_count += 1

    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1
        move_count += 1

    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1
        move_count += 1

    return Metrics(n, comparisons, move_count)

funcs = [
    selection_sort,
    merge_sort
]

profiler = TimeAndSpaceProfiler()
results = []

total_iterations = len(funcs) * len(lengths) * nbr_experiments * 3
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
                    logs = profiler.profile(func, data)
                    logs.update({
                        "algorithm": func.__name__,
                        "data_type": label,
                        "size": size,
                        "experiment": experiment_idx + 1,
                    })
                    results.append(logs)

                    pbar.set_postfix({
                        'algorithm': func.__name__,
                        'data_type': label,
                        'size': size,
                        'experiment': experiment_idx + 1,
                    })
                    pbar.update(1)

df = pd.DataFrame(results)

csv_filename = "benchmark_extended_results.csv"
df.to_csv(csv_filename, index=False)

df['time'] = pd.to_numeric(df['time'], errors='coerce')
df['memory'] = pd.to_numeric(df['memory'], errors='coerce')

grouped = df.groupby(['algorithm', 'data_type', 'size']).agg({
    'time': 'mean',
    'memory': 'mean',
    'comparison_count': 'mean',
    'move_count': 'mean'
}).reset_index()

df.to_csv('sort_extended_results_raw.csv', index=False)
grouped.to_csv('sort_extended_results_grouped.csv', index=False)

print("\nResults have been saved to 'sort_extended_results_raw.csv' and 'sort_extended_results_grouped.csv'")
