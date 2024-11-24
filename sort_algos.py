import numpy as np

# TODO: Data Generation
lengths = [10, 100, 1000, 10000]

# إنشاء مصفوفات عشوائية باستخدام numpy
random_arrays = [np.random.randint(0, 100000, size=l).tolist() for l in lengths]

# إنشاء مصفوفات مرتبة باستخدام range
sorted_arrays = [list(range(l)) for l in lengths]

# إنشاء مصفوفات مرتبة عكسياً باستخدام range
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
    for arr_type, arrays in [("Random", random_arrays), 
                             ("Sorted", sorted_arrays), 
                             ("Inverse Sorted", inverse_sorted_arrays)]:
        for length, array in zip(lengths, arrays):
            total_comparisons = 0
            total_swaps = 0
            for _ in range(nbr_experiments):
                comp, swaps = func(array.copy())
                total_comparisons += comp
                total_swaps += swaps
            
            avg_comparisons = total_comparisons / nbr_experiments
            avg_swaps = total_swaps / nbr_experiments
            results.append({
                "Function": func_name,
                "Array Type": arr_type,
                "Length": length,
                "Avg Comparisons": avg_comparisons,
                "Avg Swaps": avg_swaps
            })

# طباعة النتائج
for result in results:
    print(result)
