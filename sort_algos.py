## TODO: TP should be HERE
import random
import time 

## TODO: Data Generation
A=[random.randint(0,10000) for i in range(10000)]

## TODO: Sort Algorithms implementations

# Bubble_sort(array, lenght) :
def Bubble_Sort(array, length):
    for pass_num in range(length - 1, 0, -1):  
        for index in range(pass_num):  
            if array[index] > array[index + 1]:
                temp = array[index]
                array[index] = array[index + 1]
                array[index + 1] = temp
    return array

# Insertion_Sort _by_exchanges(array, lenght) :
def Insertion_Sort_By_Exchanges(array, length):
    for current_index in range(1, length): 
        position = current_index
        while position > 0 and array[position] < array[position - 1]:
            smaller = array[position]
            array[position] = array[position - 1]
            array[position - 1] = smaller
            position -= 1  
    return array

# Insertion_Sort _by_shifting(array, lenght) :
def Insertion_Sort_By_Shifting(array, length):
    for step in range(1, length): 
        current_value = array[step]
        index = step - 1
        while index >= 0 and array[index] > current_value:
            array[index + 1] = array[index] 
            index -= 1
        array[index + 1] = current_value
    return array

## TODO: Selection Sort is our task now
def sort_Selection(arr):
    for current_index in range(len(arr)):
        smallest_index = current_index
        for next_index in range(current_index + 1, len(arr)):
            if arr[next_index] < arr[smallest_index]:
                smallest_index = next_index
        arr[current_index], arr[smallest_index] = arr[smallest_index], arr[current_index]

## TODO: make Benchmarks
start_time = time.time() 
sort_Selection(A)     
end_time = time.time()   

print("Sorted array:")
for i in A:
    print(i, end=" ")

execution_time = end_time - start_time
print("\nSorting time:", execution_time, "seconds")