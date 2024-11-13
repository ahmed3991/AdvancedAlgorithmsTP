## TODO: TP should be HERE
import random
import time

## TODO: Data Generation
r = int(input("enter N  =  "))
data = [random.randint(0, 100) for i in range(r)]

## TODO: Sort Algorithms implementations
## TODO: Selection Sort is our task now

def selectionSort(data, n):
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if data[j] < data[min_index]:
                min_index = j
        # Swap the found minimum element with the first element
        data[i], data[min_index] = data[min_index], data[i]

## TODO: Make Benchmarks
n = len(data)
print('the table unsort:\n')
print(data)
start = time.time()
selectionSort(data, n)
end = time.time()
print('\nThe table after sort:\n')
print(data)
print(f"\nTime of sorting: {end - start:} seconds")