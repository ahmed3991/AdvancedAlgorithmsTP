## TODO: TP should be HERE


## TODO: Data Generation


## TODO: Sort Algorithms implementations

import time
import random
import psutil

def get_memory_usage():
    current_process = psutil.Process()
    return current_process.memory_info().rss / (1024 * 1024)

def selection_sort_algorithm(data, size):
    swap_count = 0

    start_time = time.time()
    initial_memory = get_memory_usage()

    for current_index in range(size):
        smallest_index = current_index
        for next_index in range(current_index + 1, size):
            if data[smallest_index] > data[next_index]:
                smallest_index = next_index
                swap_count += 1

        data[current_index], data[smallest_index] = data[smallest_index], data[current_index]
    final_memory = get_memory_usage()
    end_time = time.time()

    print(f"Execution Time: {end_time - start_time:.5f} seconds")
    print(f"Memory Used: {final_memory - initial_memory:.2f} MB")
    print(f"Total Swaps: {swap_count}")

    return data

if __name__ == "__main__":
    random_array = [random.randint(1, 100) for _ in range(10)]
    print("Original Array:", random_array)

    sorted_array = selection_sort_algorithm(random_array, len(random_array))
    print("Sorted Array:", sorted_array)

## TODO: make Benchmarks