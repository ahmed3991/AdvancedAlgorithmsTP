## TODO: TP should be HERE
import random
import time


## TODO: Data Generation
r = int(input("Enter the range of data: "))
data = [random.randint(0, 10000) for i in range(r)]


## TODO: Sort Algorithms implementations
## TODO: Selection Sort is our task now
def selectionSort(data):
    comps = 0
    swaps = 0
    for i in range(len(data)):
        min=i
        for j in range(i + 1, len(data)):
            comps += 1
            if data[j] < data[min]:
                min=j
        if min!= i:
            data[i], data[min] = data[min], data[i]
            swaps += 1
    return comps, swaps

## TODO: Complete the code

def bubbleSort(data):
    comps = 0
    swaps = 0
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            comps += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                swaps += 1
    return comps, swaps

def insertionSortShifting(data,n):
    comps=0
    swaps=0

    for i in range(1, n):
        temp = data[i]
        j = i - 1

        while j >= 0 and data[j] > temp:
            comps+ 1
            data[j+1] = data[j]
            swaps += 1
            j -= 1
        data[j+1] = temp

        if j!= i-1:
            comps=1

    return comps ,swaps

def insertionSortExchange(data,n):
    comps=0
    swaps=0

    for i in range(1, n):
        j=i
        while j>0 and data[j]<data[j-1]:
            comps += 1
            data[j], data[j-1] = data[j-1], data[j]
            swaps+=1
            j-=1

        if j>0:
            comps+=1

    return comps, swaps


## TODO: make Benchmarks

def benchmarkSort(sort_function, data):
    start = time.time()
    comps, swaps = sort_function(data)
    end = time.time()
    return comps, swaps, end - start

print('Data before sorting:')
print(data[:20])

comps, swaps, duration = benchmarkSort(selectionSort, data.copy())
print("\nSelection Sort:")
print(f"Comparisons: {comps}, Swaps: {swaps}, Time: {duration:.5f} seconds")

comps, swaps, duration = benchmarkSort(bubbleSort, data.copy())
print("\nBubble Sort:")
print(f"Comparisons: {comps}, Swaps: {swaps}, Time: {duration:.5f} seconds")

comps, swaps, duration = benchmarkSort(insertionSortShifting, data.copy())
print("\nInsertion Sort (Shifting):")
print(f"Comparisons: {comps}, Swaps: {swaps}, Time: {duration:.5f} seconds")

comps, swaps, duration = benchmarkSort(insertionSortExchange, data.copy())
print("\nInsertion Sort (Exchange):")
print(f"Comparisons: {comps}, Swaps: {swaps}, Time: {duration:.5f} seconds")
