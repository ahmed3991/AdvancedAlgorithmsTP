import sys
import os

# Make sure to add the correct path to sys.path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, parent_dir)



import random
import numpy as np
from memory_profiler import memory_usage
from complexity.analyser import ComplexityAnalyzer, LinearComplexity, QuadraticComplexity
from complexity.visualizer import ComplexityVisualizer
from complexity.generator import StringGenerator
import time

# Longest Common Subsequence Implementations
def lcs_recursive(X, Y):
    if not X or not Y:
        return 0
    elif X[-1] == Y[-1]:
        return 1 + lcs_recursive(X[:-1], Y[:-1])
    else:
        return max(lcs_recursive(X[:-1], Y), lcs_recursive(X, Y[:-1]))

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

# String Generator for Testing
class StringGenerator:
    def __init__(self, alphabet=['A', 'B', 'C']):
        self.alphabet = alphabet

    def generate(self, size: int = 1):
        return ''.join(random.choices(self.alphabet, k=size))

    def generate_pair(self, size1: int, size2: int):
        return self.generate(size1), self.generate(size2)

# Profiler Class
class Profiler:
    def profile(self, func, *args, **kwargs):
        pass

class TimeAndSpaceProfiler(Profiler):
    def profile(self, func, *args, **kwargs):
        start_time = time.time()
        mem_before = memory_usage()[0]

        result = func(*args, **kwargs)

        mem_after = memory_usage()[0]
        end_time = time.time()

        logs = {
            "function": func.__name__,
            "time": end_time - start_time,
            "memory": mem_after - mem_before,
        }

        if hasattr(result, '_asdict'):
            logs.update(result._asdict())
        else:
            logs["result"] = result

        return logs

# Profiling and Visualization
if __name__ == "__main__":
    profiler = TimeAndSpaceProfiler()
    analyzer = ComplexityAnalyzer([LinearComplexity(), QuadraticComplexity()])

    # Generate test cases
    generator = StringGenerator(['A', 'C', 'G', 'T'])
    sizes = [5, 10, 15, 20, 25]  # Different input sizes
    times_recursive = []
    times_dynamic = []

    for size in sizes:
        X, Y = generator.generate_pair(size, size)

        # Profile recursive LCS
        profile_logs = profiler.profile(lcs_recursive, X, Y)
        time_rec = profile_logs["time"]
        times_recursive.append(time_rec)

        # Profile dynamic LCS
        profile_logs_dyn = profiler.profile(lcs_dynamic, X, Y)
        time_dyn = profile_logs_dyn["time"]
        times_dynamic.append(time_dyn)

    # Visualize complexities
    sizes_np = np.array(sizes)
    times_rec_np = np.array(times_recursive)
    times_dyn_np = np.array(times_dynamic)

    visualizer = ComplexityVisualizer(sizes_np, times_rec_np, [LinearComplexity(), QuadraticComplexity()])
    visualizer.plot("O(n^2)", "LCS Recursive vs Sizes")

    visualizer = ComplexityVisualizer(sizes_np, times_dyn_np, [LinearComplexity(), QuadraticComplexity()])
    visualizer.plot("O(n^2)", "LCS Dynamic vs Sizes")
