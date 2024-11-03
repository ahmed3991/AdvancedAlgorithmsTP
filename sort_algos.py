from complexity import time_and_space_profiler
from tqdm import tqdm
import numpy as np
import pandas as pd

# Initialization logic
np.random.seed(42)
tests = []

# Define lengths up to 1,000,000 with steps of 10,000
lengths = np.arange(1000, 1000000, 10000)
tests_per_length = lambda length: 1 if length < 10000 else 2  # Increase tests for larger lengths

for length in lengths:
    # Generate a sorted array only once per length to save computation time
    val = np.sort(np.random.randint(1, 4 * length, size=length))
    for _ in range(tests_per_length(length)):
        target = np.random.randint(1, 4 * length)
        tests.append((length, val, target))

# Function definitions

@time_and_space_profiler
def sequential_search(val, target):
    for i in range(len(val)):
        if target == val[i]:  # Comparison
            return i + 1  # Early return
        elif target < val[i]:  # Stop if target is smaller
            break
    return len(val)

@time_and_space_profiler
def advanced_sequential_search(val, target):
    for i, item in enumerate(val):
        if target == item:  # Comparison
            return i + 1  # Early return
        elif target < item:  # Stop if target is smaller
            return i
    return len(val)

@time_and_space_profiler
def binary_search(val, target):
    start, end = 0, len(val) - 1
    iteration = 0

    while start <= end:
        half = (end + start) // 2
        if target == val[half]:
            return iteration + 1  # Count iterations only
        elif target < val[half]:
            end = half - 1
        else:
            start = half + 1
        iteration += 1
    return iteration

# Run tests
funcs = [sequential_search, advanced_sequential_search, binary_search]
results = []

for i, (length, val, target) in tqdm(enumerate(tests), total=len(tests), ncols=80):
    for func in funcs:
        func_name, comparison, T, S = func(val, target)
        results.append((i, func_name, length, comparison, T, S))

# Convert results to DataFrame and save
df = pd.DataFrame(results, columns=['id_test', 'function_name', 'array_length', 'comparison', 'time', 'space'])
print(df)
df.to_csv('results.csv', index=False)
