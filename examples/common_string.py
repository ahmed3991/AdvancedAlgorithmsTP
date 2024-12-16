#TODO: put the code here
import pandas as pd
from tqdm import tqdm
import sys
from pathlib import Path
from collections import namedtuple
import time

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from complexity import (
    DataGeneratorFactory,
    StringGenerator,
    TimeAndSpaceProfiler,
    ComplexityAnalyzer,
    ComplexityVisualizer,
    ComplexityDashboardVisualizer
)

# Define Metrics named tuple to store only time and memory
Metrics = namedtuple("Metrics", ["n", "time", "memory"])

# Setup Data Generator
factory = DataGeneratorFactory()
factory.register_generator("string", StringGenerator(['A', 'B', 'C']))

# Define string lengths and number of experiments
lengths = [10, 50, 100]
nbr_experiments = 3

# Generate string pairs for testing algorithms
string_pairs = [
    [
        factory.get_generator("string").generate_pair(size, size)
        for _ in range(nbr_experiments)
    ]
    for size in lengths
]

# Define LCS algorithms

# LCS algorithm (without memory)
def lcs_recursive(X, Y):
    if not X or not Y:
        return 0
    if X[-1] == Y[-1]:
        # If the last characters are equal, move to the rest
        return 1 + lcs_recursive(X[:-1], Y[:-1])
    else:
        # Call the function recursively for the two options
        return max(lcs_recursive(X[:-1], Y), lcs_recursive(X, Y[:-1]))

# LCS algorithm using memoization (memory)
def lcs_memoization(X, Y, memo=None):
    if memo is None:
        memo = {}
    if not X or not Y:
        return 0
    if (X, Y) in memo:
        return memo[(X, Y)]
    if X[-1] == Y[-1]:
        memo[(X, Y)] = 1 + lcs_memoization(X[:-1], Y[:-1], memo)
    else:
        memo[(X, Y)] = max(
            lcs_memoization(X[:-1], Y, memo), lcs_memoization(X, Y[:-1], memo)
        )
    return memo[(X, Y)]

# LCS algorithm using dynamic programming (bottom-up approach)
def lcs_dynamic(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

# Setup profiler
profiler = TimeAndSpaceProfiler()

# Setup ComplexityAnalyzer and Visualizers
analyzer = ComplexityAnalyzer()
visualizer = ComplexityVisualizer()
dashboard_visualizer = ComplexityDashboardVisualizer()

# List of algorithms for testing
funcs = [
    ("Recursive", lcs_recursive),
    ("Memoization", lcs_memoization),
    ("Dynamic Programming", lcs_dynamic),
]

results = []

# Create progress bar using tqdm
total_iterations = len(funcs) * len(lengths) * nbr_experiments
with tqdm(total=total_iterations, desc="Benchmarking", unit="experiment") as pbar:
    for func_name, func in funcs:
        for size, experiments in zip(lengths, string_pairs):
            for experiment_idx, (X, Y) in enumerate(experiments):
                # Use TimeAndSpaceProfiler to measure time and memory
                logs = profiler.profile(func, X, Y)
                logs.update({
                    "algorithm": func_name,
                    "size": size,
                    "experiment": experiment_idx + 1,
                })
                results.append(logs)

                # Analyze algorithm complexity using ComplexityAnalyzer
                analyzer.analyze(func, X, Y)

                # Update progress bar
                pbar.set_postfix({
                    "algorithm": func_name,
                    "size": size,
                    "experiment": experiment_idx + 1,
                })
                pbar.update(1)

# Convert results to a pandas DataFrame
df = pd.DataFrame(results)

# Write the DataFrame to a CSV file
csv_filename = "lcs_benchmark_results.csv"
df.to_csv(csv_filename, index=False)

# Data Preprocessing: Convert time and memory columns to numeric
df['time'] = pd.to_numeric(df['time'], errors='coerce')
df['memory'] = pd.to_numeric(df['memory'], errors='coerce')

# Grouping by algorithm and size
grouped = df.groupby(['algorithm', 'size']).agg({
    'time': 'mean',
    'memory': 'mean',
}).reset_index()

# Save both raw and grouped results for later analysis
df.to_csv('lcs_results_raw.csv', index=False)
grouped.to_csv('lcs_results_grouped.csv', index=False)

# Display results using the visualizers
visualizer.visualize(df)
dashboard_visualizer.visualize(df)

print(f"\nResults have been saved to '{csv_filename}'")

