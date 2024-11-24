import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

 ## TODO: TP should be HERE


## TODO: Data Generation

lengths =[10,100,1000,10000]

# TODO : Use numpy
random_arrays= [np.random.randint(0, 10000, size=l).tolist() for l in lengths ]
# TODO : Use range
sorted_arrays= [list(range(l)) for l in lengths ]
# TODO : Use range
inverse_sorted_arrays = [list(range(l, 0, -1)) for l in lengths ]

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
for func in funcs: 
    print(f"Testing {func.name}") 
    for l, (rand_arr, sorted_arr, inv_sorted_arr) in enumerate(zip(random_arrays, sorted_arrays, inverse_sorted_arrays)): 
        print(f"Array length: {lengths[l]}") 
        rand_comparisons = 0 
        rand_swaps = 0 
 
        sorted_comparisons = 0 
        sorted_swaps = 0 
 
        inv_comparisons = 0 
        inv_swaps = 0 
 
        for _ in range(nbr_experiments): 
            comp, swap = func(rand_arr.copy()) 
            rand_comparisons += comp 
            rand_swaps += swap 
 
        comp, swap = func(sorted_arr.copy()) 
        sorted_comparisons += comp 
        sorted_swaps += swap 
 
        comp, swap = func(inv_sorted_arr.copy()) 
        inv_comparisons += comp 
        inv_swaps += swap 
 
        results.append({ 
            "algorithm": func.name, 
            "array_length": lengths[l], 
            "random_comparisons": rand_comparisons / nbr_experiments, 
            "random_swaps": rand_swaps / nbr_experiments, 
            "sorted_comparisons": sorted_comparisons, 
            "sorted_swaps": sorted_swaps, 
            "inverse_comparisons": inv_comparisons, 
            "inverse_swaps": inv_swaps 
        }) 
 
import pandas as pd 
df = pd.DataFrame(results) 
print(df) 
 
array_lengths = list(set([result['array_length'] for result in results])) 
algorithms = list(set([result['algorithm'] for result in results])) 
 
plt.figure(figsize=(10, 6)) 
for algo in algorithms: 
    comparisons = [ 
        result['random_comparisons'] 
        for result in results if result['algorithm'] == algo 
    ] 
    plt.plot(array_lengths, comparisons, label=f"{algo} (Comparisons)", marker='o') 
 
plt.title('Comparisons vs Array Lengths') 
plt.xlabel('Array Length') 
plt.ylabel('Num')






