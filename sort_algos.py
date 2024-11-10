## TODO: TP should be HERE


## TODO: Data Generation


## TODO: Sort Algorithms implementations
## TODO: Selection Sort is our task now
def selection_sort(unsorted_array):
    
    for i in range(0, len(unsorted_array) - 1):
        Minidx = i
        
        for j in range(i + 1, len(unsorted_array)):
            if unsorted_array[j] < unsorted_array[Minidx]:
                Minidx = j
        unsorted_array[i], unsorted_array[Minidx] = unsorted_array[Minidx], unsorted_array[i] # swap
## TODO: make Benchmarks

print('hello')