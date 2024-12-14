After running the tests for different string sizes, you'll likely observe the following:
•	Recursive Solution:
o	Time Complexity: O(2^n) due to overlapping subproblems. It is very slow for large strings.
o	Memory Usage: Can be high due to deep recursion stacks.
•	Memoized Recursive Solution:
o	Time Complexity: O(m * n), where m and n are the lengths of the strings. Much faster than the pure recursive solution.
o	Memory Usage: Moderate due to the memoization table.
•	Dynamic Programming:
o	Time Complexity: O(m * n), similar to memoization, but it uses an iterative approach.
o	Memory Usage: Can be high due to the 2D dp table, but more efficient than recursion.
•	Memory Optimization (Extension):
o	By using two 1D arrays instead of a 2D dp table, we can significantly reduce memory usage.
7. Conclusion
•	The recursive solution without memoization is inefficient for large input sizes due to its exponential time complexity.
•	The memoized solution and the dynamic programming approach both have a time complexity of O(m * n), which is more efficient, especially for large strings.
•	The dynamic programming approach is preferred for its clarity and iterative nature, but it can be optimized in terms of memory by using two 1D arrays.

