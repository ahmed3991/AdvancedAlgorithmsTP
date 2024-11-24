## TODO: TP should be HERE


## TODO: Data Generation


## TODO: Sort Algorithms implementations
## TODO: Selection Sort is our task now
@time_and_space_profiler
def selection_sort(T):
    i=0
    index_min=0
    j=0
    comparisons=0
    moves=0
    while(i<(len(T)-1)):
        comparisons+=1
        index_min=i
        j=i+1
        while(j<len(T)):
            if(T[j]<T[index_min]):
                comparisons+=1
                index_min=j
            j+=1
        swap(T,i,index_min)
        moves+=1
        i+=1
    return comparisons,moves
    

## TODO: make Benchmarks

print('hello')
