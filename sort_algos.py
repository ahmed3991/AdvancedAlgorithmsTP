## TODO: TP should be HERE


## TODO: Data Generation


## TODO: Sort Algorithms implementations
## TODO: Selection Sort is our task now
def selection_sort(arr):
    n = len(arr)
    comparison = 0  # Counter to track the number of comparisons

    for i in range(n):
        # افتراض أن العنصر الحالي هو الأصغر
        min_index = i
        for j in range(i + 1, n):
            comparison += 1
            # إذا كان العنصر الحالي أصغر من العنصر الذي نفترض أنه الأصغر، قم بتحديث المؤشر
            if arr[j] < arr[min_index]:
                min_index = j
        # تبديل العنصر الأصغر مع العنصر الأول في الجزء غير المرتب
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr, comparison


## TODO: make Benchmarks

print('hello')