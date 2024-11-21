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
  def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr
def insertion_sort_by_exchanges(arr):
    def insertion_sort_by_exchange(arr):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]  # التبديل
            j -= 1
    return arr

## TODO: make Benchmarks

