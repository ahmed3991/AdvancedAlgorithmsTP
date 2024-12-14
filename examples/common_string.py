#TODO: put the code here
import random
import time
import numpy as np
import matplotlib.pyplot as plt # type: ignore
from abc import ABC, abstractmethod

class StringGenerator(DataGenerator):
    def __init__(self, alphabet=None):
        if alphabet is None:
            alphabet = ['A', 'B', 'C']
        self.alphabet = alphabet

    def generate(self, size: int = 1) -> str:
        return ''.join(random.choice(self.alphabet) for _ in range(size))

    def generate_pair(self, m: int, n: int, similarity: float = 0.0) -> tuple[str, str]:
        if not (0.0 <= similarity <= 1.0):
            raise ValueError("Similarity must be between 0.0 and 1.0")
        base_string = self.generate(max(m, n))
        string1 = base_string[:m]
        string2 = ''
        for i in range(n):
            if i < len(base_string) and random.random() < similarity:
                string2 += base_string[i]
            else:
                string2 += random.choice(self.alphabet)
        return string1, string2

    def generate_similar(self, base_string: str, difference_count: int = 0) -> str:
        base_list = list(base_string)
        for _ in range(min(difference_count, len(base_list))):
            index = random.randint(0, len(base_list) - 1)
            base_list[index] = random.choice(self.alphabet)
        return ''.join(base_list)
    
def LCS_Recursion(string1, string2, m, n):
    if m == 0 or n == 0:
        return 0,
    if string1[m-1] == string2[n-1]:
        return 1 +LCS_Recursion(string1, string2, m-1, n-1)
    else:
        return max(LCS_Recursion(string1, string2, m-1, n), LCS_Recursion(string1, string2, m, n-1))

    

def LCS_Dynamic_(string1, string2, m, n):
    LCS_Dynamic = [[0 for x in range(n+1)] for x in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                LCS_Dynamic[i][j] = 0
            elif S1[i-1] == S2[j-1]:
                LCS_Dynamic[i][j] = LCS_Dynamic[i-1][j-1] + 1
            else:
                LCS_Dynamic[i][j] = max(LCS_Dynamic[i-1][j], LCS_Dynamic[i][j-1])

    index = LCS_Dynamic[m][n]

    LCS_Dynamic_ = [""] * (index+1)
    LCS_Dynamic_[index] = ""

    i = m
    j = n
    while i > 0 and j > 0:
        if S1[i-1] == S2[j-1]:
            LCS_Dynamic_[index-1] = S1[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif LCS_Dynamic[i-1][j] > LCS_Dynamic[i][j-1]:
            i -= 1
        else:
            j -= 1
            
    print("S1 : " + S1 + "\nS2 : " + S2)
    print("LCS_Dynamic: " + "".join(LCS_Dynamic_))

def LCS_Memo(string1, string2, m, n, memo):
    if m == 0 or n == 0:
        return 0
    if x[m-1] == y[n-1]:
        memo[m][n] = 1 + LCS_Memo(x, y, m-1, n-1, memo)
    else:
        memo[m][n] = max(LCS_Memo(x, y, m-1, n, memo), LCS_Memo(x, y, m, n-1, memo))
    return memo[m][n]

class Profiler(ABC):
    @abstractmethod
    def profile(self, func, *args, **kwargs):
        pass

class TimeAndSpaceProfiler(Profiler):
    def profile(self, func, *args, **kwargs):
        start_time = time.time()
        mem_before = memory_usage()[0]

        result = func(*args, **kwargs)

        mem_after = memory_usage()[0]
        end_time = time.time()

        logs = {
            "function": func.__name__,
            "time": end_time - start_time,
            "memory": mem_after - mem_before,
        }
        
        logs.update(result._asdict())
        return logs


# Complexity Functions
class ComplexityFunction(ABC):
    @abstractmethod
    def evaluate(self, x: np.ndarray) -> np.ndarray:
        pass

    @abstractmethod
    def name(self) -> str:
        pass

class ZeroComplexity(ComplexityFunction):
    def evaluate(self, x: np.ndarray) -> np.ndarray:
        return np.zeros(x.shape)

    def name(self) -> str:
        return "O(0)"

class ConstantComplexity(ComplexityFunction):
    def evaluate(self, x: np.ndarray) -> np.ndarray:
        return np.ones(x.shape)

    def name(self) -> str:
        return "O(1)"

class LinearComplexity(ComplexityFunction):
    def evaluate(self, x: np.ndarray) -> np.ndarray:
        return x

    def name(self) -> str:
        return "O(n)"

class QuadraticComplexity(ComplexityFunction):
    def evaluate(self, x: np.ndarray) -> np.ndarray:
        return x ** 2

    def name(self) -> str:
        return "O(n^2)"

class CubicComplexity(ComplexityFunction):
    def evaluate(self, x: np.ndarray) -> np.ndarray:
        return x ** 3

    def name(self) -> str:
        return "O(n^3)"

class LogarithmicComplexity(ComplexityFunction):
    def evaluate(self, x: np.ndarray) -> np.ndarray:
        return np.log2(x)

    def name(self) -> str:
        return "O(log n)"

class LinearLogComplexity(ComplexityFunction):
    def evaluate(self, x: np.ndarray) -> np.ndarray:
        return x * np.log2(x)

    def name(self) -> str:
        return "O(n log n)"


# Least Squares Calculation
class LeastSquaresCalculator:
    @staticmethod
    def calculate(x: np.ndarray, y: np.ndarray, complexity_func: ComplexityFunction) -> float:
        sigma_gn_squared = complexity_func.evaluate(x) ** 2
        sigma_gn_y = complexity_func.evaluate(x) * y
        coef = sigma_gn_y.sum() / sigma_gn_squared.sum()
        rms = np.sqrt(((y - coef * complexity_func.evaluate(x)) ** 2).mean()) / y.mean()
        return rms


# Complexity Analyzer
class ComplexityAnalyzer:
    def __init__(self, complexity_functions: list = None):
        if complexity_functions is None:
            self.complexity_functions = [
                ZeroComplexity(),
                ConstantComplexity(),
                LinearComplexity(),
                QuadraticComplexity(),
                CubicComplexity(),
                LogarithmicComplexity(),
                LinearLogComplexity(),
            ]
        else:
            self.complexity_functions = complexity_functions

    def get_best_fit(self, x: np.ndarray, y: np.ndarray) -> str:
        best_fit = float("inf")
        best_func = None

        for func in self.complexity_functions:
            rms = LeastSquaresCalculator.calculate(x, y, func)
            if rms < best_fit:
                best_fit = rms
                best_func = func

        return best_func.name(), best_func

m = len(string1)
n = len(string2)
memo = [[-1 for _ in range(n + 1)] for _ in range(m + 1)]
print(LCS_Memo(string1, string2, m, n, memo))
print(LCS_Recursion(string1, string2, m, n))
print(LCS_Recursion(string1, string2, m, n))
print('Please use the complexity library')

