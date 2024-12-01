## TODO: TP should be HERE
import random
import numpy as np
import pandas as pd
from tqdm import tqdm
import time

## TODO: Data Generation
leng = [10,100,1000,10000]

randomArrs = [np.random.randint(0,100,size=n) for n in leng]
sortedArrs = [np.array(range(n)) for n in leng]
inverseArrs = [np.array(range(n-1,-1,-1)) for n in leng]



## TODO: Sort Algorithms implementations
## TODO: Selection Sort is our task now
def selectionSort(data):
    comps=0
    swaps=0
    n=len(data)
    for i in range(n):
        min=i
        for j in range(i+1,n):
            comps+=1
            if data[j] <data[min]:
                min=j
        if min!= i:
            data[i],data[min] =data[min],data[i]
            swaps+=1
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

def insertionShifting(data):
    comps=0
    swaps=0
    n = len(data)
    for i in range(1, n):
        temp = data[i]
        j = i - 1

        while j >= 0 and data[j] > temp:
            comps+ 1
            data[j+1] = data[j]
            swaps += 1
            j -= 1
        data[j+1] = temp


    return comps ,swaps

def insertionExchange(data):
    comps=0
    swaps=0
    n=len(data)
    for i in range(1,n):
        j=i
        while j>0 and data[j]<data[j-1]:
            comps += 1
            data[j], data[j-1] = data[j-1], data[j]
            swaps+=1
            j-=1


    return comps, swaps


def measurePerformance(implFunction, data):
    start_time = time.time()
    copy_data = data[:]
    sorted_data = implFunction(copy_data)
    end_time = time.time()
    execution_time = (end_time - start_time) * 1000
    return execution_time


def performExperiments():
    results = []
    tests = 5
    algos = [selectionSort, bubbleSort, insertionShifting, insertionExchange]

    for n, randomArr, sortedArr, inverseArr in tqdm(zip(leng, randomArrs, sortedArrs, inverseArrs), total=len(leng),
                                                    desc="Processing Experiments"):
        for algo in algos:
            for expType, data in [("Random", randomArr), ("Sorted", sortedArr), ("Inverse Sorted", inverseArr)]:
                comps, swaps = algo(data)
                exec_time = measurePerformance(algo, data)
                results.append({
                    "Function": algo.__name__,
                    "Array Type": expType,
                    "Array Length": n,
                    "Comparisons": comps,
                    "Swaps": swaps,
                    "Execution Time (ms)": exec_time
                })

    df_results = pd.DataFrame(results)
    print(df_results)
    df_results.to_csv("sorting_experiment_results.csv", index=False)


performExperiments()

## TODO: make Benchmarks
'''
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
'''