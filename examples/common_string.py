import random
from typing import List, Tuple
import pandas as pd
from tqdm import tqdm
import sys
from pathlib import Path
from collections import namedtuple

# Add parent directory to sys.path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from complexity import (
    TimeAndSpaceProfiler,
    StringGenerator
)

# Define a named tuple for capturing metrics
Metrics = namedtuple('Metrics', ['length', 'comparisons', 'move_count'])

# Recursive approach for LCS
def lcs_recursive(str1: str, str2: str, i: int, j: int, comparisons=0, moves=0) -> Metrics:
    if i == 0 or j == 0:
        return Metrics(0, comparisons, moves)

    if str1[i - 1] == str2[j - 1]:
        return lcs_recursive(str1, str2, i - 1, j - 1, comparisons + 1, moves)
    else:
        result1 = lcs_recursive(str1, str2, i - 1, j, comparisons + 1, moves)
        result2 = lcs_recursive(str1, str2, i, j - 1, comparisons + 1, moves)
        return Metrics(max(result1.length, result2.length), result1.comparisons, result1.move_count)

# Memoized version of LCS
def lcs_memoized(str1: str, str2: str, memo=None, comparisons=0, moves=0) -> Metrics:
    if memo is None:
        memo = {}
    
    if (len(str1), len(str2)) in memo:
        return memo[(len(str1), len(str2))]

    if not str1 or not str2:
        return Metrics(0, comparisons, moves)

    if str1[-1] == str2[-1]:
        result = lcs_memoized(str1[:-1], str2[:-1], memo, comparisons + 1, moves)
        memo[(len(str1), len(str2))] = Metrics(result.length + 1, result.comparisons, result.move_count)
    else:
        res1 = lcs_memoized(str1[:-1], str2, memo, comparisons + 1, moves)
        res2 = lcs_memoized(str1, str2[:-1], memo, comparisons + 1, moves)
        memo[(len(str1), len(str2))] = Metrics(max(res1.length, res2.length), res1.comparisons, res1.move_count)

    return memo[(len(str1), len(str2))]

# Bottom-up dynamic programming approach for LCS
def lcs_bottom_up(str1: str, str2: str) -> Metrics:
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    comparisons, moves = 0, 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            comparisons += 1
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                moves += 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return Metrics(dp[m][n], comparisons, moves)

# Initialize utility classes
string_gen = StringGenerator(['A', 'C', 'G', 'T'])
profiler = TimeAndSpaceProfiler()

# Function to profile LCS algorithms
def profile_lcs(method, *args):
    """Runs the profiling of a given LCS function."""
    return profiler.profile(method, *args)

# Experiment parameters
sizes = [10, 15, 20]
tests_per_size = 3
results_data = []

# Benchmark LCS implementations
with tqdm(total=len(sizes) * tests_per_size * 3, desc="Running LCS Benchmarks", unit="test") as progress:
    for string_size in sizes:
        for test_num in range(tests_per_size):
            # Generate input strings
            str_a = string_gen.generate(string_size)
            str_b = string_gen.generate(string_size)

            # Recursive profiling
            recursive_log = profile_lcs(lcs_recursive, str_a, str_b, len(str_a), len(str_b))
            recursive_log.update({"method": "Recursive", "size": string_size, "test_id": test_num + 1})
            results_data.append(recursive_log)

            # Memoized profiling
            memoized_log = profile_lcs(lcs_memoized, str_a, str_b)
            memoized_log.update({"method": "Memoized", "size": string_size, "test_id": test_num + 1})
            results_data.append(memoized_log)

            # Bottom-up profiling
            bottom_up_log = profile_lcs(lcs_bottom_up, str_a, str_b)
            bottom_up_log.update({"method": "Bottom-Up", "size": string_size, "test_id": test_num + 1})
            results_data.append(bottom_up_log)

            # Update progress
            progress.update(1)

# Save raw results to CSV
results_df = pd.DataFrame(results_data)
results_df.to_csv("lcs_raw_results.csv", index=False)

# Post-process and aggregate results
results_df['time'] = pd.to_numeric(results_df['time'], errors='coerce')
results_df['memory'] = pd.to_numeric(results_df['memory'], errors='coerce')
summary = results_df.groupby(['method', 'size']).agg({
    'time': 'mean',
    'memory': 'mean',
}).reset_index()

# Save aggregated results
summary.to_csv("lcs_summary_results.csv", index=False)

print("Benchmarking complete. Results saved in 'lcs_raw_results.csv' and 'lcs_summary_results.csv'.")
