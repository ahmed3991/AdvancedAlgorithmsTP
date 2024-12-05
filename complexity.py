from memory_profiler import memory_usage
import time
import numpy as np

# Profiler to measure execution time and memory usage
def time_and_space_profiler(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        mem_before = memory_usage()[0]

        result = func(*args, **kwargs)

        mem_after = memory_usage()[0]
        end_time = time.time()

        return func.__name__, result, end_time - start_time, mem_after - mem_before
    return wrapper

# Calculate the least squares to fit the complexity function
def leastSquares(x, y, func):
    sigma_gn_squared = (func(x) ** 2).sum()
    sigma_gn_y = (func(x) * y).sum()
    coef = sigma_gn_y / sigma_gn_squared
    rms = np.sqrt(((y - coef * func(x)) ** 2).mean()) / y.mean()
    func_data = coef * func(x)
    
    return rms, func_data, coef

# Determine the complexity of the algorithm using array length and time/comparison data
def get_complexity(x, y):
    # Define common complexity functions
    def _1(x): return np.ones(x.shape)
    def n(x): return x
    def n_2(x): return x ** 2
    def n_3(x): return x ** 3
    def log2(x): return np.log2(x)
    def nlog2(x): return x * np.log2(x)

    funcs = [_1, n, n_2, n_3, log2, nlog2]
    complexity_names = ['O(1)', 'O(n)', 'O(n^2)', 'O(n^3)', 'O(log n)', 'O(n log n)']

    # Fit each function and find the best fit
    best_fit, _, _ = leastSquares(x, y, funcs[0])
    best_name = complexity_names[0]

    for func, name in zip(funcs[1:], complexity_names[1:]):
        new_fit, _, _ = leastSquares(x, y, func)
        if new_fit < best_fit:
            best_fit = new_fit
            best_name = name

    return best_name

# Generate random data for testing
def generate_test_data(lengths, tests_per_length=5):
    np.random.seed(42)
    tests = []

    for length in lengths:
        for _ in range(tests_per_length):
            array = np.sort(np.random.randint(1, 4 * length, size=length))
            target = np.random.randint(1, 4 * length)
            tests.append((length, array, target))

    return tests

# Logic to test algorithms and determine the best one based on complexity
def test_algorithms(algorithms, test_data):
    results = []
    for length, array, target in test_data:
        for func in algorithms:
            func_name, result, exec_time, mem_usage = func(array, target)
            results.append((func_name, length, exec_time, mem_usage, result))
    
    # Organize results into arrays for analysis
    complexities = {}
    for func_name in set(r[0] for r in results):
        lengths = np.array([r[1] for r in results if r[0] == func_name])
        times = np.array([r[2] for r in results if r[0] == func_name])
        best_fit = get_complexity(lengths, times)
        complexities[func_name] = best_fit

    # Find the algorithm with the best (lowest) complexity
    best_algorithm = min(complexities, key=lambda k: complexities[k])

    return complexities, best_algorithm


# Example usage
if __name__ == "__main__":
    # Define algorithms to test
    @time_and_space_profiler
    def dummy_algorithm(val, target):
        return np.searchsorted(val, target)

    algorithms = [dummy_algorithm]

    # Generate test data
    lengths = np.array([1000, 5000, 10000, 50000, 100000])
    test_data = generate_test_data(lengths)

    # Test algorithms and find the best one
    complexities, best_algorithm = test_algorithms(algorithms, test_data)

    print("Complexities of each algorithm:")
    for algo, complexity in complexities.items():
        print(f"{algo}: {complexity}")

    print(f"The best algorithm is: {best_algorithm}")

