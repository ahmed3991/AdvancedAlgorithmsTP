## TODO: TP should be HERE


## TODO: Data Generation

lenghts =[10,100,1000,10000]

# TODO : Use numpy
random_arrays= []
# TODO : Use range
sorted_arrays= []
# TODO : Use range
inverse_sorted_arrays = []

nbr_experiments = 10


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
    comparisons = 0
    swaps = 0
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1

    return  comparisons, swaps


def insertion_sort_shifting(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            comparisons += 1
            arr[j + 1] = arr[j]  # Shift
            swaps += 1
            j -= 1
        arr[j + 1] = key

        if j != i - 1:
            comparisons += 1

    return  comparisons, swaps
def insertion_sort_exchange(arr):
    comparisons = 0
    swaps = 0
    n = len(arr)

    for i in range(1, n):
        j = i
        while j > 0 and arr[j] < arr[j - 1]:
            comparisons += 1
            arr[j], arr[j - 1] = arr[j - 1], arr[j]  # Swap
            swaps += 1
            j -= 1

        if j > 0:
            comparisons += 1

    return  comparisons, swaps



funcs = [selection_sort, bubble_sort,insertion_sort_shifting,insertion_sort_exchange]

results = []
 
# TODO: Complete the benchmark code

for func in funcs:
    for length, random_arr, sorted_arr, inverse_arr in zip(lengths, random_arrays, sorted_arrays, inverse_sorted_arrays):
        # إجراء التجربة للقائمة العشوائية
        start_time = time.time()
        comparisons, swaps = func(random_arr)
        elapsed_time = time.time() - start_time
        results.append((func.__name__, length, "random", comparisons, swaps, elapsed_time))

        # إجراء التجربة للقائمة المرتبة
        start_time = time.time()
        comparisons, swaps = func(sorted_arr)
        elapsed_time = time.time() - start_time
        results.append((func.__name__, length, "sorted", comparisons, swaps, elapsed_time))

        # إجراء التجربة للقائمة المرتبة عكسياً
        start_time = time.time()
        comparisons, swaps = func(inverse_arr)
        elapsed_time = time.time() - start_time
        results.append((func.__name__, length, "inverse_sorted", comparisons, swaps, elapsed_time))

# عرض النتائج
print("Function | Length | Array Type       | Comparisons | Swaps | Time (s)")
print("---------|--------|------------------|-------------|-------|----------")
for result in results:
    print(f"{result[0]:<9} | {result[1]:<6} | {result[2]:<16} | {result[3]:<11} | {result[4]:<5} | {result[5]:.6f}")
