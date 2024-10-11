import functools

from memory_profiler import memory_usage
import time

def time_and_space_profiler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        mem_before = memory_usage()[0]

        result = func(*args, **kwargs)

        mem_after = memory_usage()[0]
        end_time = time.time()

        return (result, end_time - start_time, mem_after - mem_before)
    return wrapper