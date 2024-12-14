#TODO: put the code here
import time
import random
from memory_profiler import profile

from complexity.generator import StringGenerator


# Generate random strings for testing
gen = StringGenerator(['A', 'B', 'C'])
str1, str2 = gen.generate_pair(1000, 1000)  # Strings of size 1000

# Test Recursive Solution
start_time = time.time()
lcs_recursive(str1, str2, len(str1), len(str2))
end_time = time.time()
print(f"Recursive time: {end_time - start_time} seconds")

# Test Recursive with Memoization
memo = [[-1 for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
start_time = time.time()
lcs_memoization(str1, str2, len(str1), len(str2), memo)
end_time = time.time()
print(f"Memoization time: {end_time - start_time} seconds")

# Test Dynamic Programming
start_time = time.time()
lcs_dp(str1, str2)
end_time = time.time()
print(f"DP time: {end_time - start_time} seconds")

@profile
def test_lcs():
    # Test Dynamic Programming
    lcs_dp(str1, str2)

test_lcs()
print('Please use the complexity library')

