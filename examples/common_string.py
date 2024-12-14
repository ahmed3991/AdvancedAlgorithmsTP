import time
import random


# Step 1: Recursive implementation (with memoization)
def lcs_recursive(X, Y, m, n, memo):
    if m == 0 or n == 0:
        return 0, ""
    if (m, n) in memo:
        return memo[(m, n)]

    if X[m - 1] == Y[n - 1]:
        result_length, result_string = lcs_recursive(X, Y, m - 1, n - 1, memo)
        memo[(m, n)] = result_length + 1, result_string + X[m - 1]
    else:
        result_left, result_left_string = lcs_recursive(X, Y, m - 1, n, memo)
        result_right, result_right_string = lcs_recursive(X, Y, m, n - 1, memo)

        if result_left > result_right:
            memo[(m, n)] = result_left, result_left_string
        else:
            memo[(m, n)] = result_right, result_right_string

    return memo[(m, n)]


# Step 2: Dynamic Programming approach (bottom-up)
def lcs_dynamic(X, Y):
    m = len(X)
    n = len(Y)
    dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if X[i - 1] == Y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    # Reconstructing the LCS string from dp table
    lcs_string = ""
    i, j = m, n
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs_string = X[i - 1] + lcs_string
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return dp[m][n], lcs_string


# Step 3: String Generator for random string creation
class StringGenerator:
    def __init__(self, alphabet=['A', 'B', 'C']):
        self.alphabet = alphabet

    def generate(self, size):
        return ''.join(random.choice(self.alphabet) for _ in range(size))

    def generate_pair(self, size1, size2):
        str1 = self.generate(size1)
        str2 = self.generate(size2)
        return str1, str2


# Time measurement function
def time_lcs(func, X, Y, m, n, memo=None):
    start_time = time.time()
    if func == lcs_recursive:
        result = func(X, Y, m, n, memo)
    else:
        result = func(X, Y)
    end_time = time.time()
    return result[0], result[1], end_time - start_time  # Return length, LCS string, and time


# Testing with small strings
X = "ABCBDAB"
Y = "BDCAB"
memo = {}

# Recursive approach with memoization
lcs_recursive_result, lcs_recursive_string, time_recursive = time_lcs(lcs_recursive, X, Y, len(X), len(Y), memo)
print(
    f"LCS (Recursive) on strings X: {X}, Y: {Y} -> LCS: {lcs_recursive_string}, LCS Length: {lcs_recursive_result}, Time: {time_recursive:.6f}s")

# Dynamic Programming approach
lcs_dynamic_result, lcs_dynamic_string, time_dynamic = time_lcs(lcs_dynamic, X, Y, len(X), len(Y))
print(
    f"LCS (Dynamic Programming) on strings X: {X}, Y: {Y} -> LCS: {lcs_dynamic_string}, LCS Length: {lcs_dynamic_result}, Time: {time_dynamic:.6f}s")

# Generate random strings and test with the generator
gen = StringGenerator(['A', 'B', 'C', 'D'])
str1, str2 = gen.generate_pair(8, 10)  # Generate strings of length 8 and 10
print(f"Generated strings: \nStr1: {str1}\nStr2: {str2}")

# Testing LCS on generated random strings
lcs_gen_recursive_result, lcs_gen_recursive_string, time_gen_recursive = time_lcs(lcs_recursive, str1, str2, len(str1),
                                                                                  len(str2), memo)
print(
    f"LCS (Recursive) on generated strings Str1: {str1}, Str2: {str2} -> LCS: {lcs_gen_recursive_string}, LCS Length: {lcs_gen_recursive_result}, Time: {time_gen_recursive:.6f}s")

lcs_gen_dynamic_result, lcs_gen_dynamic_string, time_gen_dynamic = time_lcs(lcs_dynamic, str1, str2, len(str1),
                                                                            len(str2))
print(
    f"LCS (Dynamic Programming) on generated strings Str1: {str1}, Str2: {str2} -> LCS: {lcs_gen_dynamic_string}, LCS Length: {lcs_gen_dynamic_result}, Time: {time_gen_dynamic:.6f}s")
