## TODO: TP should be HERE
import time
from random import randint

## TODO: Data Generation
def generateRandomTable(length):
    t = []  # Initialize the list
    for i in range(length):
        t.append(randint(0, 1000000))  # Use randint correctly
    return t


def generateSortedTable(length):
    t = []  # Initialize the list
    for i in range(length):
        t.append(i)  # Append sequential integers
    return t


def generateReversedTable(length):
    t = []  # Initialize the list
    for i in range(length):
        t.append(length - i - 1)  # Append reversed integers
    return t

## TODO: Sort Algorithms implementations
def selectionSort(t, n):
    comp, move = 0, 0
    for i in range(n):
        index = i
        for j in range(i + 1, n):
            if t[j] < t[index]:
                index = j
            comp += 1
        if index != i:
            t[i], t[index] = t[index], t[i]
            move += 1
    return comp, move


def bubbleSort(t, n):
    comp, move = 0, 0
    for i in range(n):
        for j in range(0, n - i - 1):
            if t[j] > t[j + 1]:
                t[j], t[j + 1] = t[j + 1], t[j]
                move += 1
            comp += 1
    return comp, move


def insertionSortExchange(t, n):
    comp, move = 0, 0
    for i in range(1, n):
        j = i - 1
        while j >= 0 and t[j] > t[i]:
            t[j], t[j + 1] = t[j + 1], t[j]
            comp += 1
            move += 1
            j -= 1
        comp += 1
    return comp, move


def insertionSortShifting(t, n):
    comp, move = 0, 0
    for i in range(1, n):
        key = t[i]
        j = i - 1
        while j >= 0 and t[j] > key:
            t[j + 1] = t[j]
            comp += 1
            move += 1
            j -= 1
        t[j + 1] = key
        comp += 1
    return comp, move


## TODO: make Benchmarks

def measurePerformance(sizes, table_generator, name):
    print(f"\nPerformance on {name} Tables:")
    for size in sizes:
        table = table_generator(size)
        print(f"\nSize: {size}")

        for sort_func in [selectionSort, bubbleSort, insertionSortExchange, insertionSortShifting]:
            table_copy = table.copy()
            start_time = time.time()
            comp, move = sort_func(table_copy, size)
            excution_time = time.time() - start_time

            print(f"{sort_func.__name__}: Time={excution_time:.4f}s, Comparisons={comp}, Moves={move}")


def main():
    sizes = [100, 1000, 10000]  # Adjust sizes as needed
    measurePerformance(sizes, generateRandomTable, "Random")
    measurePerformance(sizes, generateSortedTable, "Sorted")
    measurePerformance(sizes, generateReversedTable, "Reversed")


if __name__ == "__main__":
    main()
