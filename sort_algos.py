import numpy as np
import matplotlib.pyplot as plt

lengths = [10, 100, 1000, 10000]

random_arrays = [np.random.randint(0, 100, size=l).tolist() for l in lengths]

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
            arr[j + 1] = arr[j] 
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
            arr[j], arr[j - 1] = arr[j - 1], arr[j]  
            swaps += 1
            j -= 1

        if j > 0:
            comparisons += 1

    return comparisons, swaps


funcs = [selection_sort, bubble_sort, insertion_sort_shifting, insertion_sort_exchange]
results = {func.__name__: {"Random": [], "Sorted": [], "Inverse Sorted": []} for func in funcs}

for func in funcs:
    for arr_type, arrays in zip(
        ["Random", "Sorted", "Inverse Sorted"], 
        [random_arrays, sorted_arrays, inverse_sorted_arrays]
    ):
        for arr in arrays:
            comparisons, swaps = func(arr)
            results[func.__name__][arr_type].append((len(arr), comparisons, swaps))

n_cols = 3
n_rows = (len(funcs) + n_cols - 1) // n_cols
fig, axes = plt.subplots(n_rows, n_cols, figsize=(15, 5 * n_rows))

axes = axes.flatten()

for i, func in enumerate(funcs):
    ax = axes[i]
    for arr_type in ["Random", "Sorted", "Inverse Sorted"]:
        lengths = [r[0] for r in results[func.__name__][arr_type]]
        comparisons = [r[1] for r in results[func.__name__][arr_type]]
        ax.plot(lengths, comparisons, label=f"{arr_type} Arrays")

    ax.set_title(f"{func.__name__} - Comparisons vs Array Length")
    ax.set_xlabel("Array Length")
    ax.set_ylabel("Number of Comparisons")
    ax.legend()

for j in range(len(funcs), len(axes)):
    fig.delaxes(axes[j])

plt.tight_layout()
plt.show()
