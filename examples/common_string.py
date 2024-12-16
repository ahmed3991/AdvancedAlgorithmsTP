def lcs_recursive(x, y):
    
    if not x or not y:
        return ""

    if x[-1] == y[-1]:
        return lcs_recursive(x[:-1], y[:-1]) + x[-1]
    
    lcs1 = lcs_recursive(x[:-1], y)
    lcs2 = lcs_recursive(x, y[:-1])
    
    return lcs1 if len(lcs1) > len(lcs2) else lcs2

def lcs_memoized(x, y):
    memo = {}
    def helper(i, j):
        if i == 0 or j == 0:
            return ""
        if (i, j) in memo:
            return memo[(i, j)]
        if x[i - 1] == y[j - 1]:
            memo[(i, j)] = helper(i - 1, j - 1) + x[i - 1]
        else:
            lcs1 = helper(i - 1, j)
            lcs2 = helper(i, j - 1)
            memo[(i, j)] = lcs1 if len(lcs1) > len(lcs2) else lcs2

        return memo[(i, j)]

    return helper(len(x), len(y))

def lcs_dynamic(x, y):
    m, n = len(x), len(y)
    dp = [["" for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + x[i - 1]
            else:
                dp[i][j] = dp[i - 1][j] if len(dp[i - 1][j]) > len(dp[i][j - 1]) else dp[i][j - 1]

    return dp[m][n]

def main():
    x = "ABCBDAB"
    y = "BDCAB"

    print("Recursive LCS:", lcs_recursive(x, y))
    print("Memoized LCS:", lcs_memoized(x, y))
    print("Dynamic LCS:", lcs_dynamic(x, y))

if __name__ == "__main__":
    main()
