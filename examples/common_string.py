import csv
from pathlib import Path
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from complexity.generator import StringGenerator
from complexity.profiler import TimeAndSpaceProfiler
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def lcs_recursive(x, y):
    def helper(i, j):
        if i == 0 or j == 0:
            return 0
        if x[i - 1] == y[j - 1]:
            return 1 + helper(i - 1, j - 1)
        return max(helper(i - 1, j), helper(i, j - 1))

    return helper(len(x), len(y))


def lcs_memoized(x, y):
    memo = {}

    def helper(i, j):
        if i == 0 or j == 0:
            return 0
        if (i, j) in memo:
            return memo[(i, j)]

        if x[i - 1] == y[j - 1]:
            memo[(i, j)] = 1 + helper(i - 1, j - 1)
        else:
            memo[(i, j)] = max(helper(i - 1, j), helper(i, j - 1))

        return memo[(i, j)]

    return helper(len(x), len(y))


def lcs_dp(x, y):
    n, m = len(x), len(y)
    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]


def lcs_optimized(x, y):
    n, m = len(x), len(y)
    prev = [0] * (m + 1)
    curr = [0] * (m + 1)

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if x[i - 1] == y[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev, curr = curr, [0] * (m + 1)

    return prev[m]


def test_performance():
    gen = StringGenerator(["A", "C", "G", "T"])
    sizes = [10, 20, 50, 100, 200, 500, 1000, 2000, 5000]

    csv_file = Path(__file__).parent / "performance_results.csv"
    with open(csv_file, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(
            ["Algorithm", "String Size", "LCS Result", "Time (s)", "Memory (MB)"]
        )

        for size in sizes:
            s1 = gen.generate(size)
            s2 = gen.generate(size)

            print(f"Testing with strings of size {size}...")

            profiler = TimeAndSpaceProfiler()

            # Test each algorithm and write results to CSV
            for algorithm_name, algorithm in [
                # ("Recursive", lcs_recursive),
                # ("Memoized", lcs_memoized),
                ("DP", lcs_dp),
                # ("Optimized DP", lcs_optimized),
            ]:
                result, stats = profiler.profile(algorithm, s1, s2)
                print(f"{algorithm_name} LCS: {result}")
                print(f"Time: {stats['time']:.4f}s, Memory: {stats['memory']} MB")
                writer.writerow(
                    [algorithm_name, size, result, stats["time"], stats["memory"]]
                )
                file.flush()  # Flush the buffer to ensure immediate saving

            print("-" * 40)

    print(f"Results saved to {csv_file}")


if __name__ == "__main__":
    test_performance()