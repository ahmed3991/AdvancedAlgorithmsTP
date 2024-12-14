import random
import time
import psutil
import matplotlib.pyplot as plt

# Memory usage function
def memory_usage():
    process = psutil.Process()
    return process.memory_info().rss

# Recursive LCS without memoization
def lcs_recursive_without_memo(x, y, i, j):
    if i == 0 or j == 0:
        return 0
    if x[i - 1] == y[j - 1]:
        return 1 + lcs_recursive_without_memo(x, y, i - 1, j - 1)
    else:
        return max(lcs_recursive_without_memo(x, y, i - 1, j), lcs_recursive_without_memo(x, y, i, j - 1))

# Recursive LCS with memoization
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

# Dynamic Programming LCS
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

# String generator class
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

# Plot results
def plot_results(sizes, times, memories):
    plt.figure(figsize=(12, 6))

    # Plotting execution time
    plt.subplot(1, 2, 1)
    for method, time_data in times.items():
        plt.plot(sizes, time_data, label=method, marker='o')
    plt.title("Execution Time Comparison")
    plt.xlabel("Input Size (Length of Strings)")
    plt.ylabel("Time (seconds)")
    plt.legend()

    # Plotting memory usage
    plt.subplot(1, 2, 2)
    for method, memory_data in memories.items():
        plt.plot(sizes, memory_data, label=method, marker='o')
    plt.title("Memory Usage Comparison")
    plt.xlabel("Input Size (Length of Strings)")
    plt.ylabel("Memory (bytes)")
    plt.legend()

    plt.tight_layout()
    plt.show()

# Compare memory and plot
def compare_memory_with_plot():
    generator = StringGenerator(['A', 'B', 'C'])
    sizes = list(range(5, 20, 2))  # Input sizes: 5, 7, 9, ..., 19

    times = {
        "Recursive without Memoization": [],
        "Recursive with Memoization": [],
        "Dynamic Programming": []
    }

    memories = {
        "Recursive without Memoization": [],
        "Recursive with Memoization": [],
        "Dynamic Programming": []
    }

    for size in sizes:
        x, y = generator.generate_pair(size, size)

        # Measure Recursive without Memoization
        start_time = time.time()
        lcs_recursive_without_memo(x, y, len(x), len(y))
        elapsed_time = time.time() - start_time
        memory_used = memory_usage()
        times["Recursive without Memoization"].append(elapsed_time)
        memories["Recursive without Memoization"].append(memory_used)

        # Measure Recursive with Memoization
        start_time = time.time()
        lcs_recursive_with_memo(x, y, len(x), len(y), {})
        elapsed_time = time.time() - start_time
        memory_used = memory_usage()
        times["Recursive with Memoization"].append(elapsed_time)
        memories["Recursive with Memoization"].append(memory_used)

        # Measure Dynamic Programming
        start_time = time.time()
        lcs_dynamic(x, y)
        elapsed_time = time.time() - start_time
        memory_used = memory_usage()
        times["Dynamic Programming"].append(elapsed_time)
        memories["Dynamic Programming"].append(memory_used)

    # Normalize data to make curves appear as straight lines
    for method in times:
        times[method] = [t * 1000 for t in times[method]]  # Scale time to milliseconds
    for method in memories:
        memories[method] = [m // 1000 for m in memories[method]]  # Scale memory to kilobytes

    plot_results(sizes, times, memories)

# Main
if __name__ == "__main__":
    compare_memory_with_plot()
