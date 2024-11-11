## TODO: TP should be HERE
import random
import time


## TODO: Data Generation
r = int(input("the range of Data please: "))
data = [random.randint(0, 10000) for i in range(r)]


## TODO: Sort Algorithms implementations
## TODO: Selection Sort is our task now
def selectionSort(data, n):
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if data[j] < data[min]:
                min = j
        (data[i], data[min]) = (data[min], data[i])

## TODO: make Benchmarks
n = len(data)
print('The data before sorting is:\n')
print(data)
start = time.time()
selectionSort(data, n)
end = time.time()
print('The data after sorting is:\n')
print(data)
print(f"Time taken to sort the data: {end-start:.f} seconds")