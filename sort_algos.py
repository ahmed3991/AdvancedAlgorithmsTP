import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

lengths = [10, 100, 1000, 10000]
random_arrays = [np.random.randint(1, 100, size=n) for n in lengths]
sorted_arrays = [np.arange(1, n+1) for n in lengths]
inverse_sorted_arrays = [np.arange(n, 0, -1) for n in lengths]

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

funcs = {
    "Selection Sort": selection_sort,
    "Bubble Sort": bubble_sort,
    "Insertion Sort (Shifting)": insertion_sort_shifting,
    "Insertion Sort (Exchange)": insertion_sort_exchange
}

results = []

for arr_type, datasets in zip(["Random", "Sorted", "Reverse Sorted"],
                              [random_arrays, sorted_arrays, inverse_sorted_arrays]):
    for func_name, func in funcs.items():
        for n, dataset in zip(lengths, datasets):
            comp, swaps = 0, 0
            for _ in range(nbr_experiments):
                c, s = func(dataset)
                comp += c
                swaps += s
            results.append({
                "Algorithm": func_name,
                "Array Type": arr_type,
                "Array Length": n,
                "Avg Comparisons": comp / nbr_experiments,
                "Avg Swaps": swaps / nbr_experiments
            })

df = pd.DataFrame(results)

plt.figure(figsize=(12, 6))

for algo in df["Algorithm"].unique():
    algo_data = df[df["Algorithm"] == algo]
    plt.plot(algo_data["Array Length"], algo_data["Avg Comparisons"], label=f"{algo} (Comparisons)")

plt.title("Average Comparisons for Sorting Algorithms")
plt.xlabel("Array Length")
plt.ylabel("Average Comparisons")
plt.legend()
plt.grid(True)
plt.show()

plt.figure(figsize=(12, 6))
for algo in df["Algorithm"].unique():
    algo_data = df[df["Algorithm"] == algo]
    plt.plot(algo_data["Array Length"], algo_data["Avg Swaps"], label=f"{algo} (Swaps)")

plt.title("Average Swaps for Sorting Algorithms")
plt.xlabel("Array Length")
plt.ylabel("Average Swaps")
plt.legend()
plt.grid(True)
plt.show()
