import random
from typing import List, Tuple
import pandas as pd
from tqdm import tqdm
import sys
from pathlib import Path
from collections import namedtuple

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from complexity import (
    TimeAndSpaceProfiler,
    StringGenerator
)

# LCS functions (Recursive, Memoization, Bottom-up)
Metrics = namedtuple('Metrics', ['lcs_length', 'comparisons', 'move_count'])


def lcs_recursive(x: str, y: str, i: int, j: int, comparisons=0, move_count=0) -> Metrics:
    if i == 0 or j == 0:
        return Metrics(0, comparisons, move_count)

    if x[i - 1] == y[j - 1]:
        return lcs_recursive(x, y, i - 1, j - 1, comparisons + 1, move_count)
    else:
        res1 = lcs_recursive(x, y, i - 1, j, comparisons + 1, move_count)
        res2 = lcs_recursive(x, y, i, j - 1, comparisons + 1, move_count)
        return Metrics(max(res1.lcs_length, res2.lcs_length), res1.comparisons, res1.move_count)


def lcs_memoization(x: str, y: str, memo=None, comparisons=0, move_count=0) -> Metrics:
    if memo is None:
        memo = {}
    if (len(x), len(y)) in memo:
        return memo[(len(x), len(y))]
    if not x or not y:
        return Metrics(0, comparisons, move_count)

    if x[-1] == y[-1]:
        result = lcs_memoization(x[:-1], y[:-1], memo, comparisons + 1, move_count)
        memo[(len(x), len(y))] = Metrics(result.lcs_length + 1, result.comparisons, result.move_count)
    else:
        res1 = lcs_memoization(x[:-1], y, memo, comparisons + 1, move_count)
        res2 = lcs_memoization(x, y[:-1], memo, comparisons + 1, move_count)
        memo[(len(x), len(y))] = Metrics(max(res1.lcs_length, res2.lcs_length), res1.comparisons, res1.move_count)

    return memo[(len(x), len(y))]


def lcs_bottom_up(x: str, y: str) -> Metrics:
    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    comparisons = 0
    move_count = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            comparisons += 1
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                move_count += 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return Metrics(dp[m][n], comparisons, move_count)


# Initialize the StringGenerator and TimeAndSpaceProfiler
gen = StringGenerator(['A', 'C', 'G', 'T'])
profiler = TimeAndSpaceProfiler()


# Benchmarking function for LCS
def benchmark_lcs(func, *args):
    """
    Function to benchmark the LCS algorithms.
    Takes any number of arguments and passes them to the function.
    """
    logs = profiler.profile(func, *args)  # Use *args to pass all arguments correctly
    return logs


# Testing and profiling LCS functions
lengths = [10, 15, 20]
nbr_experiments = 3
results = []

# Set up the progress bar
total_iterations = len(lengths) * nbr_experiments * 3  # for random, sorted, inverse_sorted
with tqdm(total=total_iterations, desc="Benchmarking LCS", unit="experiment") as pbar:
    for size in lengths:
        for experiment_idx in range(nbr_experiments):
            # Generate strings for LCS
            X = gen.generate(size)
            Y = gen.generate(size)

            # Profile Recursive LCS
            logs = benchmark_lcs(lcs_recursive, X, Y, len(X), len(Y))
            logs.update({"algorithm": "lcs_recursive", "size": size, "experiment": experiment_idx + 1})
            results.append(logs)

            # Profile Memoization LCS
            logs = benchmark_lcs(lcs_memoization, X, Y)
            logs.update({"algorithm": "lcs_memoization", "size": size, "experiment": experiment_idx + 1})
            results.append(logs)

            # Profile Bottom-up LCS
            logs = benchmark_lcs(lcs_bottom_up, X, Y)
            logs.update({"algorithm": "lcs_bottom_up", "size": size, "experiment": experiment_idx + 1})
            results.append(logs)

            # Update progress bar
            pbar.set_postfix({"size": size, "experiment": experiment_idx + 1})
            pbar.update(1)

# Convert results to a DataFrame
df = pd.DataFrame(results)
df.to_csv("lcs_benchmark_results.csv", index=False)

# Data Preprocessing
df['time'] = pd.to_numeric(df['time'], errors='coerce')
df['memory'] = pd.to_numeric(df['memory'], errors='coerce')

# Grouping results by algorithm, size, and experiment
grouped = df.groupby(['algorithm', 'size']).agg({
    'time': 'mean',
    'memory': 'mean',
}).reset_index()

grouped.to_csv('lcs_results_grouped.csv', index=False)

print("Results have been saved to 'lcs_benchmark_results.csv' and 'lcs_results_grouped.csv'")
