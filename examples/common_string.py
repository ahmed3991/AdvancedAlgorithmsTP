import random
import time
import psutil

def memory_usage():
    process = psutil.Process()
    return process.memory_info().rss

def lcs_recursive_without_memo(x, y, i, j):
    if i == 0 or j == 0:
        return 0
    if x[i - 1] == y[j - 1]:
        return 1 + lcs_recursive_without_memo(x, y, i - 1, j - 1)
    else:
        return max(lcs_recursive_without_memo(x, y, i - 1, j), lcs_recursive_without_memo(x, y, i, j - 1))

def lcs_recursive_with_memo(x, y, i, j, memo):
    if i == 0 or j == 0:
        return 0
    if (i, j) in memo:
        return memo[(i, j)]
    if x[i - 1] == y[j - 1]:
        memo[(i, j)] = 1 + lcs_recursive_with_memo(x, y, i - 1, j - 1, memo)
    else:
        memo[(i, j)] = max(lcs_recursive_with_memo(x, y, i - 1, j, memo), lcs_recursive_with_memo(x, y, i, j - 1, memo))
    return memo[(i, j)]

def lcs_dynamic(x, y):
    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            lcs.append(x[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return ''.join(reversed(lcs))

class StringGenerator:
    def __init__(self, alphabet=['A', 'B', 'C']):
        self.alphabet = alphabet

    def generate(self, size: int = 1) -> str:
        return ''.join(random.choices(self.alphabet, k=size))

    def generate_pair(self, size1: int, size2: int, similar: bool = False):
        x = self.generate(size1)
        y = self.generate(size2)

        if similar:
            common_length = min(size1, size2) // 3
            common_part = ''.join(random.choices(self.alphabet, k=common_length))
            x = x[:size1 - common_length] + common_part
            y = y[:size2 - common_length] + common_part

        return x, y

def compare_memory():
    generator = StringGenerator(['A', 'B', 'C'])

    x = generator.generate(10)
    y, z = generator.generate_pair(20, 20, similar=True)

    print(f"\nGenerated string x (10): {x}")
    print(f"Generated strings y and z (20, 20): {y}, {z}\n")

    for name, func in [("Recursive without Memoization", lcs_recursive_without_memo),
                       ("Recursive with Memoization", lambda x, y, i, j: lcs_recursive_with_memo(x, y, i, j, {})),
                       ("Dynamic Programming", lcs_dynamic)]:
        print(f"\n{name}:")

        start_time = time.time()
        func(x, y, len(x), len(y)) if "Recursive" in name else func(x, y)
        elapsed_time = time.time() - start_time

        print(f"Time: {elapsed_time:.6f} seconds")
        print(f"Memory Usage: {memory_usage()} bytes")

if __name__ == "__main__":
    compare_memory()
