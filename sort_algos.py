import time
import numpy as np
# from memory_profiler import memory_usage
import random
import psutil

def memory_usage():
    # Returns memory usage in MB
    process = psutil.Process()
    return process.memory_info().rss / (1024 * 1024)



## Sort Algorithms implementations
# def selection_sort(array, length):
#     count = 0

#     start_time = time.time() 
#     mem_before = memory_usage()
    
#     for i in range(length):
#         min_index = i 
#         for j in range( i + 1, length): 
#             if array[min_index] > array[j]:
#                min_index = j
#                count += 1

#         array[i], array[j] = array[j], array[i]

#     mem_after = memory_usage()
#     end_time = time.time()

#     print(f"Execution time: {end_time - start_time} s")
#     print(f"CPU: {mem_after - mem_before} mb")
#     print(f"Number of swaps: {count}")

#     return array


def Bubble_sort(array,length):
    count = 0

    start_time = time.time()
    mem_before = memory_usage()

    for i in range(length):
        for j in range(0,length - i-1):
            if array[j] > array[j+1]:
                swap = array[j]
                array[j] = array[j+1]
                array[j+1] = swap
                count += 1

    
    end_time = time.time()
    mem_after = memory_usage()

    print(f"Execution time :{end_time - start_time} s")
    print(f"CPU :{mem_after }  " )
    print(f"Number of swaps: {count}")

    return array


def insertion_sort_by_shifting(arr,length):
    start_time = time.time() 
    mem_before = memory_usage()
    count = 0 

    for i in range(length-1):
        j = i
        while j >= 0 and arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1
            count += 1

    mem_after = memory_usage()
    end_time = time.time()

    print(f"Execution time: {end_time - start_time} s")
    print(f"CPU: {mem_after - mem_before} mb")
    print(f"Number of swaps: {count}")

    return arr


def insertion_sort_by_exchanges(arr,length):

    start_time = time.time() 
    mem_before = memory_usage()
    count = 0 

    for i in range(1, length):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]  
            count += 1  
            j -= 1

    mem_after = memory_usage()
    end_time = time.time()

    print(f"Execution time: {end_time - start_time} s")
    print(f"CPU: {mem_after - mem_before} mb")
    print(f"Number of swaps: {count}")

    return arr


length = 10000
array = [random.randint(0, 10000) for _ in range(length)] 
sorted_array = sorted(array)  
descending_array = sorted(array, reverse=True) 

# print("final array :",selection_sort(sorted_array, length))
# print("random array :")
# sortedArray = selection_sort(array, length)
# print("sorted array :")
# sortedArray = selection_sort(sorted_array, length)
# print("sorted reverse array :")
# sortedArray = selection_sort(descending_array, length)

# print("final array :",Bubble_sort(sorted_array, length))
# print("random array :")
# sortedArray = Bubble_sort(array, length)
# print("sorted array :")
# sortedArray = Bubble_sort(sorted_array, length)
# print("sorted reverse array :")
# sortedArray = Bubble_sort(descending_array, length)

# print("final array :",insertion_sort_by_shifting(sorted_array, length))
# print("random array :")
# sortedArray = insertion_sort_by_shifting(array, length)
# print("sorted array :")
# sortedArray = insertion_sort_by_shifting(sorted_array, length)
# print("sorted reverse array :")
# sortedArray = insertion_sort_by_shifting(descending_array, length)

# print("final array :",insertion_sort_by_exchanges(sorted_array, length))
print("random array :")
sortedArray = insertion_sort_by_exchanges(array, length)
print("sorted array :")
sortedArray = insertion_sort_by_exchanges(sorted_array, length)
print("sorted reverse array :")
sortedArray = insertion_sort_by_exchanges(descending_array, length)