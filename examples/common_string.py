import csv
import random
import time

# استخدم perf_counter لقياس الزمن بدقة
from time import perf_counter


def lcs_recursive(X, Y):
    if not X or not Y:
        return 0
    if X[-1] == Y[-1]:
        return 1 + lcs_recursive(X[:-1], Y[:-1])
    else:
        return max(lcs_recursive(X[:-1], Y), lcs_recursive(X, Y[:-1]))


def lcs_recursive_with_memoization(X, Y, memo=None):
    if memo is None:
        memo = {}
    if (len(X), len(Y)) in memo:
        return memo[(len(X), len(Y))]
    if not X or not Y:
        memo[(len(X), len(Y))] = 0
    elif X[-1] == Y[-1]:
        memo[(len(X), len(Y))] = 1 + lcs_recursive_with_memoization(X[:-1], Y[:-1], memo)
    else:
        memo[(len(X), len(Y))] = max(
            lcs_recursive_with_memoization(X[:-1], Y, memo),
            lcs_recursive_with_memoization(X, Y[:-1], memo),
        )
    return memo[(len(X), len(Y))]


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


class StringGenerator:
    def __init__(self, alphabet=None):
        if alphabet is None:
            alphabet = ["A", "B", "C"]
        self.alphabet = alphabet

    def generate(self, size=1):
        return "".join(random.choice(self.alphabet) for _ in range(size))

    def generate_pair(self, size1, size2):
        return self.generate(size1), self.generate(size2)


def run_tests():
    gen = StringGenerator(["A", "C", "G", "T"])
    test_data = [gen.generate_pair(10, 15) for _ in range(5)]  # إنشاء 5 أزواج من السلاسل

    recursive_results = []
    memoization_results = []
    dp_results = []
    benchmark_results = []

    for X, Y in test_data:
        # LCS Recursive
        start = perf_counter()
        recursive_result = lcs_recursive(X, Y)
        recursive_time = perf_counter() - start
        recursive_results.append((X, Y, recursive_result, recursive_time))

        # LCS Recursive with Memoization
        start = perf_counter()
        memoization_result = lcs_recursive_with_memoization(X, Y)
        memoization_time = perf_counter() - start
        memoization_results.append((X, Y, memoization_result, memoization_time))

        # LCS Dynamic Programming
        start = perf_counter()
        dp_result = lcs_dp(X, Y)
        dp_time = perf_counter() - start
        dp_results.append((X, Y, dp_result, dp_time))

        # Benchmark data
        benchmark_results.append((X, Y, (recursive_time, memoization_time, dp_time)))

    # Save results for each method
    save_results("lcs_recursive_results.csv", recursive_results)
    save_results("lcs_recursive_with_memoization_results.csv", memoization_results)
    save_results("lcs_dp_results.csv", dp_results)

    # Save benchmark results
    save_benchmark_results("lcs_benchmark_results.csv", benchmark_results)


def save_results(file_name, results):
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Test Number", "X", "Y", "Result", "Execution Time (s)"])
        for test_number, (X, Y, result, exec_time) in enumerate(results, start=1):
            writer.writerow([test_number, X, Y, result, exec_time])


def save_benchmark_results(file_name, benchmark_results):
    with open(file_name, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Test Number", "X", "Y", "Recursive Time", "Memoization Time", "DP Time"])
        for test_number, (X, Y, times) in enumerate(benchmark_results, start=1):
            writer.writerow([test_number, X, Y, *times])


if __name__ == "__main__":
    print("Running LCS tests and saving results to CSV files...")
    run_tests()
    print("Results saved to:")
    print("  - lcs_recursive_results.csv")
    print("  - lcs_recursive_with_memoization_results.csv")
    print("  - lcs_dp_results.csv")
    print("  - lcs_benchmark_results.csv")
