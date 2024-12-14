
### 1. `generateString` Function

This function generates random strings based on a given set of characters and a specified length. For example:
- If the character set is `[A, B, C, D]` and the length is `10`, the function produces a string of length 10 made up of these characters.
- It is useful for testing LCS algorithms on random data of different lengths.

### 2. LCS Algorithms

#### a. `lcs_recursive`
- This function uses recursion to compute the Longest Common Subsequence (LCS).
- It compares the last characters of the strings. If they match, they are added to the result.
- It relies on dividing the problem into subproblems.
- **Drawback**: Performance is poor for large strings due to high redundancy (exponential complexity).

#### b. `lcs_memoized`
- Improves the recursive approach using memoization.
- Stores intermediate results to avoid recomputation.
- Much faster compared to the basic recursive implementation.

#### c. `lcs_dynamic`
- Uses Dynamic Programming to compute the LCS.
- Creates a 2D table to store intermediate results of comparisons.
- It is the most efficient of the three algorithms in terms of speed and resource usage.

### 3. Modifications in `profiler`

I modified the `profile` function to return a log containing:
- The function name.
- Execution time.
- Memory usage.

I also added support to handle the result as a dictionary-like object using `_asdict`.

