import random
import time

def lcs_recursive(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    if X[m-1] == Y[n-1]:
        return 1 + lcs_recursive(X, Y, m-1, n-1)
    else:
        return max(lcs_recursive(X, Y, m-1, n), lcs_recursive(X, Y, m, n-1))

def lcs_memoized(X, Y):
    memo = {}

    def helper(m, n):
        if (m, n) in memo:
            return memo[(m, n)]
        if m == 0 or n == 0:
            result = 0
        elif X[m-1] == Y[n-1]:
            result = 1 + helper(m-1, n-1)
        else:
            result = max(helper(m-1, n), helper(m, n-1))
        memo[(m, n)] = result
        return result

    return helper(len(X), len(Y))

def lcs_dp(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    i, j = m, n
    lcs = []
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs.append(X[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] > dp[i][j-1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs))

def lcs_optimized(X, Y):
    m, n = len(X), len(Y)
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i-1] == Y[j-1]:
                curr[j] = prev[j-1] + 1
            else:
                curr[j] = max(prev[j], curr[j-1])
        prev, curr = curr, [0] * (n + 1)

    return prev[-1]

class StringGenerator:
    def __init__(self, alphabet=['A', 'B', 'C']):
        self.alphabet = alphabet

    def generate(self, size: int = 1) -> str:
        return ''.join(random.choice(self.alphabet) for _ in range(size))

    def generate_pair(self, m: int, n: int) -> tuple:
        return self.generate(m), self.generate(n)

if __name__ == "__main__":
    # Generate test data
    gen = StringGenerator(['A', 'C', 'G', 'T'])
    str1, str2 = gen.generate_pair(10, 8)  # Adjust lengths for testing
    print(f"String 1: {str1}")
    print(f"String 2: {str2}")

    print("\nTesting Recursive Approach...")
    start = time.time()
    lcs_length_recursive = lcs_recursive(str1, str2, len(str1), len(str2))
    end = time.time()
    print(f"Recursive LCS Length: {lcs_length_recursive}")
    print(f"Execution Time: {end - start:.5f} seconds")
    print("\nTesting Memoized Recursive Approach...")
    start = time.time()
    lcs_length_memoized = lcs_memoized(str1, str2)
    end = time.time()
    print(f"Memoized LCS Length: {lcs_length_memoized}")
    print(f"Execution Time: {end - start:.5f} seconds")
    print("\nTesting Dynamic Programming Approach...")
    start = time.time()
    lcs_result_dp = lcs_dp(str1, str2)
    end = time.time()
    print(f"LCS (DP): {lcs_result_dp}")
    print(f"LCS Length: {len(lcs_result_dp)}")
    print(f"Execution Time: {end - start:.5f} seconds")
    print("\nTesting Optimized DP Approach...")
    start = time.time()
    lcs_length_optimized = lcs_optimized(str1, str2)
    end = time.time()
    print(f"Optimized DP LCS Length: {lcs_length_optimized}")
    print(f"Execution Time: {end - start:.5f} seconds")


    
    

