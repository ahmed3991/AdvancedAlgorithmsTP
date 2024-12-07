from abc import ABC, abstractmethod
import numpy as np

from typing import List

class ComplexityFunction(ABC):
    @abstractmethod
    def evaluate(self, x: np.ndarray) -> np.ndarray:
        """Evaluate the complexity function for input x."""
        pass

    @abstractmethod
    def name(self) -> str:
        """Return the name of the complexity function."""
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

class LeastSquaresCalculator:
    @staticmethod
    def calculate(x: np.ndarray, y: np.ndarray, complexity_func: ComplexityFunction) -> float:
        sigma_gn_squared = complexity_func.evaluate(x) ** 2
        sigma_gn_y = complexity_func.evaluate(x) * y
        coef = sigma_gn_y.sum() / sigma_gn_squared.sum()
        rms = np.sqrt(((y - coef * complexity_func.evaluate(x)) ** 2).mean()) / y.mean()
        return rms


class ComplexityAnalyzer:
    def __init__(self, complexity_functions: List[ComplexityFunction] = None):
        """
        Initialize the complexity analyzer.
        :param complexity_functions: Optional list of complexity functions. If None, uses defaults.
        """
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
        """
        Determine the best-fitting complexity function based on the provided data.
        :param x: Input sizes.
        :param y: Measured times or space values.
        :return: Name of the best-fitting complexity function.
        """
        best_fit = float("inf")
        best_func = None

        for func in self.complexity_functions:
            rms = LeastSquaresCalculator.calculate(x, y, func)
            if rms < best_fit:
                best_fit = rms
                best_func = func

        return best_func.name(), best_func
