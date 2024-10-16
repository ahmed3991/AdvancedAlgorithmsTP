import functools

from memory_profiler import memory_usage
import inspect
import time
from memory_profiler import memory_usage
class Counter:
    def __init__(self):
        self.__count = 0

    def increment(self):
        self.__count += 1

    @property
    def count(self):
        return self.__count


def time_and_space_profiler(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        mem_before = memory_usage()[0]

        counter = Counter()
        if 'compare_counter' in (inspect.getfullargspec(func).args + inspect.getfullargspec(func).kwonlyargs):
            kwargs['compare_counter'] = counter
        _result = func(*args, **kwargs)

        mem_after = memory_usage()[0]
        end_time = time.time()

        return counter.count, end_time - start_time, mem_after - mem_before

    return wrapper