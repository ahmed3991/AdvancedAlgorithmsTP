from memory_profiler import memory_usage
import time

def time_and_space_profiler(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        mem_before = memory_usage()[0]

        result = func(*args, **kwargs)

        mem_after = memory_usage()[0]
        end_time = time.time()

        print(f"Execution time: {end_time - start_time} seconds")
        print(f"Memory usage: {mem_after - mem_before} MiB")

        return result
    return wrapper