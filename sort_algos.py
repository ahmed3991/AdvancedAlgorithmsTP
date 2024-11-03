from complexity import time_and_space_profiler
from tqdm import tqdm , trange
import numpy as np
import pandas as pd



## Data Generation
np.random.seed(42)
tests = []
lengths = np.array(range(100, 1000, 200))  
tests_per_length = 3    

for length in lengths:
        for _ in range(tests_per_length):
            val = np.random.randint(1, 4 * length, size=length)
            test = (length, val)
            tests.append(test)



# Sort Algorithms implementations

##selection_sort

@time_and_space_profiler
def selection_sort(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)
    
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_index]:
                min_index = j
        
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            swaps += 1
    
    return  comparisons, swaps

##bubble_sort

@time_and_space_profiler
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

##time_and_space_profiler

@time_and_space_profiler
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

##insertion_sort_exchange

@time_and_space_profiler
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

##Convert To Data Frame

funcs = [selection_sort, bubble_sort, insertion_sort_shifting, insertion_sort_exchange]

results = []
for i, (length, val) in tqdm(enumerate(tests), ncols=len(tests)):
    for func in funcs:
        func_name, (comparisons, swaps), elapsed_time, mem_used = func(val)  
        results.append((i, func_name, len(val), comparisons, swaps, elapsed_time, mem_used))

df = pd.DataFrame(results, columns=['id_test', 'function_name', 'array_length', 'comparison', 'Swaps', 'time', 'space'])

print(df)
df.to_csv('results.csv', index=False)