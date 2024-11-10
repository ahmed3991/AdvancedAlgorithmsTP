## TODO: TP should be HERE


## TODO: Data Generation


## TODO: Sort Algorithms implementations
## TODO: Selection Sort is our task now
def selectionSort (t,n) :
    comp, move = 0, 0  # Initialize comparison and move counters
    for i in range(n):
        index = i
        for j in range(i + 1, n):
            if t[j] < t[index]:
                index = j
            comp += 1
        if index != i:
            t[i], t[index] = t[index], t[i]
            move += 1
    return comp, move

## TODO: make Benchmarks

print('hello')