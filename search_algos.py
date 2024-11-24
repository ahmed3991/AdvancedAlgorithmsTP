import numpy as np

lenghts = [10, 100, 1000, 10000]

random_arrays = [np.random.randint(0, 10000, size=n).tolist() for n in lenghts]

sorted_arrays = [list(range(n)) for n in lenghts]


inverse_sorted_arrays = [list(range(n, 0, -1)) for n in lenghts]

nbr_experiments = 10

funcs = [selection_sort, bubble_sort, insertion_sort_shifting, insertion_sort_exchange]

results = []

for func in funcs:
    for length in lenghts:
        for arr in [random_arrays, sorted_arrays, inverse_sorted_arrays]:
            
            comparison_count_total = 0
            move_count_total = 0
            for _ in range(nbr_experiments):
                comparisons, moves = func(arr[length])
                comparison_count_total += comparisons
                move_count_total += moves
            
            avg_comparisons = comparison_count_total / nbr_experiments
            avg_moves = move_count_total / nbr_experiments
            results.append({
                "algorithm": func.__name__,
                "array_type": arr,
                "length": length,
                "average_comparisons": avg_comparisons,
                "average_moves": avg_moves
            })

for result in results:
    print(f"Algorithm: {result['algorithm']}, Array type: {result['array_type']}, "
          f"Length: {result['length']}, Avg Comparisons: {result['average_comparisons']}, "
          f"Avg Moves: {result['average_moves']}")
