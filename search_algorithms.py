import numpy as np
import pandas as pd
import time
from memory_profiler import memory_usage
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")


# خوارزمية البحث الخطي البسيط
def simple_sequential_search(arr, target):
    comparisons = 0
    for element in arr:
        comparisons += 1
        if element == target:
            return comparisons
    return comparisons


# خوارزمية البحث الخطي المحسن
def optimized_sequential_search(arr, target):
    comparisons = 0
    for element in arr:
        comparisons += 1
        if element > target:
            return comparisons
        if element == target:
            return comparisons
    return comparisons


# خوارزمية البحث الثنائي (تكراري)
def iterative_binary_search(arr, target):
    comparisons = 0
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if arr[mid] == target:
            return comparisons
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return comparisons


# خوارزمية البحث الثنائي (تكراري)
def recursive_binary_search(arr, target, left, right, comparisons=0):
    if left > right:
        return comparisons
    mid = (left + right) // 2
    comparisons += 1
    if arr[mid] == target:
        return comparisons
    elif arr[mid] < target:
        return recursive_binary_search(arr, target, mid + 1, right, comparisons)
    else:
        return recursive_binary_search(arr, target, left, mid - 1, comparisons)


# قياس الأداء
def test_search_algorithm(algorithm, arr, target):
    start_time = time.time()
    comparisons = algorithm(arr, target)
    exec_time = time.time() - start_time
    return comparisons, exec_time


# تنفيذ التجارب
def run_experiments():
    array_sizes = [10**3, 10**4, 10**5]  # تقليل الأحجام لتسريع التنفيذ
    algorithms = {
        "Simple Sequential Search": simple_sequential_search,
        "Optimized Sequential Search": optimized_sequential_search,
        "Iterative Binary Search": iterative_binary_search,
        "Recursive Binary Search": lambda arr, target: recursive_binary_search(arr, target, 0, len(arr) - 1)
    }
    results = []

    for size in array_sizes:
        arr = sorted(np.random.randint(1, size * 10, size))
        for algorithm_name, algorithm in algorithms.items():
            total_comparisons, total_exec_time = 0, 0
            for _ in range(10):  # تقليل عدد التجارب إلى 10 لتسريع التنفيذ
                target = np.random.randint(1, size * 10)
                comp, time_taken = test_search_algorithm(algorithm, arr, target)
                total_comparisons += comp
                total_exec_time += time_taken
            results.append({
                "Algorithm": algorithm_name,
                "Array Size": size,
                "Avg Comparisons": total_comparisons / 10,
                "Avg Execution Time": total_exec_time / 10
            })

    return pd.DataFrame(results)


if __name__ == '__main__':
    # تشغيل التجارب وحفظ النتائج
    results_df = run_experiments()

    # عرض النتائج في شكل جدول
    print(results_df)

    # رسم منحنيات بيانية لوقت التنفيذ لكل خوارزمية حسب حجم المصفوفة
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=results_df, x='Array Size', y='Avg Execution Time', hue='Algorithm')
    plt.title('Average Execution Time by Algorithm and Array Size')
    plt.xlabel('Array Size')
    plt.ylabel('Avg Execution Time (s)')
    plt.grid(True)
    plt.show()

    # رسم منحنيات بيانية لعدد المقارنات لكل خوارزمية حسب حجم المصفوفة
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=results_df, x='Array Size', y='Avg Comparisons', hue='Algorithm')
    plt.title('Average Comparisons by Algorithm and Array Size')
    plt.xlabel('Array Size')
    plt.ylabel('Avg Comparisons')
    plt.grid(True)
    plt.show()
