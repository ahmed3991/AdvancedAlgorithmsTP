import time
import tracemalloc
import csv
import psutil
import os

# Recursive LCS
def lcs_recursive(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]:
        return 1 + lcs_recursive(X, Y, m - 1, n - 1)
    else:
        return max(lcs_recursive(X, Y, m - 1, n), lcs_recursive(X, Y, m, n - 1))

# Recursive LCS with Memoization
def lcs_recursive_memo(X, Y, m, n, memo):
    if (m, n) in memo:
        return memo[(m, n)]
    if m == 0 or n == 0:
        result = 0
    elif X[m - 1] == Y[n - 1]:
        result = 1 + lcs_recursive_memo(X, Y, m - 1, n - 1, memo)
    else:
        result = max(lcs_recursive_memo(X, Y, m - 1, n, memo), lcs_recursive_memo(X, Y, m, n - 1, memo))
    memo[(m, n)] = result
    return result

# Dynamic Programming LCS
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

# Helper function to measure time and memory
def measure_lcs(func, *args):
    # Start tracking memory
    tracemalloc.start()

    # Start tracking process memory usage
    process = psutil.Process(os.getpid())
    start_mem = process.memory_info().rss

    # Start the timer
    start_time = time.perf_counter()
    
    # Execute the function
    result = func(*args)

    # End the timer
    end_time = time.perf_counter()

    # Get memory usage
    end_mem = process.memory_info().rss
    current, peak = tracemalloc.get_traced_memory()

    # Stop tracking memory
    tracemalloc.stop()

    return result, end_time - start_time, end_mem - start_mem, peak

# Main execution
def main():
    X = "ABCBDAB"
    Y = "BDCAB"

    results = []

    # Measure Recursive LCS
    _, rec_time, rec_memory_diff, rec_memory_peak = measure_lcs(lcs_recursive, X, Y, len(X), len(Y))
    
    # Measure Recursive LCS with Memoization
    _, rec_memo_time, rec_memo_memory_diff, rec_memo_memory_peak = measure_lcs(lcs_recursive_memo, X, Y, len(X), len(Y), {})

    # Measure DP LCS
    _, dp_time, dp_memory_diff, dp_memory_peak = measure_lcs(lcs_dp, X, Y)

    # Collect results in a dictionary
    results.append({
        "Recursive Time (s)": round(rec_time, 6),
        "Recursive Memo Time (s)": round(rec_memo_time, 6),
        "DP Time (s)": round(dp_time, 6),
        "Recursive Memory Usage Diff (bytes)": rec_memory_diff,
        "Recursive Memoized Memory Usage Diff (bytes)": rec_memo_memory_diff,
        "DP Memory Usage Diff (bytes)": dp_memory_diff,
        "Recursive Memory Peak Usage (bytes)": rec_memory_peak,
        "Recursive Memoized Memory Peak Usage (bytes)": rec_memo_memory_peak,
        "DP Memory Peak Usage (bytes)": dp_memory_peak
    })

    # Write results to CSV
    with open('lcs_results.csv', 'w', newline='') as csvfile:
        fieldnames = [
            "Recursive Time (s)",
            "Recursive Memo Time (s)",
            "DP Time (s)",
            "Recursive Memory Usage Diff (bytes)",
            "Recursive Memoized Memory Usage Diff (bytes)",
            "DP Memory Usage Diff (bytes)",
            "Recursive Memory Peak Usage (bytes)",
            "Recursive Memoized Memory Peak Usage (bytes)",
            "DP Memory Peak Usage (bytes)"
        ]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print("Results saved to 'lcs_results.csv'. Please refer to the CSV for detailed analysis.")

if __name__ == "__main__":
    main()
