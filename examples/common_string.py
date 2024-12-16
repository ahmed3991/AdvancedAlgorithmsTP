#TODO: put the code here
import pandas as pd
from tqdm import tqdm
import numpy as np
import sys
import time
from pathlib import Path
# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from complexity.generator import StringGenerator  
from functools import lru_cache
from collections import namedtuple

Metrics = namedtuple('Metrics', ['time', 'length', 'memory'])

@lru_cache(None)
def lcs_recursive_memoized(X: str, Y: str) -> int:
    """Recursive LCS with memoization"""
    def helper(i: int, j: int) -> int:
        if i == 0 or j == 0:
            return 0
        if X[i - 1] == Y[j - 1]:
            return 1 + helper(i - 1, j - 1)
        else:
            return max(helper(i - 1, j), helper(i, j - 1))
    return helper(len(X), len(Y))

def lcs_dp(X: str, Y: str) -> int:
    """Bottom-Up LCS with Dynamic Programming"""
    m, n = len(X), len(Y)
    dp = np.zeros((m + 1, n + 1), dtype=int)
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

def profile_lcs(algo, X: str, Y: str) -> Metrics:
    start_time = time.time()
    length = algo(X, Y)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return Metrics(time=elapsed_time, length=length, memory=0)  

lcs_algorithms = [
    (lcs_recursive_memoized, 'Recursive_Memoized'),
    (lcs_dp, 'Dynamic_Programming')
]

sizes = [10, 50, 100, 200] 
nbr_experiments = 5 
similarity = 0.5  


generator = StringGenerator(['A', 'C', 'G', 'T'])

results = []

total_experiments = len(sizes) * nbr_experiments * len(lcs_algorithms)
print(f"\nRunning {total_experiments} LCS experiments...")

with tqdm(total=total_experiments, desc="Running experiments") as pbar:
    for size in sizes:
        for exp in range(nbr_experiments):
            X, Y = generator.generate_pair(size, size, similarity)
            for algo, algo_name in lcs_algorithms:
                metrics = profile_lcs(algo, X, Y)
                results.append({
                    'algorithm': algo_name,
                    'size': size,
                    'experiment': exp,
                    'time': metrics.time,
                    'lcs_length': metrics.length,
                    'memory': metrics.memory
                })
                pbar.update(1)

df = pd.DataFrame(results)

csv_file = 'lcs_results.csv'
df.to_csv(csv_file, index=False)
print(f"\nResults have been saved to '{csv_file}'")

grouped = df.groupby(['algorithm', 'size']).agg({
    'time': 'mean',
    'lcs_length': 'mean',
    'memory': 'mean'
}).reset_index()
summary_file = 'lcs_summary.csv'
grouped.to_csv(summary_file, index=False)
print(f"Summary results saved to '{summary_file}'")
print('Please use the complexity library')

