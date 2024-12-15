#TODO: put the code here
import random
import time
import csv
from memory_profiler import memory_usage

print('Please use the complexity library')


def lcs_recursive(X, Y, i, j):
    if i == 0 or j == 0:
        return 0
    if X[i - 1] == Y[j - 1]:
        return 1 + lcs_recursive(X, Y, i - 1, j - 1)
    else:
        return max(lcs_recursive(X, Y, i - 1, j), lcs_recursive(X, Y, i, j - 1))

def lcs_recursive_memo(X, Y, i, j, memo):
    if i == 0 or j == 0:
        return 0
    if (i, j) in memo:
        return memo[(i, j)]
    if X[i - 1] == Y[j - 1]:
        memo[(i, j)] = 1 + lcs_recursive_memo(X, Y, i - 1, j - 1, memo)
    else:
        memo[(i, j)] = max(lcs_recursive_memo(X, Y, i - 1, j, memo), lcs_recursive_memo(X, Y, i, j - 1, memo))
    return memo[(i, j)]

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

class StringGenerator:
    def __init__(self, alphabet=['A', 'B', 'C']):
        self.alphabet = alphabet

    def generate(self, size: int) -> str:
        return ''.join(random.choice(self.alphabet) for _ in range(size))

    def generate_pair(self, size1: int, size2: int) -> tuple:
        return self.generate(size1), self.generate(size2)

def measure_performance(lcs_func, *args):
    try:
        start_time = time.time()
        mem_usage = memory_usage((lcs_func, args))
        end_time = time.time()
        return {
            'time': end_time - start_time,
            'memory': max(mem_usage) - min(mem_usage)
        }
    except Exception as e:
        print(f"Error during performance measurement: {e}")
        return {'time': None, 'memory': None}

def write_to_csv(data, filename="lcs_performance_results.csv"):
    header = ['Method', 'Time (seconds)', 'Memory Usage (MB)']
    try:
        with open(filename, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(header)
            writer.writerows(data)
        print(f"Results saved to {filename}")
    except IOError as e:
        print(f"Failed to write results to {filename}: {e}")

def main():
    gen = StringGenerator(['A', 'B', 'C', 'D', 'E'])
    X, Y = gen.generate(20), gen.generate(15)
    results = []
    perf_rec = measure_performance(lcs_recursive, X, Y, len(X), len(Y))
    results.append(['Recursive (No Memo)', perf_rec['time'], perf_rec['memory']])
    memo = {}
    perf_rec_memo = measure_performance(lcs_recursive_memo, X, Y, len(X), len(Y), memo)
    results.append(['Recursive (With Memo)', perf_rec_memo['time'], perf_rec_memo['memory']])
    perf_dp = measure_performance(lcs_dp, X, Y)
    results.append(['Dynamic Programming', perf_dp['time'], perf_dp['memory']])
    write_to_csv(results)

if __name__ == "__main__":
    main()