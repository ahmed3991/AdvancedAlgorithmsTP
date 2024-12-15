import pandas as pd
from tqdm import tqdm
import sys
from pathlib import Path
import sys
sys.stdout.reconfigure(encoding='utf-8')

# إضافة الدليل الأبوي إلى المسار
sys.path.append(str(Path(__file__).parent.parent))

from complexity import (
    StringGenerator,
    TimeAndSpaceProfiler,
)

from collections import namedtuple

# تعريف NamedTuple لنتيجة LCS
LCSResult = namedtuple('LCSResult', ['lcs_length', 'comparison_count'])

# تهيئة مولد البيانات
string_generator = StringGenerator(alphabit=['A', 'C', 'G', 'T'])  # مثال: استخدام الأبجدية الخاصة بـ DNA

# تعيين أطوال السلاسل وعدد التجارب
lengths = [3, 5, 7]
nbr_experiments = 3

# تعريف NamedTuple لقياسات الأداء
Metrics = namedtuple('Metrics', ['n', 'comparison_count', 'move_count'])

# خوارزميات LCS
def lcs_recursive(str1, str2, m, n, comparison_count=0):
    if m == 0 or n == 0:
        return LCSResult(0, comparison_count)
    if str1[m - 1] == str2[n - 1]:
        result = lcs_recursive(str1, str2, m - 1, n - 1, comparison_count)
        return LCSResult(result.lcs_length + 1, result.comparison_count)
    else:
        result1 = lcs_recursive(str1, str2, m - 1, n, comparison_count + 1)
        result2 = lcs_recursive(str1, str2, m, n - 1, comparison_count + 1)
        return LCSResult(max(result1.lcs_length, result2.lcs_length), result1.comparison_count + result2.comparison_count)

def lcs_memoization(str1, str2, m, n, memo, comparison_count=0):
    if m == 0 or n == 0:
        return LCSResult(0, comparison_count)
    if memo[m][n] != -1:
        return LCSResult(memo[m][n], comparison_count)
    if str1[m - 1] == str2[n - 1]:
        result = lcs_memoization(str1, str2, m - 1, n - 1, memo, comparison_count)
        memo[m][n] = result.lcs_length + 1
        return LCSResult(memo[m][n], result.comparison_count)
    else:
        result1 = lcs_memoization(str1, str2, m - 1, n, memo, comparison_count + 1)
        result2 = lcs_memoization(str1, str2, m, n - 1, memo, comparison_count + 1)
        memo[m][n] = max(result1.lcs_length, result2.lcs_length)
        return LCSResult(memo[m][n], result1.comparison_count + result2.comparison_count)

def lcs_dp(str1, str2):
    m, n = len(str1), len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    comparison_count = 0
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            comparison_count += 1
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return LCSResult(dp[m][n], comparison_count)

# قائمة الخوارزميات للاختبار
funcs = [
    lcs_recursive,
    lcs_memoization,
    lcs_dp,
]

# عملية القياس
profiler = TimeAndSpaceProfiler()
results = []

# إعداد شريط التقدم باستخدام tqdm
total_iterations = len(funcs) * len(lengths) * nbr_experiments
with tqdm(total=total_iterations, desc="Benchmarking", unit="experiment") as pbar:
    for func in funcs:
        for size in lengths:
            for experiment_idx in range(nbr_experiments):
                data = string_generator.generate(size)
                m, n = len(data), len(data)

                # تهيئة جدول الميمو لخوارزمية الميمو
                if func == lcs_memoization:
                    memo = [[-1] * (n + 1) for _ in range(m + 1)]
                    logs = profiler.profile(func, data, data, m, n, memo)
                elif func == lcs_dp:
                    # بالنسبة لخوارزمية lcs_dp، نمرر السلسلتين فقط
                    logs = profiler.profile(func, data, data)
                else:
                    # بالنسبة للخوارزميات الأخرى (مثل lcs_recursive)، نمرر m و n
                    logs = profiler.profile(func, data, data, m, n)

                logs.update({
                    "algorithm": func.__name__,
                    "data_type": "random",
                    "size": size,
                    "experiment": experiment_idx + 1,
                })
                results.append(logs)
                pbar.set_postfix({
                    'algorithm': func.__name__,
                    'size': size,
                    'experiment': experiment_idx + 1,
                })
                pbar.update(1)

# تحويل النتائج إلى DataFrame
df = pd.DataFrame(results)

# كتابة النتائج في ملف CSV
csv_filename = "benchmark_results.csv"
df.to_csv(csv_filename, index=False)

# معالجة البيانات: تحويل الأعمدة الخاصة بالوقت والذاكرة إلى قيم عددية
df['time'] = pd.to_numeric(df['time'], errors='coerce')
df['memory'] = pd.to_numeric(df['memory'], errors='coerce')

# تجميع البيانات حسب الخوارزمية، نوع البيانات والحجم
grouped = df.groupby(['algorithm', 'data_type', 'size']).agg({
    'time': 'mean',
    'memory': 'mean',
    'comparison_count': 'mean',
}).reset_index()

# حفظ النتائج الخام والمجمعة لتحليل لاحق
df.to_csv('lcs_results_raw.csv', index=False)
grouped.to_csv('lcs_results_grouped.csv', index=False)

print("\nتم حفظ النتائج في 'lcs_results_raw.csv' و 'lcs_results_grouped.csv'")
