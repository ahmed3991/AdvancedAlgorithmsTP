import random
def selectionSort(array, size):
    for i in range(size):
        min_index = i
        for j in range(i + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[i], array[min_index]) = (array[min_index], array[i])

size = 10
arr = random.sample(range(-1000, 1000), size)
selectionSort(arr, size)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)
