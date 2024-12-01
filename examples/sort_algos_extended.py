import pandas as pd
from tqdm import tqdm
import sys
from pathlib import Path

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

factory = DataGeneratorFactory()
factory.register_generator("random", RandomDataGenerator(0, 100))
factory.register_generator("sorted", LinearDataGenerator())

lengths = [10, 100, 1000]
nbr_experiments = 3

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
    comparisons = 0
    move_count = 0

    def merge(left, right):
        nonlocal comparisons, move_count
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            comparisons += 1
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
                move_count += 1

        merged.extend(left[i:])
        merged.extend(right[j:])
        move_count += len(left[i:]) + len(right[j:])
        return merged

    def divide_and_merge(arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = divide_and_merge(arr[:mid])
        right = divide_and_merge(arr[mid:])
        return merge(left, right)

    sorted_arr = divide_and_merge(arr)
    return Metrics(len(arr), comparisons, move_count)

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
