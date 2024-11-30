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
def sort_selection (t):
    i=0
    swap =0
    comp = 0
    for i in range(len(t)):
        j=i
        for j in range(len(t)):
          comp = comp + 1
          if t[j]>t[i] :
              c= t[i]
              t[i]=t[j]
              t[j]=c
              swap=swap+1
    return 'sort_selection', comp , swap


def sort_bull (t):
    i=0
    swap =0
    comp = 0
    for i in range(len(t)):
        for j in range(len(t)-i-1):
            comp = comp + 1
            if t[j]>t[j+1] :
              c= t[j+1]
              t[j+1]=t[j]
              t[j]=c
              swap=swap+1

    return 'sort_bull',comp , swap


def sort_insertion (t):
    comp = 0
    swap = 0
    for i in range(1,len(t)):
          c=t[i]
          j=i-1
          comp = comp + 1
          while (j>=0 and c < t[j]):
                comp = comp + 1
                t[j+1] = t[j]
                j=j-1
                swap=swap+1
          t[j+1] = c
    comp = comp - 1
    return 'sort_insertion' ,comp , swap


## TODO: make Benchmarks

print('hello')