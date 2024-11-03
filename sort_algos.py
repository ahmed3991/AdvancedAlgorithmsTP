from complexity import time_and_space_profiler
from tqdm import tqdm , trange
import numpy as np
import pandas as pd


np.random.seed(42)

tests = []

lenghts = [1000,10000,100000]

tests_per_length = 3


for length in lenghts:
    for _ in range(tests_per_length):

        table = np.sort(np.random.randint(1,4*length,size=length))

        target = np.random.randint(1,4*length) 

        test = (length, table)

        tests.append(test)

#functions

@time_and_space_profiler
def selection_sort(T):
    i=0
    index_min=0
    j=0
    comparisons=0
    while(i<(len(T)-1)):
        index_min=i
        j=i+1
        while(j<len(T)):
            if(T[j]<T[index_min]):
                comparisons+=1
                index_min=j
            j+=1
        swap(T,i,index_min)
        i+=1
    return comparisons

def swap(T,a,b):
    T[a], T[b] = T[b], T[a]

@time_and_space_profiler
def bubble_sort(T):
    n = len(T)
    comparisons=0
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if T[j] > T[j+1]:
                comparisons+=1
                T[j], T[j+1] = T[j+1], T[j]
                swapped = True
        if (swapped == False):
            break
    return comparisons

@time_and_space_profiler
def insertion_sort_swap(T):
    comparisons=0
    N = len(T)
     
    for i in range(1,N):
        j = i
 
        while (j > 0 and T[j] < T[j - 1]) :
            comparisons+=1
            temp = T[j]
            T[j] = T[j - 1]
            T[j-1] = temp

            j -= 1
    return comparisons
    
@time_and_space_profiler
def insertion_sort_shift(T):
    comparisons=0

    for i in range(1, len(T)):
        key = T[i]
        j = i - 1

        while (j >= 0 and key < T[j]):
            comparisons+=1
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key

funcs = [selection_sort,bubble_sort,insertion_sort_swap,insertion_sort_shift]

results = []

for i , (length, table) in tqdm(enumerate(tests),ncols=len(tests)):
    
    for func in funcs:

        func_name,comparisons,T, S = func(table)

        results.append((i,func_name,length,comparisons,T,S))

df = pd.DataFrame(results, columns=['id_test','function_name','array_length','comparisons','time','space'])

print(df)

df.to_csv('results.csv', index=False)
