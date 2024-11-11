import time
import numpy as np
import random
import psutil

def memory_usage():
    # Returns memory usage in MB
    process = psutil.Process()
    return process.memory_info().rss / (1024 * 1024)

#selection sort  
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



# sortedArray = selection_sort(array, length)
# sortedArray = selection_sort(sorted_array, length)
# sortedArray = selection_sort(descending_array, length)