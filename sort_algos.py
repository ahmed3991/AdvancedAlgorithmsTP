## TODO: TP should be HERE

import time
import random

# الدالة الرئيسية لكل خوارزمية التي تحسب الأداء
def measure_performance(sort_function, array):
    comparisons = 0
    moves = 0
    start_time = time.time()
    
    # تنفيذ الخوارزمية مع حساب المقارنات والحركات
    comparisons, moves = sort_function(array)
    
    # حساب وقت التنفيذ
    end_time = time.time()
    execution_time = end_time - start_time
    
    return comparisons, moves, execution_time

# الترتيب بالاختيار
def selection_sort(arr):
    comparisons = 0
    moves = 0
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            moves += 1
    return comparisons, moves

# الترتيب بالفقاعات
def bubble_sort(arr):
    comparisons = 0
    moves = 0
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                moves += 1
    return comparisons, moves

# الترتيب بالإدراج (التبادلي)
def insertion_sort_exchanges(arr):
    comparisons = 0
    moves = 0
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0:
            comparisons += 1
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
                moves += 1
            else:
                break
            j -= 1
    return comparisons, moves

# الترتيب بالإدراج (الإزاحة)
def insertion_sort_shifts(arr):
    comparisons = 0
    moves = 0
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if arr[j] > key:
                arr[j + 1] = arr[j]
                moves += 1
            else:
                break
            j -= 1
        arr[j + 1] = key
    return comparisons, moves

# إنشاء المصفوفات
def generate_arrays(size):
    random_array = [random.randint(1, size) for _ in range(size)]
    ascending_array = sorted(random_array)
    descending_array = sorted(random_array, reverse=True)
    return random_array, ascending_array, descending_array

# تشغيل التجارب وجمع النتائج
def run_experiments(sizes=[1000, 10000, 100000]):
    results = {"selection_sort": [], "bubble_sort": [], "insertion_sort_exchanges": [], "insertion_sort_shifts": []}
    
    for size in sizes:
        print(f"Running experiments for size: {size}")
        
        # تحضير بيانات الاختبار
        random_array, ascending_array, descending_array = generate_arrays(size)
        
        for algorithm_name, sort_function in [("selection_sort", selection_sort), 
                                              ("bubble_sort", bubble_sort), 
                                              ("insertion_sort_exchanges", insertion_sort_exchanges), 
                                              ("insertion_sort_shifts", insertion_sort_shifts)]:
            
            comparisons_list, moves_list, time_list = [], [], []
            
            for _ in range(30):  # تكرار التجربة 30 مرة
                # نسخ المصفوفة لاستخدامها في كل اختبار
                array_copy = random_array[:]
                
                # قياس الأداء
                comparisons, moves, execution_time = measure_performance(sort_function, array_copy)
                
                comparisons_list.append(comparisons)
                moves_list.append(moves)
                time_list.append(execution_time)
            
            # حساب المتوسط
            avg_comparisons = sum(comparisons_list) / len(comparisons_list)
            avg_moves = sum(moves_list) / len(moves_list)
            avg_time = sum(time_list) / len(time_list)
            
            # تخزين النتائج
            results[algorithm_name].append({
                "size": size,
                "avg_comparisons": avg_comparisons,
                "avg_moves": avg_moves,
                "avg_time": avg_time
            })
    
    return results

if __name__ == "__main__":
    results = run_experiments()
    print(results)

## TODO: Data Generation


## TODO: Sort Algorithms implementations


## TODO: make Benchmarks

print('hello')