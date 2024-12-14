# Practical Work: Longest Common Subsequence (LCS)

## **Objective**
The goal of this practical assignment is to understand and implement two different methods to solve the Longest Common Subsequence (LCS) problem:

1. A **recursive approach** with or without memoization.
2. A **dynamic programming approach** using a bottom-up method.

Additionally, you will explore the generation of random test data to validate your implementations.

---

## **Problem Statement**
Given two strings `X` and `Y`, the **Longest Common Subsequence (LCS)** is the longest sequence of characters that appears in the same order in both strings, but not necessarily consecutively.

### **Example**
- If `X = "ABCBDAB"` and `Y = "BDCAB"`, the LCS could be `"BCAB"` or `"BDAB"`, with a length of 4.
- If `X = "AXYT"` and `Y = "AYZX"`, the LCS is `"AY"`, with a length of 2.

---

## **Steps to Complete the Assignment**

### **1. Recursive Implementation**
- Implement the LCS using a **recursive approach** based on the recurrence relation:

  - If the last characters of `X` and `Y` are the same:
    ```
    LCS(X[0..m], Y[0..n]) = 1 + LCS(X[0..m-1], Y[0..n-1])
    ```
  - Otherwise:
    ```
    LCS(X[0..m], Y[0..n]) = max(LCS(X[0..m-1], Y[0..n]), LCS(X[0..m], Y[0..n-1]))
    ```

- Test this solution on small strings, as it can be computationally expensive for large inputs.

#### **Enhancement: Memoization**
- Modify the recursive solution to use **memoization** for storing intermediate results to avoid redundant calculations.

### **2. Dynamic Programming Implementation**
- Use a **bottom-up dynamic programming approach** to solve the LCS problem:
  1. Construct a table `dp` of size `(m+1) * (n+1)` where `m` and `n` are the lengths of `X` and `Y`.
  2. Fill this table using the rules derived from the recurrence relation.
  3. Use the table to retrieve both the length of the LCS and the sequence itself by backtracking through the table.

### **3. Random String Generation**
In the provided file `complexity/generator.py`, you will implement the `StringGenerator` class to:

1. Generate **random strings** using a given alphabet (e.g., `['A', 'B', 'C']`).
2. Generate **pairs of strings** with specified lengths (`m` and `n`) and degrees of similarity.

#### Example:
```python
# Example usage:
# Create generator with DNA alphabet
gen = StringGenerator(['A', 'C', 'G', 'T'])

# Generate a single random string
random_string = gen.generate(10)  # e.g., "ACGTACGTAC"

# Generate a pair of strings with specified lengths
str1, str2 = gen.generate_pair(5, 8, similarity=0.7)
```

### **4. Comparison and Testing**
- Compare the performance of the recursive and dynamic programming solutions in terms of:
  - Execution time.
  - Memory usage.

- Test the solutions on:
  - Small test cases (e.g., `X = "ABCBDAB"`, `Y = "BDCAB"`).
  - Randomly generated test cases (using `StringGenerator`).

---

## **Tasks**

1. **Implement the recursive LCS solution** (with and without memoization) in `examples/common_string.py`.
2. **Implement the dynamic programming solution** to compute both the length and the LCS string.
3. **Complete the StringGenerator class** in `complexity/generator.py` to generate test data.
4. Compare and document the performance of the different approaches.

---

## **Optional Optimization**
To reduce memory usage in the dynamic programming approach, optimize the table `dp` to use only two rows or a single 1D array.

---

## **Report and Submission**
Prepare a concise report including:

- An explanation of your implementations.
- Observations on the performance of each approach.
- Examples of generated test cases and their LCS results.
- Conclusions on the trade-offs between the approaches.

