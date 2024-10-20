from complexity import time_and_space_profiler
from tqdm import tqdm , trange
import numpy as np
import pandas as pd



# Inialization logic
# TODO: 30 tests should be implemented for 
#       1000;10000;100000;1000000;10000000

np.random.seed(42)

tests = []

#lenghts = [1000,10000,100000,1000000]

lenghts = np.array(range(1000,1000000,10000))

tests_per_length = 1

for length in lenghts:
    for _ in range(tests_per_length):

        val = np.sort(np.random.randint(1,4*length,size=length))

        target = np.random.randint(1,4*length)

        test = (length, val, target)

        tests.append(test)


# Function definitions

@time_and_space_profiler
def sequantial_search(val,target):
    for i in range(len(val)):
        if target == val[i]: # comparision
            return i+1
    
    return len(val)

@time_and_space_profiler
def advanced_sequantial_search(val,target):
    comparison = 0
    for i in range(len(val)):
        comparison+=2
        if target == val[i]: # comparision
            comparison-=1
            break
        # add the part to stop searching when target small to the element
        elif target < val[i]:
            break
        
    return comparison

@time_and_space_profiler
def binary_search(val,target):
	
    start = 0
    end = len(val)-1
    comparison = 1

    while start < end:
        half = (end + start)//2
        comparison+=2
        if target == val[half]:
            comparison-=1
            break
        elif target < val[half]:
            end = half -1
        else:
            start = half + 1 
        comparison+=1
    return comparison 
    
funcs = [sequantial_search, advanced_sequantial_search,binary_search]

results = []
for i , (length, val ,target) in tqdm(enumerate(tests),ncols=len(tests)):
    
    for func in funcs:

        func_name,comparison,T, S = func(val,target)

        results.append((i,func_name,length,comparison,T,S))


# Printing results
#print(results)

df = pd.DataFrame(results, columns=['id_test','fuction_name','array_length','comparison','time','space'])

print(df)

df.to_csv('results.csv', index=False)