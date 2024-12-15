from memory_profiler import profile
from tqdm import tqdm
import pandas as pd
from tqdm import tqdm
import numpy as np
import sys
from pathlib import Path

from complexity import TimeAndSpaceProfiler
from complexity.generator import StringGenerator
from examples.search_algos import nbr_experiments

sizes = [20, 50, 80, 100]
gen = StringGenerator(['A', 'C', 'G', 'T'])


# Recursive LCS function
def LCS_recursive(X: str, Y: str, size_x: int, size_y: int) -> int:
    if size_x == 0 or size_y == 0:
        return 0
    elif X[size_x - 1] == Y[size_y - 1]:
        return 1 + LCS_recursive(X, Y, size_x - 1, size_y - 1)
    else:
        return max(LCS_recursive(X, Y, size_x - 1, size_y),
                   LCS_recursive(X, Y, size_x, size_y - 1))


# Bottom-up LCS function
def LCS_bottom_up(X: str, Y: str) -> int:
    size_x, size_y = len(X), len(Y)

    # Initialize a 2D array for dynamic programming
    dp = [[0] * (size_y + 1) for _ in range(size_x + 1)]

    # Fill the dp table iteratively
    for i in range(1, size_x + 1):
        for j in range(1, size_y + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[size_x][size_y]
nbr_experiments== 5

results = []

profiler = TimeAndSpaceProfiler()

common_string_algorithms = [
    LCS_recursive,
    LCS_bottom_up
]

total_experiments = nbr_experiments * len(sizes) * len(common_string_algorithms)


with tqdm(total=total_experiments, desc="Running experiments") as pbar:
    for size in sizes:
        for exp in range(nbr_experiments):
            # Generate strings for this experiment
            X = gen.generate(size)
            Y = gen.generate(size)

            # Test each algorithm
            for algo in common_string_algorithms:
                algo_name = algo.__name__

                # Profile the algorithm
                if algo == LCS_recursive:
                    metrics = profile(algo, X, Y, len(X), len(Y))
                elif algo == LCS_bottom_up:
                    metrics = profile(algo, X, Y)

                # Append results
                results.append({
                    'algorithm': algo_name,
                    'data_type': 'random',
                    'size': size,
                    'experiment': exp,
                    **metrics,
                })

                # Update progress bar
                pbar.update(1)

# Save raw results
df = pd.DataFrame(results)
df.to_csv('common_string_results_raw.csv', index=False)

# Data Preprocessing: Convert time and memory columns to numeric
df['time'] = pd.to_numeric(df['time'], errors='coerce')
df['memory'] = pd.to_numeric(df['memory'], errors='coerce')

# Group results by algorithm, data type, and size
grouped = df.groupby(['algorithm', 'data_type', 'size']).agg({
    'time': 'mean',
    'memory': 'mean',
    'result': 'mean'
}).reset_index()

# Save grouped results
grouped.to_csv('common_string_results_grouped.csv', index=False)

print("\nResults have been saved to 'common_string_results_raw.csv' and 'common_string_results_grouped.csv'")


def main():
    for size in sizes:
        # Generate random strings of the given size
        x = gen.generate(size)
        y = gen.generate(size)

        # Compute LCS using both recursive and bottom-up approaches
        recursive_result = LCS_recursive(x, y, len(x), len(y))
        bottom_up_result = LCS_bottom_up(x, y)

        # Print the results
        print(f"Size: {size}")
        print(f"Recursive LCS: {recursive_result}")
        print(f"Bottom-up LCS: {bottom_up_result}")
        print()


if __name__ == "__main__":
    main()
