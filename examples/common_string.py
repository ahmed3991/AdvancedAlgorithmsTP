#TODO: put the code here
# Recursive LCS (without memoization)
def lcs_recursive(X, Y, m, n):
    if m == 0 or n == 0:
        return 0
    elif X[m - 1] == Y[n - 1]:
        return 1 + lcs_recursive(X, Y, m - 1, n - 1)
    else:
        return max(lcs_recursive(X, Y, m, n - 1), lcs_recursive(X, Y, m - 1, n))


# Recursive LCS with Memoization
def lcs_memoized(X, Y, m, n, memo):
    if (m, n) in memo:
        return memo[(m, n)]

    if m == 0 or n == 0:
        memo[(m, n)] = 0
    elif X[m - 1] == Y[n - 1]:
        memo[(m, n)] = 1 + lcs_memoized(X, Y, m - 1, n - 1, memo)
    else:
        memo[(m, n)] = max(lcs_memoized(X, Y, m, n - 1, memo), lcs_memoized(X, Y, m - 1, n, memo))

    return memo[(m, n)]


# Dynamic Programming LCS (Bottom-Up approach)
def lcs_dp(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Trace back to reconstruct LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs))


# String Generator class to generate test strings
import random


class StringGenerator:
    def __init__(self, alphabet=['A', 'B', 'C']):
        self.alphabet = alphabet

    def generate(self, size: int = 1) -> str:
        return ''.join(random.choice(self.alphabet) for _ in range(size))

    def generate_pair(self, size1: int, size2: int):
        return self.generate(size1), self.generate(size2)


# Example usage of StringGenerator
gen = StringGenerator(['A', 'B', 'C'])
str1, str2 = gen.generate_pair(10, 12)

print("String 1:", str1)
print("String 2:", str2)
print("LCS (Recursive):", lcs_recursive(str1, str2, len(str1), len(str2)))
print("LCS (Memoized):", lcs_memoized(str1, str2, len(str1), len(str2), {}))
print("LCS (DP):", lcs_dp(str1, str2))
