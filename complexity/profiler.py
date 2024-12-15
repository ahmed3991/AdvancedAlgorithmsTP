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
        start_time = time.time()  # بدء قياس الوقت
        mem_before = memory_usage()[0]  # قياس استهلاك الذاكرة قبل التنفيذ

        result = func(*args, **kwargs)  # تنفيذ الدالة

        mem_after = memory_usage()[0]  # قياس استهلاك الذاكرة بعد التنفيذ
        end_time = time.time()  # انتهاء قياس الوقت

        logs = {
            "function": func.__name__,
            "time": end_time - start_time,
            "memory": mem_after - mem_before,
        }

        # إضافة النتيجة إلى السجل
        if isinstance(result, dict):  # إذا كانت النتيجة عبارة عن قاموس
            logs.update(result)
        else:  # إذا كانت النتيجة عددًا أو نصًا
            logs["result"] = result

        return logs
