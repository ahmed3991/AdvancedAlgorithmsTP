from tqdm import tqdm
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../complexity")))

from analyser import ComplexityAnalyzer
from generator import StringGenerator
from visualizer import ComplexityVisualizer
from profiler import TimeAndSpaceProfiler
import numpy as np
import pandas as pd

#TODO: put the code here
print('Please use the complexity library')

## Implement a recursive solution without memoization
def Lcs_recursive(x: str, y: str) -> int:

    if not x or not y:
        return 0
    if x[-1] == y[-1]:
        return 1 + Lcs_recursive(x[:-1], y[:-1])
    else:
        return max(Lcs_recursive(x[:-1], y), Lcs_recursive(x, y[:-1]))

## Implement a recursive solution with memoization
def Lcs_recursive_with_memoization(x: str, y: str, memo: dict = {}) -> int:
    if not x or not y:
        return 0
    
    if (x, y) in memo:
        return memo[(x, y)]
    
    if x[-1] == y[-1]:
        memo[(x, y)] = 1 + Lcs_recursive_with_memoization(x[:-1], y[:-1], memo)
    else:
        memo[(x, y)] = max(Lcs_recursive_with_memoization(x[:-1], y, memo),
                           Lcs_recursive_with_memoization(x, y[:-1], memo))
    
    return memo[(x, y)]

## Implement a dynamic programming (bottom-up) solution.
def Lcs_dp(x: str, y: str) -> int:

    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

## Save LCS performance results to a CSV file
def Save_results(str_lengths, recursive_times,recursive_memo_times ,dp_times, memory_usage_recursive,memory_usage_recursive_memo, memory_usage_dp):

    data = {
        "String Length": str_lengths,
        "Recursive Time": recursive_times,
        "Recursive Memo Time":recursive_memo_times,
        "DP Time": dp_times,
        "Recursive Memory usage ": memory_usage_recursive,
        "Recursive memoized Memory usage":memory_usage_recursive_memo,
        "DP Memory usage": memory_usage_dp
    }    
    df = pd.DataFrame(data)
    df.to_csv("lcs_performance_results.csv", index=False)
    print("Results saved to lcs_performance_results.csv")

## Test,save and compare the performance of recursive and dynamic programming LCS algorithms
def Test_lcs_performance():

    # Generate strings
    string_generator = StringGenerator(['A', 'B', 'C', 'D'])
    str_lengths = np.array([3 , 6, 12, 15, 16])
    recursive_times = []
    recursive_memoized_times = []
    dp_times = []
    memory_usage_recursive = []
    memory_usage_recursive_memoized = [] 
    memory_usage_dp = []

    profiler = TimeAndSpaceProfiler()

    # for length in str_lengths:
    for length in tqdm(str_lengths, desc="Running LCS Performance Tests"):    
        str1 = string_generator.generate(length)
        str2 = string_generator.generate(length)

        # Measure recursive execution time and mamory usage
        result = profiler.profile(Lcs_recursive, str1, str2)
        recursive_times.append(result["time"])
        memory_usage_recursive.append(result["memory"]) 

        # Measure memoized recursive execution time and memory usage
        result = profiler.profile(Lcs_recursive_with_memoization, str1, str2, {})
        recursive_memoized_times.append(result["time"])
        memory_usage_recursive_memoized.append(result["memory"])

        # Measure dynamic programming execution time and mamory usage
        result = profiler.profile(Lcs_dp, str1, str2)
        dp_times.append(result['time'])
        memory_usage_dp.append(result['memory'])
    
    Save_results(str_lengths, recursive_times, recursive_memoized_times, dp_times, memory_usage_recursive, memory_usage_recursive_memoized, memory_usage_dp)

    # Analyze and visualize
    analyzer = ComplexityAnalyzer()
    recursive_complexity = analyzer.get_best_fit(str_lengths, np.array(recursive_times))
    memoized_complexity = analyzer.get_best_fit(str_lengths, np.array(recursive_times))
    dp_complexity = analyzer.get_best_fit(str_lengths, np.array(dp_times))

    print(f"Recursive complexity fit: {recursive_complexity}")
    print(f"Memoized recursive complexity fit: {memoized_complexity}")
    print(f"Dynamic programming complexity fit: {dp_complexity}")

    recursive_complexity_name = recursive_complexity[0]
    memoized_complexity_name = memoized_complexity[0]
    dp_complexity_name = dp_complexity[0] 
    
    # Visualize  execution time performance for recursive dynamic programming
    visualizer = ComplexityVisualizer( str_lengths, np.array(recursive_times), analyzer.complexity_functions)
    visualizer.plot(recursive_complexity_name, title="Recursive LCS Performance")

    visualizer = ComplexityVisualizer(str_lengths, np.array(recursive_memoized_times), analyzer.complexity_functions)
    visualizer.plot(memoized_complexity_name, title="Memoized Recursive LCS Performance")

    visualizer = ComplexityVisualizer(str_lengths, np.array(dp_times), analyzer.complexity_functions)
    visualizer.plot(dp_complexity_name, title="Dynamic Programming LCS Performance")

    # Visualize memory usage for recursive with and without memoiasation dynamic programming
    memory_visualizer = ComplexityVisualizer( str_lengths, np.array(memory_usage_recursive), analyzer.complexity_functions)
    memory_visualizer.plot(recursive_complexity_name, title="Memory Usage Recursive")

    memory_visualizer = ComplexityVisualizer(str_lengths, np.array(memory_usage_recursive_memoized), analyzer.complexity_functions)
    memory_visualizer.plot(memoized_complexity_name, title="Memory Usage Memoized")

    memory_visualizer = ComplexityVisualizer(str_lengths, np.array(memory_usage_dp), analyzer.complexity_functions)
    memory_visualizer.plot(dp_complexity_name, title="Memory Usage DP")

if __name__ == "__main__":
    Test_lcs_performance()
