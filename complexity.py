from memory_profiler import memory_usage
import time
import numpy as np

def time_and_space_profiler(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        mem_before = memory_usage()[0]

        result = func(*args, **kwargs)

        mem_after = memory_usage()[0]
        end_time = time.time()

        #print(f"Execution time: {end_time - start_time} seconds")
        #print(f"Memory usage: {mem_after - mem_before} MiB")

        return func.__name__,result,end_time-start_time,mem_after - mem_before
    return wrapper

# calculate the least squares to fit the complexity fucntion
# inspired by https://github.com/Alfex4936/python-bigO-calculator
def leastSquares(x,y,func):
    sigma_gn_squared = func(x)**2
    sigma_gn_y = func(x) * y
    coef = sigma_gn_y.sum() / sigma_gn_squared.sum()
    rms = np.sqrt(((y - coef * func(x))** 2).mean()) / y.mean()
    return rms

# print the complexity of the algorithm using array lenght and time - or comparison -
def get_complexity(x, y):

    def _1(x):
        return np.ones(x.shape)

    def n(x):
        return x

    def n_2(x):
        return x**2

    def n_3(x):
        return x**3

    def log2(x):
        return np.log2(x)

    def nlog2(x):
        return x * np.log2(x)

    funcs = [_1,n,n_2,n_3,log2,nlog2]
    complexity_names = ['O(1)','O(n)','O(n2)','O(n3)','O(log2)','O(nlog2)']

    best_fit =  leastSquares(x,y,funcs[0])
    best_name = complexity_names[0]


    for func , name  in zip(funcs[1:],complexity_names[1:]):
        new_fit = leastSquares(x,y,func)
        if new_fit < best_fit:
            best_fit = new_fit
            best_name = name

    return best_name

#TODO: add the code to generate random data for testing 
#TODO: add the logic to test algorithms directly and get the best one from them using complexity comparion
