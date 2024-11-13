import time
import random

def selection_sort(arr):
    comparisons = 0
    moves = 0
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
        moves += 1
    return comparisons, moves

def bubble_sort(arr):
    comparisons = 0
    moves = 0
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                moves += 1
                swapped = True
        if not swapped:
            break   
    return comparisons, moves

def insertion_sort_by_exchanges(arr):
    comparisons = 0
    moves = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]
            moves += 1
            j -= 1
        arr[j + 1] = key
        moves += 1
    return comparisons, moves

def insertion_sort_by_shifting(arr):
    comparisons = 0
    moves = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            j -= 1
        arr[j + 1] = key
        moves += 1
    return comparisons, moves

def measure_performance(sort_func, arr):
    start_time = time.time()
    comparisons, moves = sort_func(arr.copy())
    cpu_time = time.time() - start_time
    return comparisons, moves, cpu_time

sizes = [1000, 10000]
sort_types = ["random", "ascending", "descending"]
results = {}

for size in sizes:
    for sort_type in sort_types:
        if sort_type == "random":
            arr = [random.randint(1, 10000) for _ in range(size)]
        elif sort_type == "ascending":
            arr = list(range(size))
        else:  # descending
            arr = list(range(size, 0, -1))

        results[(size, sort_type)] = {
            "selection": measure_performance(selection_sort, arr),
            "bubble": measure_performance(bubble_sort, arr),
            "insertion_exchange": measure_performance(insertion_sort_by_exchanges, arr),
            "insertion_shift": measure_performance(insertion_sort_by_shifting, arr),
        }

for key, value in results.items():
    print(f"Size: {key[0]}, Type: {key[1]}")
    for algo, (comparisons, moves, cpu_time) in value.items():
        print(f"  {algo}: Comparisons: {comparisons}, Moves: {moves}, CPU Time: {cpu_time:.6f} seconds")