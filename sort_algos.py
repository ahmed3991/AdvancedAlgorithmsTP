## TODO: TP should be HERE


## TODO: Data Generation


## TODO: Sort Algorithms implementations
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

## TODO: Complete the code

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        # متغير لتتبع ما إذا حدث تبادل
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                # تبديل العناصر إذا كانت في ترتيب خاطئ
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        # إذا لم يحدث أي تبادل، المصفوفة مرتبة
        if not swapped:
            break
def insertion_sort_by_shifting(arr):
   for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
    
def insertion_sort_by_exchange(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]  # التبديل
            j -= 1
    return arr


