import time
import random
import psutil

def memory_usage():
    # Returns memory usage in MB
    process = psutil.Process()
    return process.memory_info().rss / (1024 * 1024)


def Bubble_sort(array,length):
    start_time = time.time()
    mem_before = memory_usage()
    count = 0

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
    print(f"CPU: {mem_after - mem_before} mb")
    print(f"Number of swaps: {count}")

    return array


def insertion_sort_by_shifting(array,length):
    start_time = time.time() 
    mem_before = memory_usage()
    count = 0 

    for i in range(length-1):
        j = i
        while j >= 0 and array[j] > array[j+1]:
            array[j], array[j+1] = array[j+1], array[j]
            j -= 1
            count += 1

    mem_after = memory_usage()
    end_time = time.time()

    print(f"Execution time: {end_time - start_time} s")
    print(f"CPU: {mem_after - mem_before} mb")
    print(f"Number of swaps: {count}")

    return array


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

def namestr(obj, namespace):
    return [name for name in namespace if namespace[name] is obj][0]

length = 10000
randomArray = [random.randint(0, length) for _ in range(length)] 
sorted_array = sorted(randomArray)  
descending_array = sorted(randomArray, reverse=True) 

funcs = [Bubble_sort, insertion_sort_by_shifting,insertion_sort_by_exchanges]
arrays = [randomArray, sorted_array,descending_array]
for func in funcs:
    print(func.__name__ + ': ')
    for array in arrays:
        print(namestr(array, globals()) + ': ')
        func(array,length)