
# TP 2: Experimental Study of Simple Sorting Algorithms

This practical session (TP) focuses on the experimental study of simple sorting algorithms (selection sort, bubble sort, and insertion sort with two variants). Here’s a structured approach to guide students in comparing these algorithms:

## 1. Learning Objectives
- Implement simple sorting algorithms studied in tutorials -TD-.
- Compare the performance of these algorithms by measuring the number of comparisons, the number of moves, and CPU execution time.
- Analyze the impact of the initial data arrangement (random, ascending order, descending order).

Here’s a quick review of the algorithms:
- **Selection Sort**: Finds the minimum in the unsorted part of the array and swaps it with the first element of this part.
- **Bubble Sort**: Compares each pair of adjacent elements and swaps them if necessary, repeating the process until the array is sorted.
- **Insertion Sort (by exchanges)**: Inserts each element in its appropriate position through successive exchanges.
- **Insertion Sort (by shifting)**: Shifts larger elements to make room for the direct insertion of a new element.

## 2. Preparing Test Data
- **Generating Arrays**: Create arrays of various sizes (e.g., 1,000; 10,000; 100,000; 1,000,000 elements) to observe scalability.
- **Sorting Scenarios**: Generate three types of arrays for each size:
  - **Random**: Values without any specific order.
  - **Sorted in Ascending Order**: To observe algorithm behavior when the array is already sorted.
  - **Sorted in Descending Order**: To analyze performance in the worst case, especially for algorithms like bubble sort.

## 3. Sorting Algorithm Implementation
- Students should implement each algorithm with counters for:
  - **Comparisons**: Number of comparisons between elements.
  - **Moves**: Number of times an element is moved or swapped.
  - **CPU Time**: Use a timer to measure the execution time of each algorithm.

## 4. Data Measurement and Collection
For each algorithm and array type:
- Execute over 30 tests to reduce statistical variation.
- Collect:
  - Average number of comparisons.
  - Average number of moves/swaps.
  - Average CPU time.
- Organize these results into comparative tables to facilitate analysis.

## 5. Results Analysis
- **Comparisons and Moves**: Compare how different types of arrays (random, sorted, reverse sorted) affect the number of comparisons and moves.
- **CPU Time**: Compare execution times and identify the most efficient algorithms for each array type.
- **Complexity**: Relate observations to the theoretical complexity of the algorithms, such as O(n²) for these simple sorts, and see if the experimental results confirm this complexity.

## 6. Conclusion and Interpretation
- Compare the strengths and weaknesses of each algorithm based on the sorting scenarios.
- Summarize the conditions in which one algorithm would be preferable to another.
