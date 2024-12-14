#TODO: put the code here
import pandas as pd
from tqdm import tqdm

import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from complexity import (
    StringGenerator,
    TimeAndSpaceProfiler,
    ComplexityAnalyzer,
    ComplexityVisualizer,
    ComplexityDashboardVisualizer
)
from collections import namedtuple

# Define metrics namedtuple
Metrics = namedtuple('Metrics', ['n', 'comparison_count'])
# Data generation
string_gen = StringGenerator(['A', 'B', 'C', 'D']) 
# Data generation parameters
lengths = [4, 6, 8, 10]
nbr_experiments = 5
# Generate string pairs for each length and experiment
random_string_pairs = [
    [string_gen.Pair_generator(size, size) for _ in range(nbr_experiments)]
    for size in lengths
]
similar_string_pairs = [
    [string_gen.Pair_Similar(size, size, 0.8) for _ in range(nbr_experiments)]
    for size in lengths
]

#Lcs functions 

#LCS Recursive 
def lcs_recursive(X, Y):
    comparison_count = 0
    def helper(i, j):
        nonlocal comparison_count
        if i == 0 or j == 0:
            return 0
        comparison_count += 1
        if X[i - 1] == Y[j - 1]:
            return 1 + helper(i - 1, j - 1)
        comparison_count += 1
        return max(helper(i - 1, j), helper(i, j - 1))
    result = helper(len(X), len(Y))
    return Metrics(result, comparison_count)

#LCS recursive memoization.

def lcs_recursive_memoization(X, Y):
    comparison_count = 0   
    memo = {}
    def helper(i, j):
        nonlocal comparison_count
        if (i, j) in memo:
            return memo[(i, j)]        
        if i == 0 or j == 0:
            return 0
        
        comparison_count += 1
        if X[i - 1] == Y[j - 1]:
            result = 1 + helper(i - 1, j - 1)
        else:
            comparison_count += 1
            result = max(helper(i - 1, j), helper(i, j - 1))
        memo[(i, j)] = result
        return result
    result = helper(len(X), len(Y))
    return Metrics(result, comparison_count)

#LCS Dynamic 
def lcs_Dynamic(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    comparison_count = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            comparison_count += 1
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return Metrics(dp[m][n], comparison_count)

# Algorithms to benchmark
LCS_algorithms = [
    lcs_recursive,
    lcs_recursive_memoization,
    lcs_Dynamic
]

# Initialize profiler
profiler = TimeAndSpaceProfiler()

# Results storage
results = []
# Run experiments
total_experiments = len(lengths) * nbr_experiments * len(LCS_algorithms)
print(f"\nRunning {total_experiments} LCS algorithm experiments...")
# Benchmarking setup
profiler = TimeAndSpaceProfiler()
results = []

# Create a tqdm progress bar for tracking the experiments
with tqdm(total=total_experiments, desc="Benchmarking", unit="experiment") as pbar:
    for func in LCS_algorithms:
        for size, random_experiments, similar_experiments in zip(lengths, random_string_pairs, similar_string_pairs):
            for experiment_idx in range(nbr_experiments):
                for data, label in [
                   (random_experiments[experiment_idx], "random"),
                   (similar_experiments[experiment_idx], "almost_similar"),
                ]:
                # Run and profile
                 X, Y = data
                 logs = profiler.profile(func, X, Y)
                 logs.update({
                 "algorithm": func.__name__,
                 "data_type": label,
                 "size": size,
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

df = pd.DataFrame(results)
df = df[['algorithm', 'data_type', 'size', 'comparison_count', 'time', 'memory']]
# Write the DataFrame to a CSV file
csv_filename = "lcs_benchmark_results.csv"
df.to_csv(csv_filename, index=False)
# Data Preprocessing: Convert time and memory columns to numeric
df['time'] = pd.to_numeric(df['time'], errors='coerce')
df['memory'] = pd.to_numeric(df['memory'], errors='coerce')
# Grouping by algorithm, data_type, and size
grouped = df.groupby(['algorithm', 'data_type', 'size']).agg({
    'time': 'mean',
    'memory': 'mean',
    'comparison_count': 'mean',
}).reset_index()
# Save both raw and grouped results for later analysis
df.to_csv('lcs_results_raw.csv', index=False)
grouped.to_csv('lcs_results_grouped.csv', index=False)

print("\nResults have been saved to 'lcs_results_raw.csv' and 'lcs_results_grouped.csv'")
