## TODO: TP should be HERE


## TODO: Data Generation
import random

# توليد قائمة عشوائية من الأرقام
data = [random.randint(1, 1000) for _ in range(1000)]
print(data)


## TODO: Sort Algorithms implementations

## TODO: Selection Sort is our task now
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # إيجاد العنصر الأصغر في الجزء غير المرتب
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        # تبديل العنصر الأصغر مع العنصر الأول
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


## TODO: make Benchmarks
import time

# توليد بيانات عشوائية
data = [random.randint(1, 1000) for _ in range(1000)]

# قياس الزمن الذي يستغرقه تنفيذ Selection Sort
start_time = time.time()
selection_sort(data)
end_time = time.time()
print(f"Time taken for Selection Sort: {end_time - start_time} seconds")


print('hello')