#TODO: put the code here
import pandas as pd
from tqdm import tqdm
import numpy as np
import sys
from pathlib import Path

# Add the parent directory to the system path
sys.path.append(str(Path(__file__).parent.parent))

from complexity.generator import StringGenerator
from complexity.profiler import TimeAndSpaceProfiler
from complexity.analyser import ComplexityAnalyzer

def compute_lcs_recursive(str1, str2):
    if not str1 or not str2:
        return ""
    if str1[-1] == str2[-1]:
        return compute_lcs_recursive(str1[:-1], str2[:-1]) + str1[-1]
    option1 = compute_lcs_recursive(str1[:-1], str2)
    option2 = compute_lcs_recursive(str1, str2[:-1])
    return option1 if len(option1) > len(option2) else option2

def compute_lcs_memoized(str1, str2, cache=None):
    if cache is None:
        cache = {}

    key = (len(str1), len(str2))
    if key in cache:
        return cache[key]

    if not str1 or not str2:
        result = ""
    elif str1[-1] == str2[-1]:
        result = compute_lcs_memoized(str1[:-1], str2[:-1], cache) + str1[-1]
    else:
        option1 = compute_lcs_memoized(str1[:-1], str2, cache)
        option2 = compute_lcs_memoized(str1, str2[:-1], cache)
        result = option1 if len(option1) > len(option2) else option2

    cache[key] = result
    return result

def compute_lcs_dynamic(str1, str2):
    rows, cols = len(str1), len(str2)
    dp_table = [["" for _ in range(cols + 1)] for _ in range(rows + 1)]

    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if str1[i - 1] == str2[j - 1]:
                dp_table[i][j] = dp_table[i - 1][j - 1] + str1[i - 1]
            else:
                dp_table[i][j] = dp_table[i - 1][j] if len(dp_table[i - 1][j]) > len(dp_table[i][j - 1]) else dp_table[i][j - 1]

    return dp_table[rows][cols]

# Initialize components
profiler = TimeAndSpaceProfiler()
generator = StringGenerator(alphabet=['A', 'B', 'C', 'D'], string_length=20)

# Prepare string pairs for experiments
lengths = [3, 5, 6, 8, 10, 13, 15, 20]
pair_list = [(generator.generate(size), generator.generate(size)) for size in lengths]

# Store results
experiment_data = []
print("Executing LCS algorithms...")

with tqdm(total=len(pair_list) * 3, desc="Processing pairs") as progress_bar:
    for str_a, str_b in pair_list:
        for method, implementation in zip(
            ["recursive", "memoized", "dynamic"],
            [compute_lcs_recursive, lambda x, y: compute_lcs_memoized(x, y), compute_lcs_dynamic]
        ):
            metrics = profiler.profile(implementation, str_a, str_b)
            experiment_data.append({
                'algorithm': method,
                'string1': str_a,
                'string2': str_b,
                **metrics
            })
            progress_bar.update(1)

print("\nEvaluating complexity...")

# Analyze algorithmic complexity
analyzer = ComplexityAnalyzer()
complexity_results = []

for method in ["recursive", "memoized", "dynamic"]:
    data_subset = [entry for entry in experiment_data if entry['algorithm'] == method]
    input_sizes = [len(entry['string1']) for entry in data_subset]
    times_taken = [entry['time'] for entry in data_subset]

    best_fit, complexity_model = analyzer.get_best_fit(np.array(input_sizes), np.array(times_taken))
    complexity_results.append({
        'algorithm': method,
        'complexity': best_fit
    })

print("\nSaving output files...")

# Save data to CSV
experiment_df = pd.DataFrame(experiment_data)
complexity_df = pd.DataFrame(complexity_results)

experiment_df.to_csv('lcs_experiment_results.csv', index=False)
complexity_df.to_csv('lcs_complexity_summary.csv', index=False)

print("\nOutput saved as 'lcs_experiment_results.csv' and 'lcs_complexity_summary.csv'")


print('Please use the complexity library')

