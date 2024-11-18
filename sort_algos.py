## TODO: TP should be HERE


## TODO: Data Generation


## TODO: Sort Algorithms implementations


## TODO: Selection Sort is our task now
def selection_sort(arr):
    # نمر على كل عنصر في القائمة
    for i in range(len(arr)):
        # نفترض أن العنصر الحالي هو الأصغر
        min_index = i
        # نبحث عن أصغر عنصر في الجزء غير المرتب من القائمة
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        # بعد العثور على أصغر عنصر، نقوم بتبديله مع العنصر الحالي
        arr[i], arr[min_index] = arr[min_index], arr[i]

# اختبار الكود
arr = [75, 35, 15, 33, 12]
selection_sort(arr)
print("القائمة مرتبة:", arr)


## TODO: make Benchmarks

print('hello')