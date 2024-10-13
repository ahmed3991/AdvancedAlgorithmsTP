from complexity import time_and_space_profiler
val = [1,10,15,16,18,22,66,100,254,321,458]

target = 0

@time_and_space_profiler
def sequantial_search(val,target):
    for i in range(len(val)):
        if target == val[i]: # comparision
            return i+1
    
    return len(val)

@time_and_space_profiler
def advanced_sequantial_search(val,target):
    for i in range(len(val)):
        if target == val[i]: # comparision
            return i+1
        # add the part to stop searching when target small to the element
        if target < val[i]:
            return i+1
        
    return len(val)

print(sequantial_search(val,target))

print(advanced_sequantial_search(val,target))