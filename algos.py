from complexity import time_and_space_profiler
import numpy as np


# Inialization logic
# TODO: 30 tests should be implemented for 
#       1000;10000;100000;1000000;10000000

tests = []

lenghts = [1000,10000,100000,1000000,10000000]
np.random.seed(42)

val = np.sort(np.random.randint(1,10000000,size=1000000))

target = np.random.randint(1,10000000)

test = (val, target)

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
    

print(sequantial_search(val,target))

print(advanced_sequantial_search(val,target))

print(binary_search(val,target))
