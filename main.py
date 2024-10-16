import utils
import algos


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
