import numpy as np

lengths = [10, 100, 1000, 10000]

random_arrays = [np.random.randint(0, 10000, size=l).tolist() for l in lengths]
sorted_arrays = [list(range(l)) for l in lengths]
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
            arr[j + 1] = arr[j]  # عملية التحريك
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
            arr[j], arr[j - 1] = arr[j - 1], arr[j]  # عملية التبديل
            swaps += 1
            j -= 1

        if j > 0:
            comparisons += 1

    return comparisons, swaps

# قائمة دوال الترتيب
funcs = [selection_sort, bubble_sort, insertion_sort_shifting, insertion_sort_exchange]

# تنفيذ الاختبارات
results = []

for func in funcs:
    for arr_type, arrays in [("Random", random_arrays), 
                             ("Sorted", sorted_arrays), 
                             ("Inverse Sorted", inverse_sorted_arrays)]:
        for l_idx, l in enumerate(lengths):
            avg_comparisons = 0
            avg_swaps = 0

            for _ in range(nbr_experiments):
                arr = arrays[l_idx]
                comparisons, swaps = func(arr)
                avg_comparisons += comparisons
                avg_swaps += swaps

            avg_comparisons /= nbr_experiments
            avg_swaps /= nbr_experiments
            results.append({
                "Algorithm": func.__name__,
                "Array Type": arr_type,
                "Array Length": l,
                "Avg Comparisons": avg_comparisons,
                "Avg Swaps": avg_swaps
            })

# طباعة النتائج
for result in results:
    print(result)

