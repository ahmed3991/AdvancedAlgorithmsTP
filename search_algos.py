from complexity import time_and_space_profiler
from tqdm import tqdm
import numpy as np
import pandas as pd

# Initialization logic
# Generating 30 tests for arrays of lengths between 1000 and 10,000,000 with 5 tests per length
np.random.seed(42)

tests = []
lengths = np.array(range(1000, 10_000_000, 200_000))
tests_per_length = 5

for length in lengths:
    for _ in range(tests_per_length):
        # Generate a sorted array and a random target
        val = np.sort(np.random.randint(1, 4 * length, size=length))
        target = np.random.randint(1, 4 * length)
        tests.append((length, val, target))

# Function definitions

@time_and_space_profiler
def sequential_search(val, target):
    """Performs a simple sequential search."""
    for i in range(len(val)):
        if target == val[i]:  # Comparison
            return i + 1
    return len(val)

@time_and_space_profiler
def advanced_sequential_search(val, target):
    """Optimized sequential search that stops early when the target is less than the current element."""
    comparison = 0
    for i in range(len(val)):
        comparison += 2
        if target == val[i]:  # Match found
            comparison -= 1
            break
        elif target < val[i]:  # No need to search further
            break
    return comparison

@time_and_space_profiler
def binary_search(val, target):
    """Performs binary search."""
    start = 0
    end = len(val) - 1
    comparison = 1

    while start <= end:
        half = (end + start) // 2
        comparison += 2
        if target == val[half]:  # Match found
            comparison -= 1
            break
        elif target < val[half]:  # Search left
            end = half - 1
        else:  # Search right
            start = half + 1
        comparison += 1
    return comparison

# List of functions to test
funcs = [sequential_search, advanced_sequential_search, binary_search]

# Run tests and collect results
results = []
for i, (length, val, target) in tqdm(enumerate(tests), total=len(tests), desc="Testing progress"):
    for func in funcs:
        func_name, comparison, T, S = func(val, target)
        results.append((i, func_name, length, comparison, T, S))

# Convert results to a DataFrame
df = pd.DataFrame(results, columns=['id_test', 'function_name', 'array_length', 'comparison', 'time', 'space'])

# Output results
print(df)

# Save results to a CSV file
df.to_csv('results.csv', index=False)

