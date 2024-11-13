## TODO: TP should be HERE


## TODO: Data Generation


## TODO: Sort Algorithms implementations

def bubble_sort(numbers):
    n = len(numbers)
    for i in range(n):
        
        already_sorted = True
        for j in range(n - i - 1):
            
            if numbers[j] > numbers[j + 1]:
               
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
                
                already_sorted = False
        
        if already_sorted:
            break
    return numbers

## TODO: make Benchmarks

print('hello')