from complexity.generator import StringGenerator

# Recursive Solution
def lcs_recursive(X, Y):
    def helper(m, n):
        if m == 0 or n == 0:
            return 0
        if X[m - 1] == Y[n - 1]:
            return 1 + helper(m - 1, n - 1)
        else:
            return max(helper(m - 1, n), helper(m, n - 1))

    return helper(len(X), len(Y))


# Recursive Solution with Memoization
def lcs_memoized(X, Y):
    memo = {}

    def helper(m, n):
        if (m, n) in memo:
            return memo[(m, n)]
        if m == 0 or n == 0:
            memo[(m, n)] = 0
        elif X[m - 1] == Y[n - 1]:
            memo[(m, n)] = 1 + helper(m - 1, n - 1)
        else:
            memo[(m, n)] = max(helper(m - 1, n), helper(m, n - 1))
        return memo[(m, n)]

    return helper(len(X), len(Y))


# Dynamic Programming Solution
def lcs_dynamic(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # To reconstruct the LCS
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return ''.join(reversed(lcs)), dp[m][n]


# Main Execution
if __name__ == "__main__":
    # Initialize the string generator
    gen = StringGenerator(['A', 'C', 'G', 'T'])

    # Generate random strings
    str1, str2 = gen.generate_pair(10, 12, similarity=0.6)
    print("Generated String 1:", str1)
    print("Generated String 2:", str2)

    # Calculate LCS using Recursive Solution
    print("LCS (Recursive):", lcs_recursive(str1, str2))

    # Calculate LCS using Memoized Solution
    print("LCS (Memoized):", lcs_memoized(str1, str2))

    # Calculate LCS using Dynamic Programming
    lcs_result, lcs_length = lcs_dynamic(str1, str2)
    print("LCS (Dynamic):", lcs_result, "Length:", lcs_length)
