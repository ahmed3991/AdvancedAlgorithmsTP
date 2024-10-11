from utils import time_and_space_profiler

@time_and_space_profiler
def SequentialSearch(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i + 1
    return len(arr)

@time_and_space_profiler
def SequentialSearchOptimized(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i + 1
        elif arr[i] > x:
            return i + 1
    return len(arr)

@time_and_space_profiler
def BinarySearch(arr, x):
    l = 0
    r = len(arr) - 1
    comparisons = 0
    while l <= r:
        comparisons += 1
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return comparisons
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return comparisons

@time_and_space_profiler
def BinarySearchRecursive(arr, x):
    def inner(arr, x, l = 0, r = None):
        if r is None:
            r = len(arr) - 1
        if l <= r:
            mid = l + (r - l) // 2
            if arr[mid] == x:
                return 1
            elif arr[mid] < x:
                return 1 + inner(arr, x, mid + 1, r)
            else:
                return 1 + inner(arr, x, l, mid - 1)
        return 1

    return inner(arr, x)