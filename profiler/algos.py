from utils import time_and_space_profiler


def SequentialSearch(arr, x, *, compare_counter=None):
    for i in range(len(arr)):
        compare_counter.increment() if compare_counter else None
        if arr[i] == x:
            return i
    return -1


def SequentialSearchOptimized(arr, x, *, compare_counter=None):
    for i in range(len(arr)):
        compare_counter.increment() if compare_counter else None
        if arr[i] == x:
            return i
        elif arr[i] > x:
            return -1
    return -1


def BinarySearch(arr, x, *, compare_counter=None):
    l = 0
    r = len(arr) - 1
    while l <= r:
        compare_counter.increment() if compare_counter else None
        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            l = mid + 1
        else:
            r = mid - 1
    return mid


def BinarySearchRecursive(arr, x, *, compare_counter=None):
    def inner(arr, x, l=0, r=None):
        if r is None:
            r = len(arr) - 1
        if l <= r:
            mid = l + (r - l) // 2
            compare_counter.increment() if compare_counter else None
            if arr[mid] == x:
                return mid
            elif arr[mid] < x:
                return inner(arr, x, mid + 1, r)
            else:
                return inner(arr, x, l, mid - 1)
        return -1

    return inner(arr, x)
