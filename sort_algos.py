import random
def selectionSort(array, size_array):
    for i in range(size_array):
        min_index = i
        for j in range(i + 1, size_array):
            if array[j] < array[min_index]:
                min_index = j
        (array[i], array[min_index]) = (array[min_index], array[i])

size_array = 10
arr = random.sample(range(-1000, 1000), size_array)
selectionSort(arr, size_array)
print('The array after sorting in Ascending Order by selection sort is:')
print(arr)