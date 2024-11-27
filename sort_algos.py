def selectionSort(array):
    comparison = 0
    move = 0
    for i in range(len(array)):
        min = i
        for j in range(i + 1, len(array)):
            comparison += 1
            if array[j] < array[min]:
                min = j
        if min != i:
            array[i], array[min] = array[min], array[i]
            move += 1

    return comparison, move


def bubbleSort(array):
    comparison = 0
    swap = 0
    for i in range(len(array)):
        for j in range(0, len(array) - i - 1):
            comparison += 1
            if array[j] > array[j + 1]:
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp
                swap += 1
    return comparison, swap


def insertionSort(arr):
    comparison = 0
    swap = 0
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            comparison += 1
            arr[j + 1] = arr[j]
            swap += 1
            j -= 1
        if j >= 0:
            comparison += 1
        arr[j + 1] = key
        swap += 1
    return comparison, swap


def insertionSort(arr):
    comparison = 0
    swap = 0
    for i in range(1, len(arr)):
        j = i
        while (j > 0 and arr[j] < arr[j - 1]):
            comparison += 1
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            swap += 1
            j -= 1
        if j > 0:
            comparison += 1
    return comparison, swap
