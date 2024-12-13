import random
import time
import csv
from memory_profiler import memory_usage
from prettytable import PrettyTable  # استخدام مكتبة لعرض الجدول بشكل جميل

# حل المشكلة باستخدام الاستدعاء الذاتي بدون تخزين
def lcs_recursive(X, Y, i, j):
    if i == 0 or j == 0:
        return 0
    if X[i - 1] == Y[j - 1]:
        return 1 + lcs_recursive(X, Y, i - 1, j - 1)
    else:
        return max(lcs_recursive(X, Y, i - 1, j), lcs_recursive(X, Y, i, j - 1))

# حل المشكلة باستخدام الاستدعاء الذاتي مع التخزين (Memoization)
def lcs_recursive_memo(X, Y, i, j, memo):
    if i == 0 or j == 0:
        return 0
    if (i, j) in memo:
        return memo[(i, j)]
    if X[i - 1] == Y[j - 1]:
        memo[(i, j)] = 1 + lcs_recursive_memo(X, Y, i - 1, j - 1, memo)
    else:
        memo[(i, j)] = max(lcs_recursive_memo(X, Y, i - 1, j, memo), lcs_recursive_memo(X, Y, i, j - 1, memo))
    return memo[(i, j)]

# حل المشكلة باستخدام البرمجة الديناميكية
def lcs_dp(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n]

# حل المشكلة باستخدام الاستدعاء الذاتي مع إرجاع النص المشترك
def lcs_recursive_with_result(X, Y, i, j):
    if i == 0 or j == 0:
        return 0, ""
    if X[i - 1] == Y[j - 1]:
        length, lcs = lcs_recursive_with_result(X, Y, i - 1, j - 1)
        return length + 1, lcs + X[i - 1]
    else:
        length1, lcs1 = lcs_recursive_with_result(X, Y, i - 1, j)
        length2, lcs2 = lcs_recursive_with_result(X, Y, i, j - 1)
        if length1 > length2:
            return length1, lcs1
        else:
            return length2, lcs2

# حل المشكلة باستخدام الاستدعاء الذاتي مع التخزين (Memoization) مع إرجاع النص المشترك
def lcs_recursive_memo_with_result(X, Y, i, j, memo):
    if i == 0 or j == 0:
        return 0, ""
    if (i, j) in memo:
        return memo[(i, j)]
    if X[i - 1] == Y[j - 1]:
        length, lcs = lcs_recursive_memo_with_result(X, Y, i - 1, j - 1, memo)
        memo[(i, j)] = (length + 1, lcs + X[i - 1])
    else:
        length1, lcs1 = lcs_recursive_memo_with_result(X, Y, i - 1, j, memo)
        length2, lcs2 = lcs_recursive_memo_with_result(X, Y, i, j - 1, memo)
        if length1 > length2:
            memo[(i, j)] = (length1, lcs1)
        else:
            memo[(i, j)] = (length2, lcs2)
    return memo[(i, j)]

# حل المشكلة باستخدام البرمجة الديناميكية مع إرجاع النص المشترك
def lcs_dp_with_result(X, Y):
    m, n = len(X), len(Y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    directions = [[None] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                directions[i][j] = "diag"
            else:
                if dp[i - 1][j] >= dp[i][j - 1]:
                    dp[i][j] = dp[i - 1][j]
                    directions[i][j] = "up"
                else:
                    dp[i][j] = dp[i][j - 1]
                    directions[i][j] = "left"

    # استعادة النص المشترك
    lcs = []
    i, j = m, n
    while i > 0 and j > 0:
        if directions[i][j] == "diag":
            lcs.append(X[i - 1])
            i -= 1
            j -= 1
        elif directions[i][j] == "up":
            i -= 1
        else:  # "left"
            j -= 1
    return dp[m][n], ''.join(reversed(lcs))

# مولّد النصوص العشوائية
class StringGenerator:
    def __init__(self, alphabet=['A', 'B', 'C', 'D', 'E']):
        self.alphabet = alphabet

    def generate(self, size: int = 1) -> str:
        return ''.join(random.choice(self.alphabet) for _ in range(size))

    def generate_pair(self, size1: int, size2: int) -> tuple:
        return self.generate(size1), self.generate(size2)

# قياس الأداء (الوقت والذاكرة)
def measure_performance(lcs_func, *args):
    start_time = time.time()
    mem_usage_res = memory_usage((lcs_func, args))  # تمرير المتغيرات بشكل صحيح
    end_time = time.time()
    return end_time - start_time, max(mem_usage_res) - min(mem_usage_res)

# الوظيفة الرئيسية
def main():
    # إنشاء بيانات الاختبار
    gen = StringGenerator(['A', 'B', 'C', 'D', 'E'])
    
    # إنشاء جدول لعرض النتائج
    table = PrettyTable()
    table.field_names = ["Method", "Length of X", "Length of Y", "Time (Seconds)", "Memory Usage (MB)", "Longest Common Subsequence"]


    # اختبار مع أطوال مختلفة للسلاسل
    for length_X, length_Y in [(5, 10), (15, 20)]:
        X, Y = gen.generate_pair(length_X, length_Y)
        print(f"Testing X: {X}\nY: {Y}\n")

        # قياس الأداء واسترجاع النتائج لكل خوارزمية
        time_rec, mem_rec = measure_performance(lcs_recursive_with_result, X, Y, len(X), len(Y))
        _, lcs_rec = lcs_recursive_with_result(X, Y, len(X), len(Y))

        memo = {}
        time_rec_memo, mem_rec_memo = measure_performance(lcs_recursive_memo_with_result, X, Y, len(X), len(Y), memo)
        _, lcs_rec_memo = lcs_recursive_memo_with_result(X, Y, len(X), len(Y), memo)

        time_dp, mem_dp = measure_performance(lcs_dp_with_result, X, Y)
        _, lcs_dp = lcs_dp_with_result(X, Y)

        # إضافة النتائج إلى الجدول
        table.add_row(["Recursive (No Memo)", length_X, length_Y, time_rec, mem_rec, lcs_rec])
        table.add_row(["Recursive (With Memo)", length_X, length_Y, time_rec_memo, mem_rec_memo, lcs_rec_memo])
        table.add_row(["Dynamic Programming", length_X, length_Y, time_dp, mem_dp, lcs_dp])

    # طباعة الجدول
    print(table)

# تشغيل البرنامج
if __name__ == "__main__":
    main()









