import numpy as np

# TODO: Data Generation
lengths = [10, 100, 1000, 10000]

# Generate random arrays using numpy
random_arrays = [np.random.randint(1, 1000, size=l).tolist() for l in lengths]

# Generate sorted arrays using range
sorted_arrays = [list(range(1, l + 1)) for l in lengths]

# Generate inverse sorted arrays using range
inverse_sorted_arrays = [list(range(l, 0, -1)) for l in lengths]

nbr_experiments = 10


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

    return comparisons, swaps


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

    return comparisons, swaps


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

    return comparisons, swaps


funcs = [selection_sort, bubble_sort, insertion_sort_shifting, insertion_sort_exchange]

results = []

# TODO: Complete the benchmark code
for func in funcs:
    func_name = func.__name__
    for length, random_array, sorted_array, inverse_sorted_array in zip(lengths, random_arrays, sorted_arrays, inverse_sorted_arrays):
        comparisons_random, swaps_random = 0, 0
        comparisons_sorted, swaps_sorted = 0, 0
        comparisons_inverse, swaps_inverse = 0, 0

        for _ in range(nbr_experiments):
            # Random arr
            cmp, swp = func(random_array)
            comparisons_random += cmp
            swaps_random += swp

            # Sorted arr
            cmp, swp = func(sorted_array)
            comparisons_sorted += cmp
            swaps_sorted += swp

            # Inverse sorted arr
            cmp, swp = func(inverse_sorted_array)
            comparisons_inverse += cmp
            swaps_inverse += swp

        # Average results
        comparisons_random /= nbr_experiments
        swaps_random /= nbr_experiments
        comparisons_sorted /= nbr_experiments
        swaps_sorted /= nbr_experiments
        comparisons_inverse /= nbr_experiments
        swaps_inverse /= nbr_experiments

        # Store results
        results.append({
            "Function": func_name,
            "Length": length,
            "Array Type": "Random",
            "Comparisons": comparisons_random,
            "Swaps": swaps_random
        })
        results.append({
            "Function": func_name,
            "Length": length,
            "Array Type": "Sorted",
            "Comparisons": comparisons_sorted,
            "Swaps": swaps_sorted
        })
        results.append({
            "Function": func_name,
            "Length": length,
            "Array Type": "Inverse Sorted",
            "Comparisons": comparisons_inverse,
            "Swaps": swaps_inverse
        })


for result in results:
    print(result)
