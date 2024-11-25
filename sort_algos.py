## TODO: TP should be HERE


## TODO: Data Generation
import numpy as np

lenghts =[10,100,1000,10000]

# TODO : Use numpy
random_arrays = [np.random.randint(0, 100, size=l) for l in lenghts]
# TODO : Use range
sorted_arrays = [list(range(l)) for l in lenghts]
# TODO : Use range
inverse_sorted_arrays = [list(range(l, 0, -1)) for l in lenghts]

nbr_experiments = 10
# Print a summary
print("Random arrays:", [len(arr) for arr in random_arrays])
print("Sorted arrays:", [len(arr) for arr in sorted_arrays])
print("Inverse sorted arrays:", [len(arr) for arr in inverse_sorted_arrays])

def selection_sort(arr):
    comparison_count = 0
    move_count = 0
    arr = arr.copy()

    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            comparison_count += 1
            if arr[j] < arr[min_index]:
                min_index = j
        comparison_count += 1
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            move_count += 1

    return comparison_count, move_count

## TODO: Complete the code

def bubble_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return  comparisons, swaps


def insertion_sort_shifting(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]  # Shift
            swaps += 1
            j -= 1
        arr[j + 1] = key

        if j != i - 1:
            comparisons += 1

    return  comparisons, swaps
def insertion_sort_exchange(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)

    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            comparisons += 1
            arr[j], arr[j - 1] = arr[j - 1], arr[j]  # Swap
            swaps += 1
            j -= 1

        if j > 0:
            comparisons += 1

    return  comparisons, swaps



funcs = [selection_sort, bubble_sort,insertion_sort_shifting,insertion_sort_exchange]

results = []
 
# TODO: Complete the benchmark code
for length, random_arr, sorted_arr, inv_sorted_arr in zip(lenghts, random_arrays, sorted_arrays, inverse_sorted_arrays):
    print(f"\nBenchmarking for array size: {length}")

    for func in funcs:
        total_comparisons_random = 0
        total_swaps_random = 0
        total_comparisons_sorted = 0
        total_swaps_sorted = 0
        total_comparisons_inverse = 0
        total_swaps_inverse = 0

        for arr, comparison_total, swaps_total in [(random_arr, total_comparisons_random, total_swaps_random),
                                                  (sorted_arr, total_comparisons_sorted, total_swaps_sorted),
                                                  (inv_sorted_arr, total_comparisons_inverse, total_swaps_inverse)]:
            for _ in range(nbr_experiments):
                arr_copy = arr.copy()
                comparisons, swaps = func(arr_copy)
                comparison_total += comparisons
                swaps_total += swaps

        avg_comparisons_random = total_comparisons_random / nbr_experiments
        avg_swaps_random = total_swaps_random / nbr_experiments

        avg_comparisons_sorted = total_comparisons_sorted / nbr_experiments
        avg_swaps_sorted = total_swaps_sorted / nbr_experiments

        avg_comparisons_inverse = total_comparisons_inverse / nbr_experiments
        avg_swaps_inverse = total_swaps_inverse / nbr_experiments

        results.append({
            'Algorithm': func.__name__,
            'Array Size': length,
            'Type': 'Random',
            'Comparisons': avg_comparisons_random,
            'Swaps': avg_swaps_random
        })
        results.append({
            'Algorithm': func.__name__,
            'Array Size': length,
            'Type': 'Sorted',
            'Comparisons': avg_comparisons_sorted,
            'Swaps': avg_swaps_sorted
        })
        results.append({
            'Algorithm': func.__name__,
            'Array Size': length,
            'Type': 'Inverse Sorted',
            'Comparisons': avg_comparisons_inverse,
            'Swaps': avg_swaps_inverse
        })

        print(f"{func.__name__} - Random: {avg_comparisons_random:.2f} comparisons, {avg_swaps_random:.2f} swaps")
        print(f"{func.__name__} - Sorted: {avg_comparisons_sorted:.2f} comparisons, {avg_swaps_sorted:.2f} swaps")
        print(f"{func.__name__} - Inverse Sorted: {avg_comparisons_inverse:.2f} comparisons, {avg_swaps_inverse:.2f} swaps")

print("\nFinal Results:")
for result in results:
    print(result)