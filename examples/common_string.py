import sys
from pathlib import Path

import random
import pandas as pd
from tqdm import tqdm
from collections import namedtuple

from complexity import (
    DataGeneratorFactory,
    TimeAndSpaceProfiler,
    StringGenerator
)

sys.path.append(str(Path(__file__).parent.parent))

from collections import namedtuple

Metrics = namedtuple('Metrics', ['n', 'm', 'result', 'comparison_count'])

# ======================================================================= #
def lcs_recursive(X, Y, i, j, comparison_count=0):
    # Base case
    if i == 0 or j == 0:
        comparison_count += 1  # Counting the comparison
        return Metrics(n=i, m=j, result=0, comparison_count=comparison_count)

    # If characters match, add 1 to result and call LCS for remaining parts
    elif X[i-1] == Y[j-1]:
        comparison_count += 1  # Counting the comparison
        return Metrics(n=i, m=j, result=1 + lcs_recursive(X, Y, i-1, j-1, comparison_count).result,
                       comparison_count=comparison_count)
    
    # Otherwise, take the maximum of two possible subproblems
    else:
        comparison_count += 1  # Counting the comparison
        left = lcs_recursive(X, Y, i-1, j, comparison_count)
        right = lcs_recursive(X, Y, i, j-1, comparison_count)
        return Metrics(n=i, m=j, result=max(left.result, right.result), comparison_count=comparison_count)


# ======================================================================= #
def lcs_memoized(X, Y, i, j, memo, comparison_count=0):
    # Base case
    if i == 0 or j == 0:
        return Metrics(n=i, m=j, result=0, comparison_count=comparison_count)

    # If result is already calculated then return it
    if memo[i][j] is not None:
        return Metrics(n=i, m=j, result=memo[i][j], comparison_count=comparison_count)

    # If characters match
    if X[i-1] == Y[j-1]:
        comparison_count += 1  # Counting the comparison
        memo[i][j] = lcs_memoized(X, Y, i-1, j-1, memo, comparison_count).result + 1
    else:
        comparison_count += 1  # Counting the comparison
        memo[i][j] = max(lcs_memoized(X, Y, i-1, j, memo, comparison_count).result,
                          lcs_memoized(X, Y, i, j-1, memo, comparison_count).result)
    
    return Metrics(n=i, m=j, result=memo[i][j], comparison_count=comparison_count)


# ======================================================================= #
def lcs_dp(X, Y):
    m, n = len(X), len(Y)
    # Initialize DP table
    dp = [[0] * (n+1) for _ in range(m+1)]
    comparison_count = 0  # Initialize comparison counter

    # Fill DP table
    for i in range(1, m+1):
        for j in range(1, n+1):
            comparison_count += 1  # Counting the comparison (X[i-1] == Y[j-1])
            if X[i-1] == Y[j-1]:  # If characters match
                dp[i][j] = 1 + dp[i-1][j-1]
            else:  # Take max of excluding current character from X or Y
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return Metrics(n=m, m=n, result=dp[m][n], comparison_count=comparison_count)


# ======================================================================= #
def lcs_dp_optimized(X, Y):
    m, n = len(X), len(Y)
    # Use two rows instead of full DP table
    prev = [0] * (n+1)
    curr = [0] * (n+1)
    comparison_count = 0  # Initialize comparison counter

    for i in range(1, m+1):
        for j in range(1, n+1):
            comparison_count += 1  # Counting the comparison (X[i-1] == Y[j-1])
            if X[i-1] == Y[j-1]:
                curr[j] = 1 + prev[j-1]
            else:
                curr[j] = max(prev[j], curr[j-1])
        prev, curr = curr, prev  # Swap rows

    return Metrics(n=m, m=n, result=prev[n], comparison_count=comparison_count)


# ======================================================================= #
def lcs_reconstruct(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n+1) for _ in range(m+1)]
    comparison_count = 0  # Initialize comparison counter

    # Fill DP table
    for i in range(1, m+1):
        for j in range(1, n+1):
            comparison_count += 1  # Counting the comparison (X[i-1] == Y[j-1])
            if X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    # Backtrack to reconstruct LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        comparison_count += 1  # Counting the comparison (X[i-1] == Y[j-1])
        if X[i-1] == Y[j-1]:
            lcs.append(X[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return Metrics(n=m, m=n, result=len(''.join(reversed(lcs))), comparison_count=comparison_count)



# Set up data generators
factory = DataGeneratorFactory()

# Customize alphabet dynamically
default_alphabet = [chr(i) for i in range(65, 91)]   # all the alphabet
factory.register_generator("random_string", StringGenerator(alphabet=default_alphabet))

# Ensure reproducibility by setting a random seed
random.seed(42)  # Replace 42 with any seed value for consistent results

# Define ranges for each experiment
ranges = [100, 500, 1000]  # Modify as per your requirement
nbr_experiments = 20  # Number of experiments per size

# Include specific edge cases
edge_cases = [
    (1, 1, 0.0),  # Minimum size, completely dissimilar
    (1, 1, 1.0),  # Minimum size, identical
    (1000, 1000, 0.0),  # Large size, completely dissimilar
    (1000, 1000, 1.0),  # Large size, identical
]

# Generate pairs of strings with different lengths (m and n) and similarity for each experiment
random_string_pairs = [
    [
        # Generate m, n, and similarity within specific ranges
        factory.get_generator("random_string").generate_pair(
            m=random.randint(1, size),  # Random length m from 1 to 'size'
            n=random.randint(1, size),  # Random length n from 1 to 'size'
            similarity=random.uniform(0.0, 1.0)  # Random similarity between 0.0 and 1.0
        ) for _ in range(nbr_experiments)
    ]
    for size in ranges
]

# Add edge cases explicitly to the dataset
for m, n, similarity in edge_cases:
    random_string_pairs.append([
        factory.get_generator("random_string").generate_pair(m=m, n=n, similarity=similarity)
    ])
# Functions to benchmark
funcs = [
    #lcs_recursive,
    lcs_memoized,
    lcs_dp,
    lcs_dp_optimized,
    lcs_reconstruct,
]

# Benchmarking
profiler = TimeAndSpaceProfiler()
results = []

# Create a tqdm progress bar for tracking the experiments
total_iterations = len(funcs) * len(ranges) * nbr_experiments
print(f"\nRunning {total_iterations} LCS function experiments...")
with tqdm(total=total_iterations, desc="Benchmarking", unit="experiment") as pbar:
    for func in funcs:
        for size, experiments in zip(ranges, random_string_pairs):
            for experiment_idx, data in enumerate(experiments):
                # Run and profile
                X, Y = data  # The two strings to compare
                if func == lcs_recursive:
                    logs = profiler.profile(func, X, Y, len(X), len(Y))
                elif func == lcs_memoized:
                    memo = [[None] * (len(Y)+1) for _ in range(len(X)+1)]
                    logs = profiler.profile(func, X, Y, len(X), len(Y), memo)

                else:
                    logs = profiler.profile(func, X, Y)
                
                    
                results.append({
                    "size": size,
                    **logs
                })
                pbar.update(1)
                
                
# Save results to CSV
results_df = pd.DataFrame(results)
results_df.to_csv("benchmark_results.csv", index=False)
print("\nBenchmarking completed. Results saved to 'benchmark_results.csv'.")