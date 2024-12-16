import pandas as pd
from tqdm import tqdm
import random
import time
import csv
from memory_profiler import memory_usage
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

# Step 1: Recursive Solution without Memoization
def lcs_recursive(X, Y, i, j):
    if i == 0 or j == 0:
        return 0
    if X[i - 1] == Y[j - 1]:
        return 1 + lcs_recursive(X, Y, i - 1, j - 1)
    else:
        return max(lcs_recursive(X, Y, i - 1, j), lcs_recursive(X, Y, i, j - 1))

# Step 2: Recursive Solution with Memoization
def lcs_recursive_memo(X, Y, i, j, memo):
    if i == 0 or j == 0:
        return 0
    if (i, j) in memo:
        return memo[(i, j)]
    if X[i - 1] == Y[j - 1]:
        memo[(i, j)] = 1 + lcs_recursive_memo(X, Y, i - 1, j - 1, memo)
    else:
        memo[(i, j)] = max(lcs_recursive_memo(X, Y, i - 1, j, memo), lcs_recursive_memo(X, Y, i, j - 1, memo))
    return memo[(i, j)]

# Step 3: Dynamic Programming Approach (Bottom-Up)
def lcs_dp(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

# Step 4: String Generator Class
class StringGenerator:
    def __init__(self, alphabet=['A', 'B', 'C']):
        self.alphabet = alphabet

    def generate(self, size: int = 1) -> str:
        return ''.join(random.choice(self.alphabet) for _ in range(size))

    def generate_pair(self, size1: int, size2: int) -> tuple:
        return self.generate(size1), self.generate(size2)

# Function to measure memory usage and execution time
def measure_performance(lcs_func, *args):
    start_time = time.time()
    mem_usage = memory_usage((lcs_func, args))
    end_time = time.time()
    return end_time - start_time, max(mem_usage) - min(mem_usage)

# Function to write results to CSV file
def write_to_csv(data, filename="lcs_performance_results.csv"):
    header = ['Method', 'Time (seconds)', 'Memory Usage (MB)']
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(data)

# Main Function for Testing and Generating Results
def main():
    # Generate test data
    gen = StringGenerator(['A', 'B', 'C', 'D', 'E'])
    X, Y = gen.generate(20), gen.generate(15)

    # Test and measure performance for recursive approach (without memoization)
    time_rec, mem_rec = measure_performance(lcs_recursive, X, Y, len(X), len(Y))

    # Test and measure performance for recursive approach (with memoization)
    memo = {}
    time_rec_memo, mem_rec_memo = measure_performance(lcs_recursive_memo, X, Y, len(X), len(Y), memo)

    # Test and measure performance for dynamic programming approach
    time_dp, mem_dp = measure_performance(lcs_dp, X, Y)

    # Collect results in a list
    results = [
        ['Recursive (No Memo)', time_rec, mem_rec],
        ['Recursive (With Memo)', time_rec_memo, mem_rec_memo],
        ['Dynamic Programming', time_dp, mem_dp],
    ]

    # Write results to CSV
    write_to_csv(results)

# Run the main function
if __name__ == "__main__":
    main()