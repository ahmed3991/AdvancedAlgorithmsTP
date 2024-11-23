## TODO: TP should be HERE


## TODO: Data Generation


## TODO: Sort Algorithms implementations
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

def swap(T,a,b):
    T[a], T[b] = T[b], T[a]

## TODO: Complete the code

@time_and_space_profiler
def bubble_sort(T):
    n = len(T)
    comparisons=0
    moves=0
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            comparisons+=1
            if T[j] > T[j+1]:
                comparisons+=1
                T[j], T[j+1] = T[j+1], T[j]
                moves+=1
                swapped = True
        if (swapped == False):
            comparisons+=1
            break
    return comparisons,moves

@time_and_space_profiler
def insertion_sort_swap(T):
    comparisons=0
    N = len(T)
    moves=0
    for i in range(1,N):
        j = i
        comparisons+=1
        while (j > 0 and T[j] < T[j - 1]) :
            comparisons+=1
            temp = T[j]
            T[j] = T[j - 1]
            T[j-1] = temp
            moves+=1
            j -= 1
    return comparisons,moves
    
@time_and_space_profiler
def insertion_sort_shift(T):
    comparisons=0
    moves=0
    for i in range(1, len(T)):
        comparisons+=1
        key = T[i]
        j = i - 1
        while (j >= 0 and key < T[j]):
            comparisons+=1
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key
        moves+=1
    return comparisons,moves

## TODO: make Benchmarks

print('hello')
