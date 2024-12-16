import sys
import os

# Fix sys.path to include the parent directory
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, parent_dir)

import random
import numpy as np
from complexity.profiler import TimeAndSpaceProfiler
from complexity.analyser import ComplexityAnalyzer, LinearComplexity, QuadraticComplexity
from complexity.visualizer import ComplexityVisualizer
from complexity.generator import StringGenerator

# Longest Common Subsequence Implementations

def lcs_recursive(X, Y, memo=None):
    if memo is None:
        memo = {}
    if (len(X), len(Y)) in memo:
        return memo[(len(X), len(Y))]
    if not X or not Y:
        return 0
    elif X[-1] == Y[-1]:
        memo[(len(X), len(Y))] = 1 + lcs_recursive(X[:-1], Y[:-1], memo)
    else:
        memo[(len(X), len(Y))] = max(lcs_recursive(X[:-1], Y, memo), lcs_recursive(X, Y[:-1], memo))
    return memo[(len(X), len(Y))]


def lcs_memoization(X, Y, memo):
    if (len(X), len(Y)) in memo:
        return memo[(len(X), len(Y))]
    if not X or not Y:
        return 0
    elif X[-1] == Y[-1]:
        memo[(len(X), len(Y))] = 1 + lcs_memoization(X[:-1], Y[:-1], memo)
    else:
        memo[(len(X), len(Y))] = max(lcs_memoization(X[:-1], Y, memo), lcs_memoization(X, Y[:-1], memo))
    return memo[(len(X), len(Y))]


def lcs_dynamic(X, Y):
    m, n = len(X), len(Y)
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev, curr = curr, prev

    return prev[n]

# String Generator for Testing
class StringGenerator:
    def __init__(self, alphabet=['A', 'B', 'C']):
        self.alphabet = alphabet

    def generate(self, size: int = 1):
        return ''.join(random.choices(self.alphabet, k=size))

    def generate_pair(self, size1: int, size2: int):
        return self.generate(size1), self.generate(size2)

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

        # Profile recursive LCS with memoization
        profile_logs = profiler.profile(lcs_recursive, X, Y)
        time_rec = profile_logs.get("time", 0)
        times_recursive.append(time_rec)

        # Profile dynamic LCS
        profile_logs_dyn = profiler.profile(lcs_dynamic, X, Y)
        time_dyn = profile_logs_dyn.get("time", 0)
        times_dynamic.append(time_dyn)

    # Visualize complexities
    sizes_np = np.array(sizes)
    times_rec_np = np.array(times_recursive)
    times_dyn_np = np.array(times_dynamic)

    visualizer = ComplexityVisualizer(sizes_np, times_rec_np, [LinearComplexity(), QuadraticComplexity()])
    visualizer.plot("O(n^2)", "LCS Recursive with Memoization vs Sizes")

    visualizer = ComplexityVisualizer(sizes_np, times_dyn_np, [LinearComplexity(), QuadraticComplexity()])
    visualizer.plot("O(n^2)", "LCS Dynamic vs Sizes")
