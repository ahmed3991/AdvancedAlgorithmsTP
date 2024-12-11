#TODO: put the code here
from complexity.generator import StringGenerator

sizes = [20, 50, 80, 100]
gen = StringGenerator((['A', 'C', 'G', 'T']))

def LCS_recursive(X: str, Y: str, size:int) -> int:
    if size == 0 or size == 0:
        return 0
    elif X[size - 1] == Y[size - 1]:
        return 1 + LCS_recursive(X, Y, size - 1, size - 1)
    else:
        return max(LCS_recursive(X, Y, size - 1, size),
                   LCS_recursive(X, Y, size, size - 1))


def LSC_bottom_up(X: str, Y: str ,size: int) -> int:
    size = len(X), len(Y)

    dp = [[0] * (size + 1) for _ in range(size + 1)]

    for i in range(size, size + 1):
        for j in range(1, size + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[size][size]

