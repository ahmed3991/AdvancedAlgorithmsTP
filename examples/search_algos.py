import pandas as pd
from tqdm import tqdm
import numpy as np
import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from complexity.generator import (
    DataGeneratorFactory,
    RandomDataGenerator,
    LinearDataGenerator,
)
from complexity.profiler import TimeAndSpaceProfiler
from complexity.analyser import ComplexityAnalyzer
from complexity.visualizer import ComplexityVisualizer, ComplexityDashboardVisualizer

from collections import namedtuple

# Define metrics namedtuple
Metrics = namedtuple("Metrics", ["n", "comparison_count"])

# Set up data generators
factory = DataGeneratorFactory()
factory.register_generator("random", RandomDataGenerator(0, 1000))
factory.register_generator("sorted", LinearDataGenerator())

# Data generation parameters
lengths = [100, 1000, 10000, 100000]
nbr_experiments = 5

# Generate arrays for each length and experiment
random_arrays = [
    [factory.get_generator("random").generate(size) for _ in range(nbr_experiments)]
    for size in lengths
]

sorted_arrays = [
    [
        sorted(factory.get_generator("random").generate(size))
        for _ in range(nbr_experiments)
    ]
    for size in lengths
]


# Search algorithms implementation
def sequential_search(arr, target):
    comparisons = 0
    n = len(arr)

    for i in range(n):
        comparisons += 1
        if arr[i] == target:
            break

    return Metrics(n, comparisons)


def advanced_sequential_search(arr, target):
    comparisons = 0
    n = len(arr)

    for i in range(n):
        comparisons += 1
        if arr[i] == target:
            break
        # Additional comparison for sorted array optimization
        comparisons += 1
        if arr[i] > target:
            break

    return Metrics(n, comparisons)


def binary_search(arr, target):
    comparisons = 0
    n = len(arr)
    start = 0
    end = n - 1

    while start <= end:
        mid = (start + end) // 2
        comparisons += 1

        if arr[mid] == target:
            break
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
        comparisons += 1

    return Metrics(n, comparisons)


# Algorithms to benchmark
search_algorithms = [sequential_search, advanced_sequential_search, binary_search]

# Initialize profiler
profiler = TimeAndSpaceProfiler()

# Results storage
results = []

# Run experiments
total_experiments = len(lengths) * nbr_experiments * len(search_algorithms)
print(f"\nRunning {total_experiments} search algorithm experiments...")

with tqdm(total=total_experiments, desc="Running experiments") as pbar:
    for length_idx, length in enumerate(lengths):
        for exp in range(nbr_experiments):
            # Get arrays for this experiment
            random_arr = random_arrays[length_idx][exp]
            sorted_arr = sorted_arrays[length_idx][exp]

            # Generate random target (existing in array)
            random_target = random_arr[np.random.randint(0, length)]
            sorted_target = sorted_arr[np.random.randint(0, length)]

            # Test each algorithm
            for algo in search_algorithms:
                algo_name = algo.__name__

                # For sequential and advanced sequential, test with both random and sorted
                if algo == sequential_search:
                    metrics = profiler.profile(algo, random_arr, random_target)
                    results.append(
                        {
                            "algorithm": algo_name,
                            "data_type": "random",
                            "size": length,
                            "experiment": exp,
                            **metrics,
                        }
                    )
                    pbar.update(1)

                # For advanced sequential and binary search, test with sorted array
                if algo in [advanced_sequential_search, binary_search]:
                    metrics = profiler.profile(algo, sorted_arr, sorted_target)
                    results.append(
                        {
                            "algorithm": algo_name,
                            "data_type": "sorted",
                            "size": length,
                            "experiment": exp,
                            **metrics,
                        }
                    )
                    pbar.update(1)

print("\nSaving results...")

# Convert results to DataFrame
df = pd.DataFrame(results)

# Save results
df.to_csv("search_results.csv", index=False)

# Data Preprocessing: Convert time and memory columns to numeric
df["time"] = pd.to_numeric(df["time"], errors="coerce")
df["memory"] = pd.to_numeric(df["memory"], errors="coerce")

# Grouping by algorithm, data_type, and size
grouped = (
    df.groupby(["algorithm", "data_type", "size"])
    .agg({"time": "mean", "memory": "mean", "comparison_count": "mean"})
    .reset_index()
)

# Save both raw and grouped results for later analysis
df.to_csv("search_results_raw.csv", index=False)
grouped.to_csv("search_results_grouped.csv", index=False)

print(
    "\nResults have been saved to 'search_results_raw.csv' and 'search_results_grouped.csv'"
)
