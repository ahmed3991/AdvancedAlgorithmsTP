import sys
import os
from tqdm import tqdm
import random
import numpy as np
import pandas as pd
from complexity.profiler import TimeAndSpaceProfiler

def random_string(size):
    return ''.join(np.random.choice(['A', 'C', 'G', 'T'], size=size))

def lcs(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    if X[m - 1] == Y[n - 1]:
        return 1 + lcs(X, Y, m - 1, n - 1)
    else:
        return max(lcs(X, Y, m, n - 1), lcs(X, Y, m - 1, n))

def lcs_memo(X, Y, m, n, memo):
    if m == 0 or n == 0:
        return 0
    if (m, n) in memo:
        return memo[(m, n)]
    if X[m - 1] == Y[n - 1]:
        memo[(m, n)] = 1 + lcs_memo(X, Y, m - 1, n - 1, memo)
        return memo[(m, n)]
    else:
        memo[(m, n)] = max(lcs_memo(X, Y, m, n - 1, memo), lcs_memo(X, Y, m - 1, n, memo))
        return memo[(m, n)]

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

lengths = [5, 10, 15, 17]
nbr_experiments = 3

random_arrays = [
    [random_string(size) for _ in range(nbr_experiments)] for size in lengths
]

profiler = TimeAndSpaceProfiler()

funcs = [lcs, lcs_memo, lcs_dp]
results = []

with tqdm(total=len(funcs) * len(lengths) * nbr_experiments, desc="Benchmarking") as pbar:
    for func in funcs:
        for size, random_experiments in zip(lengths, random_arrays):
            for experiment_idx in range(nbr_experiments):
                data = random_experiments[experiment_idx]

                if func == lcs_memo:
                    memo = {}
                    logs = profiler.profile(func, data, data, len(data), len(data), memo)
                elif func == lcs:
                    logs = profiler.profile(func, data, data, len(data), len(data))
                else:
                    logs = profiler.profile(func, data, data)

                if isinstance(logs, dict):
                    logs.update({
                        "algorithm": func.__name__,
                        "size": size,
                        "experiment": experiment_idx + 1,
                    })
                else:
                    logs = {
                        "algorithm": func.__name__,
                        "size": size,
                        "experiment": experiment_idx + 1,
                        "result": logs
                    }
                results.append(logs)
                pbar.update(1)

df = pd.DataFrame(results)

df.to_csv("lcs_benchmark_results.csv", index=False)

grouped = df.groupby(['algorithm', 'size']).agg({
    'time': 'mean',
    'memory': 'mean'
}).reset_index()

grouped.to_csv('lcs_grouped_results.csv', index=False)

print("\nResults have been saved to 'lcs_benchmark_results.csv' and 'lcs_grouped_results.csv'")
