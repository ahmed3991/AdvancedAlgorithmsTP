import utils
import algos
import math
import numpy as np


def find_gen(size):
    arr = np.sort(np.random.randint(0, size * 10, size)).tolist()
    x_to_find = np.random.randint(
        -2 * int(math.log2(size)),
        10 * size + 2 * int(math.log2(size))
    )
    return arr, x_to_find


def main():
    profiler = utils.Profiler()
    profiler.add_size(1_000)
    profiler.add_size(10_000)
    profiler.add_size(100_000)
    profiler.add_size(1_000_000)
    profiler.add_function(algos.SequentialSearch)
    profiler.add_function(algos.SequentialSearchOptimized)
    profiler.add_function(algos.BinarySearch)
    profiler.add_function(algos.BinarySearchRecursive)
    profiler.set_samples(30)
    profiler.run()
    profiler.show()


if __name__ == "__main__":
    main()
