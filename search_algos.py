from tqdm import tqdm
import numpy as np
import pandas as pd
import random
import tracemalloc
import time

# ==========================
# Function Definitions (LCS)
# ==========================

# Recursive LCS without memoization
def lcs_recursive_no_memo(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    if X[m - 1] == Y[n - 1]:
        return 1 + lcs_recursive_no_memo(X, Y, m - 1, n - 1)
    else:
        return max(lcs_recursive_no_memo(X, Y, m - 1, n), lcs_recursive_no_memo(X, Y, m, n - 1))

# Recursive LCS with memoization
def lcs_recursive_with_memo(X, Y, m, n, memo=None):
    if memo is None:
        memo = {}
    if (m, n) in memo:
        return memo[(m, n)]
    if m == 0 or n == 0:
        return 0
    if X[m - 1] == Y[n - 1]:
        memo[(m, n)] = 1 + lcs_recursive_with_memo(X, Y, m - 1, n - 1, memo)
    else:
        memo[(m, n)] = max(lcs_recursive_with_memo(X, Y, m - 1, n, memo), lcs_recursive_with_memo(X, Y, m, n - 1, memo))
    return memo[(m, n)]

# Dynamic Programming LCS
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

# Memory-optimized Dynamic Programming LCS
def lcs_dynamic_optimized(X, Y):
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

# ========================
# Test Initialization Logic
# ========================

# Initialize random tests
np.random.seed(42)
random.seed(42)

# Define string lengths
lengths = np.array(range(1000, 10000, 2000))
tests_per_length = 5

tests = []
for length in lengths:
    for _ in range(tests_per_length):
        # Generate two random strings
        alphabet = ['A', 'C', 'G', 'T']
        X = ''.join(random.choices(alphabet, k=length))
        Y = ''.join(random.choices(alphabet, k=length))
        tests.append((length, X, Y))

# ===================
# Profiling Functions
# ===================

def profile_function(func, X, Y):
    start_time = time.time()
    tracemalloc.start()
    result = func(X, Y)
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    elapsed_time = time.time() - start_time
    return result, elapsed_time, peak / 1024  # Return memory usage in KB

# ======================
# Running the Experiments
# ======================

results = []
functions = {
    "LCS Recursive No Memo": lcs_recursive_no_memo,
    "LCS Recursive With Memo": lambda X, Y: lcs_recursive_with_memo(X, Y, len(X), len(Y)),
    "LCS Dynamic": lcs_dynamic,
    "LCS Dynamic Optimized": lcs_dynamic_optimized,
}

for i, (length, X, Y) in tqdm(enumerate(tests), total=len(tests), ncols=80):
    for func_name, func in functions.items():
        if "Recursive" in func_name and length > 1000:
            # Skip recursive solutions for very large lengths
            continue
        result, time_taken, memory_used = profile_function(func, X, Y)
        results.append((i, func_name, length, result, time_taken, memory_used))

# =================
# Results and Output
# =================

df = pd.DataFrame(results, columns=['Test ID', 'Function Name', 'String Length', 'LCS Length', 'Time (s)', 'Memory (KB)'])
print(df)
df.to_csv('lcs_results.csv', index=False)
