# الطالبة شلبي جهينة 
import pandas as pd
from tqdm import tqdm
import sys
from pathlib import Path
from collections import namedtuple

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from complexity import (
    StringGenerator,
    TimeAndSpaceProfiler,
)

# Define a Result namedtuple for storing LCS results
LCSResult = namedtuple('LCSResult', ['length', 'comparison_count'])

# Initialize string generator for random data (e.g., using DNA alphabet)
string_generator = StringGenerator(alphabet=['A', 'C', 'G', 'T'])

# Experiment parameters
string_lengths = [3, 5, 7]
num_experiments = 3

# Named tuple for storing performance metrics
Metrics = namedtuple('Metrics', ['size', 'comparison_count', 'move_count'])

# LCS Algorithms to benchmark
def lcs_recursive_algorithm(str1, str2, m, n, comparisons=0):
    if m == 0 or n == 0:
        return LCSResult(0, comparisons)
    if str1[m - 1] == str2[n - 1]:
        result = lcs_recursive_algorithm(str1, str2, m - 1, n - 1, comparisons)
        return LCSResult(result.length + 1, result.comparison_count)
    else:
        result1 = lcs_recursive_algorithm(str1, str2, m - 1, n, comparisons + 1)
        result2 = lcs_recursive_algorithm(str1, str2, m, n - 1, comparisons + 1)
        return LCSResult(max(result1.length, result2.length), result1.comparison_count + result2.comparison_count)

def lcs_with_memoization(str1, str2, m, n, memo, comparisons=0):
    if m == 0 or n == 0:
        return LCSResult(0, comparisons)
    if memo[m][n] != -1:
        return LCSResult(memo[m][n], comparisons)
    if str1[m - 1] == str2[n - 1]:
        result = lcs_with_memoization(str1, str2, m - 1, n - 1, memo, comparisons)
        memo[m][n] = result.length + 1
        return LCSResult(memo[m][n], result.comparison_count)
    else:
        result1 = lcs_with_memoization(str1, str2, m - 1, n, memo, comparisons + 1)
        result2 = lcs_with_memoization(str1, str2, m, n - 1, memo, comparisons + 1)
        memo[m][n] = max(result1.length, result2.length)
        return LCSResult(memo[m][n], result1.comparison_count + result2.comparison_count)

def lcs_with_dp(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    comparisons = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            comparisons += 1
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return LCSResult(dp[m][n], comparisons)

# List of LCS algorithms to benchmark
lcs_algorithms = [
    lcs_recursive_algorithm,
    lcs_with_memoization,
    lcs_with_dp,
]

# Set up the profiler
profiler = TimeAndSpaceProfiler()
benchmark_results = []

# Total number of experiments
total_experiments = len(lcs_algorithms) * len(string_lengths) * num_experiments

# Progress bar setup for tracking the experiments
with tqdm(total=total_experiments, desc="Running benchmarks", unit="experiment") as progress_bar:
    for algorithm in lcs_algorithms:
        for length in string_lengths:
            for experiment in range(num_experiments):
                data = string_generator.generate(length)
                m, n = len(data), len(data)

                # Handle different algorithms and memoization
                if algorithm == lcs_with_memoization:
                    memo_table = [[-1] * (n + 1) for _ in range(m + 1)]
                    logs = profiler.profile(algorithm, data, data, m, n, memo_table)
                elif algorithm == lcs_with_dp:
                    logs = profiler.profile(algorithm, data, data)
                else:
                    logs = profiler.profile(algorithm, data, data, m, n)

                # Update logs with relevant experiment info
                logs.update({
                    "algorithm": algorithm.__name__,
                    "data_type": "random",
                    "size": length,
                    "experiment": experiment + 1,
                })
                benchmark_results.append(logs)
                progress_bar.set_postfix({
                    'algorithm': algorithm.__name__,
                    'size': length,
                    'experiment': experiment + 1,
                })
                progress_bar.update(1)

# Convert results to pandas DataFrame for easier analysis
df_results = pd.DataFrame(benchmark_results)

# Save the raw results to a CSV file
raw_results_filename = "raw_benchmark_results.csv"
df_results.to_csv(raw_results_filename, index=False)

# Preprocess the data: Convert time and memory columns to numeric values
df_results['time'] = pd.to_numeric(df_results['time'], errors='coerce')
df_results['memory'] = pd.to_numeric(df_results['memory'], errors='coerce')

# Group the data by algorithm, data type, and size, then calculate average metrics
grouped_results = df_results.groupby(['algorithm', 'data_type', 'size']).agg({
    'time': 'mean',
    'memory': 'mean',
    'comparison_count': 'mean',
}).reset_index()

# Save the grouped results for summary analysis
grouped_results_filename = 'grouped_benchmark_results.csv'
grouped_results.to_csv(grouped_results_filename, index=False)

# Final confirmation
print("\nBenchmark results have been saved to 'raw_benchmark_results.csv' and 'grouped_benchmark_results.csv'.")
