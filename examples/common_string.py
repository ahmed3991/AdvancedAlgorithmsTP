#TODO: put the code here

import time
import tracemalloc
import pandas as pd
from string import ascii_letters

def lcs_recursive(x: str, y: str) -> int:
    """
    Recursive implementation of LCS without memoization.
    :param x: First string.
    :param y: Second string.
    :return: Length of the longest common subsequence.
    """
    def helper(m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        if x[m - 1] == y[n - 1]:
            return 1 + helper(m - 1, n - 1)
        else:
            return max(helper(m - 1, n), helper(m, n - 1))

    return helper(len(x), len(y))

def lcs_memoized(x: str, y: str) -> int:
    """
    Recursive implementation of LCS with memoization.
    :param x: First string.
    :param y: Second string.
    :return: Length of the longest common subsequence.
    """
    memo = {}

    def helper(m: int, n: int) -> int:
        if m == 0 or n == 0:
            return 0
        if (m, n) in memo:
            return memo[(m, n)]

        if x[m - 1] == y[n - 1]:
            memo[(m, n)] = 1 + helper(m - 1, n - 1)
        else:
            memo[(m, n)] = max(helper(m - 1, n), helper(m, n - 1))

        return memo[(m, n)]

    return helper(len(x), len(y))

def lcs_dynamic_programming(x: str, y: str) -> tuple[int, str]:
    """
    Dynamic programming implementation of LCS.
    :param x: First string.
    :param y: Second string.
    :return: Tuple containing the length of the LCS and the LCS itself.
    """
    m, n = len(x), len(y)

    # Initialize the dp table with dimensions (m+1) x (n+1)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Fill the dp table using the bottom-up approach
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:  # Match
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:  # No match
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Retrieve the LCS by traversing the dp table in reverse order
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:  # Match, move diagonally
            lcs.append(x[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:  # Move up
            i -= 1
        else:  # Move left
            j -= 1

    # Reverse the collected characters to get the LCS
    lcs.reverse()
    return dp[m][n], ''.join(lcs)

def lcs_dynamic_1d(x: str, y: str) -> tuple[int, str]:
    """
    Dynamic programming implementation of LCS using a 1D beam (one-dimensional array).
    :param x: First string.
    :param y: Second string.
    :return: Tuple containing the length of the LCS and the LCS itself.
    """
    m, n = len(x), len(y)

    # Create a 1D array for the current and previous rows
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    # Fill the 1D array using bottom-up dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:  # Match
                curr[j] = prev[j - 1] + 1
            else:  # No match
                curr[j] = max(prev[j], curr[j - 1])

        # Update prev row to be the current row for the next iteration
        prev, curr = curr, prev

    # The length of the LCS is in the last cell of the previous row
    lcs_length = prev[n]

    # Retrieve the LCS by backtracking
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:  # Match, move diagonally
            lcs.append(x[i - 1])
            i -= 1
            j -= 1
        elif prev[j] == prev[j - 1]:  # Move left
            j -= 1
        else:  # Move up
            i -= 1

    # Reverse the collected characters to get the LCS
    lcs.reverse()
    return lcs_length, ''.join(lcs)

def measure_lcs(func, x, y):
    tracemalloc.start()
    start_time = time.perf_counter()
    result = func(x, y)
    end_time = time.perf_counter()
    memory_usage, _ = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return result[0] if isinstance(result, tuple) else result, end_time - start_time, memory_usage


# Main script
def main():
    # Generate string pairs
    generator = StringGenerator()
    test_cases = [
        ("small", generator.generate_pair(7, 8)),
        ("medium", generator.generate_pair(20, 26)),
        ("large", generator.generate_pair(50, 55))
    ]

    # Initialize results list
    results = []

    # Test all cases on all functions
    for size, (x, y) in test_cases:
        for func_name, func in [
            ("recursive", lcs_recursive),
            ("dynamic_2d", lcs_dynamic_programming),
            ("dynamic_1d", lcs_dynamic_1d)
        ]:
            try:
                lcs_length, exec_time, memory = measure_lcs(func, x, y)
                results.append({
                    "size": size,
                    "function": func_name,
                    "lcs_length": lcs_length,
                    "execution_time": exec_time,
                    "memory_usage": memory
                })
            except Exception as e:
                results.append({
                    "size": size,
                    "function": func_name,
                    "lcs_length": "Error",
                    "execution_time": "Error",
                    "memory_usage": "Error",
                    "error_message": str(e)
                })

    # Save results to CSV
    df = pd.DataFrame(results)
    df.to_csv("lcs_results.csv", index=False)
    print("Results saved to lcs_results.csv")


# Run the script
if __name__ == "__main__":
    main()

print('Please use the complexity library')

