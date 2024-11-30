from abc import ABC, abstractmethod
from memory_profiler import memory_usage
import time

class Profiler(ABC):
    @abstractmethod
    def profile(self, func, *args, **kwargs):
        """Profiles a function's time and memory usage."""
        pass

class TimeAndSpaceProfiler(Profiler):
    def profile(self, func, *args, **kwargs):
        start_time = time.time()
        mem_before = memory_usage()[0]

        result = func(*args, **kwargs)

        mem_after = memory_usage()[0]
        end_time = time.time()

        logs = {
            "function": func.__name__,
            "time": end_time - start_time,
            "memory": mem_after - mem_before,
        }
        
        logs.update(result._asdict())

        return logs
