import numpy as np

# TODO: Data Generation
lenghts = [10, 100, 1000, 10000]

# TODO: Use numpy
random_arrays = []
# TODO: Use range
sorted_arrays = []
# TODO: Use range
inverse_sorted_arrays = []

# Generate arrays
for length in lenghts:
    random_arrays.append(np.random.randint(0, 10000, size=length))  # Random arrays
    sorted_arrays.append(np.arange(length))  # Sorted arrays
    inverse_sorted_arrays.append(np.arange(length-1, -1, -1))  # Inverse sorted arrays

nbr_experiments = 10

# Benchmark function
def benchmark(sorting_func, arrays, func_name):
    comparison_results = []
    move_results = []
    
    for arr in arrays:
        comparisons, moves = sorting_func(arr)
        comparison_results.append(comparisons)
        move_results.append(moves)
    
    avg_comparisons = np.mean(comparison_results)
    avg_moves = np.mean(move_results)
    print(f"{func_name} -> Avg Comparisons: {avg_comparisons}, Avg Moves: {avg_moves}")
    
    return avg_comparisons, avg_moves

# List of sorting functions
funcs = [selection_sort, bubble_sort, insertion_sort_shifting, insertion_sort_exchange]
func_names = ['Selection Sort', 'Bubble Sort', 'Insertion Sort Shifting', 'Insertion Sort Exchange']

# Run benchmarks
for func, name in zip(funcs, func_names):
    print(f"Benchmarking {name}:")
    print("Random arrays:")
    benchmark(func, random_arrays, name)
    print("Sorted arrays:")
    benchmark(func, sorted_arrays, name)
    print("Inverse sorted arrays:")
    benchmark(func, inverse_sorted_arrays, name)
    print("-" * 50)
