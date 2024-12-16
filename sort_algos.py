import random
import time
import tracemalloc
import pandas as pd

# =======================================
# TODO: TP should be HERE
# Task Processing: تعريف الهدف
# =======================================
# في هذا المشروع، سنقوم بإنشاء بيانات عشوائية، تنفيذ خوارزمية Selection Sort، 
# ومقارنة أدائها مع خوارزميات فرز أخرى.

# =======================================
# TODO: Data Generation
# توليد بيانات عشوائية لاختبار الخوارزميات
# =======================================

def generate_data(size, lower_bound=0, upper_bound=1000):
    """Generate a random list of integers."""
    return [random.randint(lower_bound, upper_bound) for _ in range(size)]

# =======================================
# TODO: Sort Algorithms Implementations
# =======================================

def selection_sort(arr):
    """Implementation of Selection Sort."""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

def bubble_sort(arr):
    """Implementation of Bubble Sort."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# =======================================
# TODO: Make Benchmarks
# =======================================

def profile_sort_function(sort_function, data):
    """Profile sorting function for time and memory."""
    # قياس الوقت والذاكرة
    start_time = time.time()
    tracemalloc.start()
    sorted_data = sort_function(data.copy())  # نسخ البيانات لتجنب التعديل الأصلي
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    elapsed_time = time.time() - start_time
    return elapsed_time, peak / 1024  # Return time and peak memory in KB

# اختبار الخوارزميات:
if __name__ == "__main__":
    print("Generating Data...")
    data_sizes = [100, 500, 1000, 5000, 10000]
    results = []

    for size in data_sizes:
        print(f"Testing for data size: {size}")
        data = generate_data(size)
        
        # اختبار Selection Sort
        time_taken, memory_used = profile_sort_function(selection_sort, data)
        results.append(("Selection Sort", size, time_taken, memory_used))
        
        # اختبار Bubble Sort
        time_taken, memory_used = profile_sort_function(bubble_sort, data)
        results.append(("Bubble Sort", size, time_taken, memory_used))
    
    # عرض النتائج
    df = pd.DataFrame(results, columns=["Algorithm", "Data Size", "Time (s)", "Memory (KB)"])
    print(df)
    df.to_csv("sort_benchmarks.csv", index=False)

    print("Done!")
