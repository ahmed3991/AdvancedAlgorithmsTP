ODO: put the code here
import csv
from tabulate import tabulate
import random
import time
import psutil

print('Please use the complexity library')
def memory_usage():
    process = psutil.Process()
    return process.memory_info().rss

def lcs_recursive_without_memo(x, y, i, j):
    if i == 0 or j == 0:
        return 0
    if x[i - 1] == y[j - 1]:
        return 1 + lcs_recursive_without_memo(x, y, i - 1, j - 1)
    else:
        return max(lcs_recursive_without_memo(x, y, i - 1, j), 
lcs_recursive_without_memo(x, y, i, j - 1))

def lcs_recursive_with_memo(x, y, i, j, memo):
    if i == 0 or j == 0:
        return 0
    if (i, j) in memo:
        return memo[(i, j)]
    if x[i - 1] == y[j - 1]:
        memo[(i, j)] = 1 + lcs_recursive_with_memo(x, y, i - 1, j - 1, 
memo)
    else:
        memo[(i, j)] = max(lcs_recursive_with_memo(x, y, i - 1, j, memo), 
lcs_recursive_with_memo(x, y, i, j - 1, memo))
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

    return dp[m][n]

class StringGenerator:
    def __init__(self, alphabet=['A', 'B', 'C']):
        self.alphabet = alphabet

    def generate(self, size: int = 1) -> str:
        return ''.join(random.choices(self.alphabet, k=size))

    def generate_pair(self, size1: int, size2: int, similar: bool = 
False):
        x = self.generate(size1)
        y = self.generate(size2)

        if similar:
            common_length = min(size1, size2) // 3
            common_part = ''.join(random.choices(self.alphabet, 
k=common_length))
            x = x[:size1 - common_length] + common_part
            y = y[:size2 - common_length] + common_part

        return x, y

def save_to_csv(results, filename="results.csv"):
    headers = ["Method", "Generated String", "Time", "Memory Usage", "Time 
Complexity (O)"]
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        for result in results:
            writer.writerow(result)
    print(f"Results saved to {filename}")

def compare_memory():
    generator = StringGenerator()

    x10 = generator.generate(10)
    x20 = generator.generate(20)
    y, z = generator.generate_pair(20, 20, similar=True)

    results = []


    start_time = time.time()
    lcs_recursive_without_memo(x10, y, len(x10), len(y))
    recursive_time = time.time() - start_time
    recursive_memory = memory_usage()
    results.append(["Recursive without Memoization", x10, 
f"{recursive_time:.6f} seconds", f"{recursive_memory} bytes", "O(2^n)"])


    start_time = time.time()
    memo = {}
    lcs_recursive_with_memo(x10, y, len(x10), len(y), memo)
    recursive_memo_time = time.time() - start_time
    recursive_memo_memory = memory_usage()
    results.append(["Recursive with Memoization", x10, 
f"{recursive_memo_time:.6f} seconds", f"{recursive_memo_memory} bytes", 
"O(n * m)"])


    start_time = time.time()
    lcs_dynamic(x10, y)
    dynamic_time = time.time() - start_time
    dynamic_memory = memory_usage()
    results.append(["Dynamic Programming", x10, f"{dynamic_time:.6f} 
seconds", f"{dynamic_memory} bytes", "O(n * m)"])


    start_time = time.time()
    lcs_recursive_without_memo(x20, y, len(x20), len(y))
    recursive_time = time.time() - start_time
    recursive_memory = memory_usage()
    results.append(["Recursive without Memoization", x20, 
f"{recursive_time:.6f} seconds", f"{recursive_memory} bytes", "O(2^n)"])

    start_time = time.time()
    memo = {}
    lcs_recursive_with_memo(x20, y, len(x20), len(y), memo)
    recursive_memo_time = time.time() - start_time
    recursive_memo_memory = memory_usage()
    results.append(["Recursive with Memoization", x20, 
f"{recursive_memo_time:.6f} seconds", f"{recursive_memo_memory} bytes", 
"O(n * m)"])

    start_time = time.time()
    lcs_dynamic(x20, y)
    dynamic_time = time.time() - start_time
    dynamic_memory = memory_usage()
    results.append(["Dynamic Programming", x20, f"{dynamic_time:.6f} 
seconds", f"{dynamic_memory} bytes", "O(n * m)"])

    save_to_csv(results)

if __name__ == "__main__":
    compare_memory()  
