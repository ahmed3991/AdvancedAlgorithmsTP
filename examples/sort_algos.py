# import pandas as pd
# from tqdm import tqdm
# import sys
# from pathlib import Path

# # Add parent directory to path
# sys.path.append(str(Path(__file__).parent.parent))

# from complexity import (
#     DataGeneratorFactory,
#     RandomDataGenerator,
#     LinearDataGenerator,
#     TimeAndSpaceProfiler,
#     ComplexityAnalyzer,
#     ComplexityVisualizer,
#     ComplexityDashboardVisualizer
# )

# from collections import namedtuple

# ## Data Generation

# # Set up data generators
# factory = DataGeneratorFactory()
# factory.register_generator("random", RandomDataGenerator(0, 100))
# factory.register_generator("sorted", LinearDataGenerator())

# # Data generation
# lengths = [10, 100, 1000]
# nbr_experiments = 3

# # Generate arrays for each length and experiment
# random_arrays = [
#     [factory.get_generator("random").generate(size) for _ in range(nbr_experiments)]
#     for size in lengths
# ]

# sorted_arrays = [
#     [factory.get_generator("sorted").generate(size) for _ in range(nbr_experiments)]
#     for size in lengths
# ]

# inverse_sorted_arrays = [
#     [list(reversed(factory.get_generator("sorted").generate(size))) for _ in range(nbr_experiments)]
#     for size in lengths
# ]

# Metrics = namedtuple('Metrics', ['n', 'comparison_count', 'move_count'])

# # Sorting algorithms
# def selection_sort(arr):
#     comparisons = 0
#     move_count = 0
#     n = len(arr)

#     for i in range(len(arr)):
#         min_index = i
#         for j in range(i + 1, len(arr)):
#             comparisons += 1
#             if arr[j] < arr[min_index]:
#                 min_index = j
#         if min_index != i:
#             arr[i], arr[min_index] = arr[min_index], arr[i]
#             move_count += 1

#     return Metrics(n, comparisons, move_count)

# def bubble_sort(arr):
#     comparisons = 0
#     move_count = 0
#     n = len(arr)

#     for i in range(n):
#         swapped = False
#         for j in range(0, n - i - 1):
#             comparisons += 1
#             if arr[j] > arr[j + 1]:
#                 arr[j], arr[j + 1] = arr[j + 1], arr[j]
#                 move_count += 1
#                 swapped = True
        
#         if not swapped:
#             break

#     return Metrics(n, comparisons, move_count)

# def insertion_sort_shifting(arr):
#     comparisons = 0
#     move_count = 0
#     n = len(arr)

#     for i in range(1, n):
#         key = arr[i]
#         j = i - 1
#         while j >= 0:
#             comparisons += 1
#             if arr[j] > key:
#                 arr[j + 1] = arr[j]
#                 move_count += 1
#                 j -= 1
#             else:
#                 break
#         arr[j + 1] = key

#     return Metrics(n, comparisons, move_count)

# def insertion_sort_exchange(arr):
#     comparisons = 0
#     move_count = 0
#     n = len(arr)

#     for i in range(1, n):
#         j = i
#         while j > 0 and arr[j] < arr[j - 1]:
#             comparisons += 1
#             arr[j], arr[j - 1] = arr[j - 1], arr[j]
#             move_count += 1
#             j -= 1
#         if j > 0:
#             comparisons += 1

#     return Metrics(n, comparisons, move_count)

# # Algorithms to benchmark
# funcs = [
#     selection_sort,
#     bubble_sort,
#     insertion_sort_shifting,
#     insertion_sort_exchange,
# ]

# # Benchmarking
# profiler = TimeAndSpaceProfiler()
# results = []

# # Create a tqdm progress bar for tracking the experiments
# total_iterations = len(funcs) * len(lengths) * nbr_experiments * 3  # 3 for random, sorted, inverse_sorted
# with tqdm(total=total_iterations, desc="Benchmarking", unit="experiment") as pbar:
#     for func in funcs:
#         for size, random_experiments, sorted_experiments, inverse_sorted_experiments in zip(
#             lengths, random_arrays, sorted_arrays, inverse_sorted_arrays
#         ):
#             for experiment_idx in range(nbr_experiments):
#                 for data, label in [
#                     (random_experiments[experiment_idx], "random"),
#                     (sorted_experiments[experiment_idx], "sorted"),
#                     (inverse_sorted_experiments[experiment_idx], "inverse_sorted"),
#                 ]:
#                     # Run and profile
#                     logs = profiler.profile(func, data)
#                     logs.update({
#                         "algorithm": func.__name__,
#                         "data_type": label,
#                         "size": size,
#                         "experiment": experiment_idx + 1,
#                     })
#                     results.append(logs)

#                     # Update tqdm progress bar with custom message
#                     pbar.set_postfix({
#                         'algorithm': func.__name__,
#                         'data_type': label,
#                         'size': size,
#                         'experiment': experiment_idx + 1,
#                     })
#                     pbar.update(1)

# # Convert results to a pandas DataFrame
# df = pd.DataFrame(results)

# # Write the DataFrame to a CSV file
# csv_filename = "benchmark_results.csv"
# df.to_csv(csv_filename, index=False)

# # Data Preprocessing: Convert time and memory columns to numeric
# df['time'] = pd.to_numeric(df['time'], errors='coerce')
# df['memory'] = pd.to_numeric(df['memory'], errors='coerce')

# # Grouping by algorithm, data_type, and size
# grouped = df.groupby(['algorithm', 'data_type', 'size']).agg({
#     'time': 'mean',
#     'memory': 'mean',
#     'comparison_count': 'mean',
#     'move_count': 'mean'
# }).reset_index()

# # Save both raw and grouped results for later analysis
# df.to_csv('sort_results_raw.csv', index=False)
# grouped.to_csv('sort_results_grouped.csv', index=False)

# print("\nResults have been saved to 'sort_results_raw.csv' and 'sort_results_grouped.csv'")





import pandas as pd
from tqdm import tqdm

import sys
from pathlib import Path

# Add parent directory to path
sys.path.append(str(Path(__file__).parent.parent))

from complexity import (
    DataGeneratorFactory,
    RandomDataGenerator,
    LinearDataGenerator,
    TimeAndSpaceProfiler,
    ComplexityAnalyzer,
    ComplexityVisualizer,
    ComplexityDashboardVisualizer
)

from collections import namedtuple

# Set up data generators
factory = DataGeneratorFactory()
factory.register_generator("random", RandomDataGenerator(0, 100))
factory.register_generator("sorted", LinearDataGenerator())

# Data generation
lengths = [10, 100, 1000]
nbr_experiments = 3

# Generate arrays for each length and experiment
random_arrays = [
    [factory.get_generator("random").generate(size) for _ in range(nbr_experiments)]
    for size in lengths
]

sorted_arrays = [
    [factory.get_generator("sorted").generate(size) for _ in range(nbr_experiments)]
    for size in lengths
]

inverse_sorted_arrays = [
    [list(reversed(factory.get_generator("sorted").generate(size))) for _ in range(nbr_experiments)]
    for size in lengths
]

Metrics = namedtuple('Metrics', ['n','comparison_count', 'move_count'])

def selection_sort(arr):
    comparisons = 0
    move_count = 0
    n = len(arr)

    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            move_count += 1

    return Metrics(n, comparisons, move_count)

def bubble_sort(arr):
    comparisons = 0
    move_count = 0
    n = len(arr)

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                move_count += 1
                swapped = True
        
        if not swapped:
            break

    return Metrics(n, comparisons, move_count)

def insertion_sort_shifting(arr):
    comparisons = 0
    move_count = 0
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                move_count += 1
                j -= 1
            else:
                break

        arr[j + 1] = key

    return Metrics(n, comparisons, move_count)

def insertion_sort_exchange(arr):
    comparisons = 0
    move_count = 0
    n = len(arr)

    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            comparisons += 1
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            move_count += 1
            j -= 1

        if j > 0:
            comparisons += 1

    return Metrics(n, comparisons, move_count)

# Algorithms to benchmark
funcs = [
    selection_sort,
    bubble_sort,
    insertion_sort_shifting,
    insertion_sort_exchange,
]

# Benchmarking
profiler = TimeAndSpaceProfiler()
results = []

# Create a tqdm progress bar for tracking the experiments
total_iterations = len(funcs) * len(lengths) * nbr_experiments * 3
with tqdm(total=total_iterations, desc="Benchmarking", unit="experiment") as pbar:

    for func in funcs:
        for size, random_experiments, sorted_experiments, inverse_sorted_experiments in zip(
            lengths, random_arrays, sorted_arrays, inverse_sorted_arrays
        ):
            for experiment_idx in range(nbr_experiments):
                for data, label in [
                    (random_experiments[experiment_idx], "random"),
                    (sorted_experiments[experiment_idx], "sorted"),
                    (inverse_sorted_experiments[experiment_idx], "inverse_sorted"),
                ]:
                    # Run and profile
                    logs = profiler.profile(func, data)
                    logs.update({
                        "algorithm": func.__name__,
                        "data_type": label,
                        "size": size,
                        "experiment": experiment_idx + 1,
                    })
                    results.append(logs)

                    # Update tqdm progress bar with custom message
                    pbar.set_postfix({
                        'algorithm': func.__name__,
                        'data_type': label,
                        'size': size,
                        'experiment': experiment_idx + 1,
                    })
                    pbar.update(1)

# Convert results to a pandas DataFrame
df = pd.DataFrame(results)

# Grouping by algorithm, data_type, and size
grouped = df.groupby(['algorithm', 'data_type', 'size']).agg({
    'time': 'mean',
    'memory': 'mean',
    'comparison_count': 'mean',
    'move_count': 'mean'
}).reset_index()

# Print the raw and grouped results in the terminal
print("\nRaw Results:")
print(df)

print("\nGrouped Results:")
print(grouped)
