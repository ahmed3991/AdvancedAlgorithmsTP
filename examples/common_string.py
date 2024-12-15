#TODO: put the code here
import pandas as pd
from tqdm import tqdm
import numpy as np
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from complexity.generator import StringGenerator
from complexity.profiler import TimeAndSpaceProfiler
from complexity.analyser import ComplexityAnalyzer

def lcs_recursive(x, y):
    if not x or not y:
        return ""
    if x[-1] == y[-1]:
        return lcs_recursive(x[:-1], y[:-1]) + x[-1]
    else:
        left = lcs_recursive(x[:-1], y)
        right = lcs_recursive(x, y[:-1])
        return left if len(left) > len(right) else right

def lcs_memoized(x, y, memo=None):
    if memo is None:
        memo = {}

    if (len(x), len(y)) in memo:
        return memo[(len(x), len(y))]

    if not x or not y:
        result = ""
    elif x[-1] == y[-1]:
        result = lcs_memoized(x[:-1], y[:-1], memo) + x[-1]
    else:
        left = lcs_memoized(x[:-1], y, memo)
        right = lcs_memoized(x, y[:-1], memo)
        result = left if len(left) > len(right) else right

    memo[(len(x), len(y))] = result
    return result

def lcs_dynamic(x, y):
    m, n = len(x), len(y)
    dp = [["" for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + x[i - 1]
            else:
                dp[i][j] = dp[i - 1][j] if len(dp[i - 1][j]) > len(dp[i][j - 1]) else dp[i][j - 1]

    return dp[m][n]


# Initialize profiler
profiler = TimeAndSpaceProfiler()

# Generate strings using StringGenerator
lengths = [3, 5, 6, 8, 10, 13, 15, 20]
gen = StringGenerator(alphabet=['A', 'B', 'C', 'D'], string_length=max(lengths))
string_pairs = [(gen.generate(length), gen.generate(length)) for length in lengths]

# Results storage
results = []

print("Running LCS experiments...")

with tqdm(total=len(string_pairs) * 3, desc="LCS experiments") as pbar:
    for str1, str2 in string_pairs:
        for algo, func in zip(
            ["recursive", "memoized", "dynamic"],
            [lcs_recursive, lambda x, y: lcs_memoized(x, y), lcs_dynamic]
        ):
          metrics = profiler.profile(func, str1, str2)
          results.append({
              'algorithm': algo,
              'str1': str1,
              'str2': str2,
              **metrics
          })
          pbar.update(1)

print("\nAnalyzing complexities...")


# Complexity analysis
analyzer = ComplexityAnalyzer()

analysis_results = []

for algo in ["recursive", "memoized", "dynamic"]:
    algo_data = [r for r in results if r['algorithm'] == algo]
    sizes = [len(r['str1']) for r in algo_data]
    times = [r['time'] for r in algo_data]

    complexity_name, complexity_func = analyzer.get_best_fit(np.array(sizes), np.array(times))
    analysis_results.append({
        'algorithm': algo,
        'complexity': complexity_name
    })

print("\nSaving results...")


# Convert results to DataFrame
df = pd.DataFrame(results)
df_analysis = pd.DataFrame(analysis_results)

# Save results
df.to_csv('lcs_results.csv', index=False)
df_analysis.to_csv('lcs_complexity_analysis.csv', index=False)

print("\nResults have been saved to 'lcs_results.csv' and 'lcs_complexity_analysis.csv'")


print('Please use the complexity library')


