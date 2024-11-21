## TODO: TP should be HERE


## TODO: Data Generation


def selection_sort(arr):

    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            comparison_count += 1
            if arr[j] < arr[min_index]:
                min_index = j
        comparison_count += 1
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr


def Bubble_sort(array,length):
    count = 0

    for i in range(length):
        for j in range(0,length - i-1):
            if array[j] > array[j+1]:
                swap = array[j]
                array[j] = array[j+1]
                array[j+1] = swap
                count += 1

    return array


def insertion_sort_by_shifting(arr,length):
    count = 0 

    for i in range(length-1):
        j = i
        while j >= 0 and arr[j] > arr[j+1]:
            arr[j], arr[j+1] = arr[j+1], arr[j]
            j -= 1
            count += 1

    return arr


def insertion_sort_by_exchanges(arr,length):
    count = 0 

    for i in range(1, length):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]  
            count += 1  
            j -= 1
    
    return arr
