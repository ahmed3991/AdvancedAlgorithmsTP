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
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            comparisons += 1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # تبادل العناصر
                swaps += 1
                swapped = True
        if not swapped:
            break  # إذا لم يتم إجراء أي تبادل، فإن المصفوفة مرتبة
    return arr, comparisons, swaps


 
def insertion_sort_shifting(arr):
    n = len(arr)
    comparisons = 0
    shifts = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]  # إزاحة العنصر
            shifts += 1
            j -= 1
        arr[j + 1] = key  # إدخال العنصر في مكانه
    return arr, comparisons, shifts

def insertion_sort_exchanges(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]  # إزاحة العنصر
            j -= 1
        arr[j + 1] = key  # إدخال العنصر في مكانه
    return arr, comparisons, swaps

## TODO: make Benchmarks

print('hello')