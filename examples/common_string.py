#TODO: put the code here

import pandas as pd
from tqdm import tqdm
import sys
from pathlib import Path
from collections import namedtuple

sys.path.append(str(Path(__file__).parent.parent))

from complexity import (
    DataGeneratorFactory,
    StringGenerator,
    TimeAndSpaceProfiler,
    ComplexityAnalyzer,
    ComplexityVisualizer,
    ComplexityDashboardVisualizer
)


## Data Generation

factory = DataGeneratorFactory()
factory.register_generator("string",StringGenerator(['A','B','C','D','E']))

lengths = [10, 100, 1000]
nbr_experiments=3

random_pairs = [
    factory.get_generator("string").generate_pair(size,size) for size in lengths for _ in range(nbr_experiments) 
]

different_pairs = [
    factory.get_generator("string").generate_diff_pair(size,size) for size in lengths for _ in range(nbr_experiments)
]

identical_pairs = [
    factory.get_generator("string").generate_ident_pair(size) for size in lengths for _ in range(nbr_experiments)
]



## Functions

    # Help functions

def longest_string(x,y):
    return x if len(x) > len (y) else y

    # LCS functions

def lcs_rec_memo(x,y,i,j,memo):

    if(i,j) in memo:
        return memo[(i,j)]

    if i == 0 or j == 0 :
        return ""
    
    if x[i-1] == y [j-1]:
        memo[(i,j)] = lcs_rec_memo(x,y,i-1,j-1,memo) + x[i-1]
        return memo[(i,j)]
    
    lcs1=lcs_rec_memo(x,y,i-1,j,memo)
    lcs2=lcs_rec_memo(x,y,i,j-1,memo)

    memo[(i,j)] = longest_string(lcs1,lcs2)
    return memo[(i,j)]

def lcs_rec(x,y,i,j):

    if i == 0 or j == 0 :
        return ""

    if x[i-1]==y[j-1] :
        return lcs_rec(x,y,i-1,j-1) + x[i-1]
    
    lcs1 = lcs_rec(x,y,i-1,j)
    lcs2 = lcs_rec(x,y,i,j-1)

    return longest_string(lcs1,lcs2)

def lcs_dp(x,y):

    n=len(x)
    m=len(y)

    dp = [["" for _ in range(m+1)] for _ in range(n+1)]

    for i in range(1,n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                dp[i][j] = dp[i-1][j-1] + x[i-1]
            else:
                dp[i][j] = dp[i-1][j] if len(dp[i-1][j])>len(dp[i][j-1]) else dp[i][j-1]

    return dp[n][m]


## Benchmarking

funcs = [
    lcs_rec,
    lcs_rec_memo,
    lcs_dp
]

profiler = TimeAndSpaceProfiler()
results = []

total_iterations = len(funcs) * len(lengths) * nbr_experiments * 3  # 3 for random, sorted, inverse_sorted
with tqdm(total=total_iterations, desc="Benchmarking", unit="experiment") as pbar:

    for func in funcs:
        for size, random_experiments, identical_experiments, diffirent_experiments in zip(
            lengths,random_pairs,identical_experiments,different_pairs
        ):
            for experiment_idx in range(nbr_experiments):
                for x,y in [
                    (random_experiments[experiment_idx], "random"),
                    (identical_experiments[experiment_idx], "identical"),
                    (diffirent_experiments[experiment_idx], "different"),
                ]:
                    logs = profiler.profile(func,x,y)
                    logs.update({
                        "algorithm": func.__name__,
                        "first_string": x,
                        "second_string": y,
                        "size": size,
                        "experiment": experiment_idx + 1,
                    })
                    results.append(logs)

                    pbar.set_postfix({
                        "algorithm": func.__name__,
                        "first_string": x,
                        "second_string": y,
                        "size": size,
                        "experiment": experiment_idx + 1,
                    })

df = pd.DataFrame(results)
csv_filename = "benchmark_results.csv"
df.to_csv(csv_filename, index=False)

df['time'] = pd.to_numeric(df['time'], errors='coerce')
df['memory'] = pd.to_numeric(df['memory'], errors='coerce')

grouped = df.groupby(['algorithm', 'first_string', 'second_string', 'size']).agg({
    'time': 'mean',
    'memory': 'mean',
}).reset_index()

df.to_csv('sort_results_raw.csv', index=False)
grouped.to_csv('sort_results_grouped.csv', index=False)

print("\nResults have been saved to 'sort_results_raw.csv' and 'sort_results_grouped.csv'")