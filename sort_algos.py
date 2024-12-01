import time
import numpy as np
import random
import psutil
import matplotlib.pyplot as plt

def memory_usage():
    process = psutil.Process()
    return process.memory_info().rss / (1024 * 1024)

def selection_sort(array, length):
    count = 0

    start_time = time.time() 
    mem_before = memory_usage()
    
    for i in range(length):
        min_index = i 
        for j in range( i + 1, length): 
            if array[min_index] > array[j]:
               min_index = j
               count += 1

        array[i], array[j] = array[j], array[i]

    mem_after = memory_usage()
    end_time = time.time()

    print(f"Execution time: {end_time - start_time} s")
    print(f"CPU: {mem_after - mem_before} mb")
    print(f"Number of swaps: {count}")

    return array

def Bubble_sort(array, length):
    count = 0
    start_time = time.time()
    mem_before = memory_usage()

    for i in range(length):
        for j in range(0, length - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]  
                count += 1

    end_time = time.time()
    mem_after = memory_usage()

    print(f"Execution time : {end_time - start_time} s")
    print(f"Memory usage: {mem_after - mem_before:.2f} MB")
    print(f"Number of swaps: {count}")

    return array

def insertion_sort_by_shifting(arr, length):
    start_time = time.time()
    mem_before = memory_usage()
    count = 0 

    for i in range(1, length):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]  
            j -= 1
            count += 1

    mem_after = memory_usage()
    end_time = time.time()

    print(f"Execution time: {end_time - start_time} s")
    print(f"Memory usage: {mem_after - mem_before:.2f} MB")
    print(f"Number of swaps: {count}")

    return arr

def insertion_sort_by_exchanges(arr, length):
    start_time = time.time()
    mem_before = memory_usage()
    count = 0 

    for i in range(1, length):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]  # Swap elements
            count += 1
            j -= 1

    mem_after = memory_usage()
    end_time = time.time()

    print(f"Execution time: {end_time - start_time} s")
    print(f"Memory usage: {mem_after - mem_before:.2f} MB")
    print(f"Number of swaps: {count}")

    return arr

results = {}

algorithms = [selection_sort,Bubble_sort, insertion_sort_by_shifting, insertion_sort_by_exchanges]
lengths = [100, 1000, 10000]
# 1000000
orders = ["Random", "Sorted", "Descending"]

def generate_algorithms(algorithms, lengths, orders):
    for algo in algorithms:
        for l in lengths:
            for o in orders:
                print(f"\n\nAlgorithm: {algo.__name__}, Length: {l}, Order: {o} ")
                
                if o == "Random":
                    arr = [random.randint(0, 10000) for _ in range(l)]
                elif o == "Sorted":
                    arr = list(range(l))
                else: 
                    arr = list(range(l, 0, -1))
                
                algo(arr, l)

generate_algorithms(algorithms, lengths, orders)