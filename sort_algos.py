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


for func in funcs:
    for length, random_arr, sorted_arr, inverse_sorted_arr in zip(lengths, random_arrays, sorted_arrays, inverse_sorted_arrays):
        for experiment in range(nbr_experiments):
            start_time = time.time()
            random_result = func(random_arr)
            end_time = time.time()
            results.append({
                "Algorithm": func.__name__,
                "Data Type": "random",
                "Array Length": length,
                "Comparisons": random_result[0],
                "Moves": random_result[1],
                "Execution Time (s)": end_time - start_time
            })

            start_time = time.time()
            sorted_result = func(sorted_arr)
            end_time = time.time()
            results.append({
                "Algorithm": func.__name__,
                "Data Type": "sorted",
                "Array Length": length,
                "Comparisons": sorted_result[0],
                "Moves": sorted_result[1],
                "Execution Time (s)": end_time - start_time
            })

            start_time = time.time()
            inverse_result = func(inverse_sorted_arr)
            end_time = time.time()
            results.append({
                "Algorithm": func.__name__,
                "Data Type": "inverse_sorted",
                "Array Length": length,
                "Comparisons": inverse_result[0],
                "Moves": inverse_result[1],
                "Execution Time (s)": end_time - start_time
            })

df = pd.DataFrame(results)

output_file = "results.csv"
df.to_csv(output_file, index=False)

print(f"Results saved to {output_file}")