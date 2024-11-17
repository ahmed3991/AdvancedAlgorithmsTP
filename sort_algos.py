## TODO: TP should be HERE


## TODO: Data Generation


## TODO: Sort Algorithms implementations
def selection_sort(arr):
    comparison_count = 0
    move_count = 0
    arr = arr.copy()

    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            comparison_count += 1
            if arr[j] < arr[min_index]:
                min_index = j
        comparison_count += 1
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
            move_count += 1

    return comparison_count, move_count

## TODO: Complete the code

def bubble_sort(arr):  
    i = 0
    swap = 0
    comp = 0
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            comp = comp + 1
            if arr[j] > arr[j+1] :
              c = arr[j+1]
              arr[j+1] = arr[j]
              arr[j] = c
              swap = swap + 1

    return 'sort_bull',comp , swap

def insertion_sort_by_shifting(arr):
    comp = 0
    swap = 0
    for i in range(1,len(arr)):
          c = arr[i]
          j = i - 1
          comp = comp + 1
          while (j >= 0 and c < arr[j]):
                comp = comp + 1
                arr[j+1] = arr[j]
                j = j - 1
                swap=swap+1
          arr[j+1] = c
    comp = comp - 1
    return 'sort_insertion' ,comp , swap

def insertion_sort_by_exchanges(arr):
    i = 0
    swap = 0
    comp = 0
    for i in range(len(arr)):
        j = i
        for j in range(len(arr)):
          comp = comp + 1
          if arr[j] > arr[i] :
              c = arr[i]
              arr[i] = arr[j]
              arr[j] = c
              swap = swap + 1
    return 'sort_selection', comp , swap

## TODO: make Benchmarks

print('hello')