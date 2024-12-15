from abc import ABC, abstractmethod
from typing import Any

import random
import numpy as np


import networkx as nx

class DataGenerator(ABC):
    @abstractmethod
    def generate(self, size: int) -> Any:
        """Generate synthetic data of the given size."""
        pass

class LinearDataGenerator(DataGenerator):
    def generate(self, size: int) -> list[int]:
        return list(range(1, size + 1))

class RandomDataGenerator(DataGenerator):
    def __init__(self, low: int = 0, high: int = 100):
        self.low = low
        self.high = high

    def generate(self, size: int) -> list[int]:
        return [random.randint(self.low, self.high) for _ in range(size)]

class GaussianDataGenerator(DataGenerator):
    def __init__(self, mean: float = 0, std: float = 1):
        self.mean = mean
        self.std = std

    def generate(self, size: int) -> np.ndarray:
        return np.random.normal(self.mean, self.std, size)

class DataGeneratorFactory:
    def __init__(self):
        self.generators = {}

    def register_generator(self, name: str, generator: DataGenerator):
        self.generators[name] = generator

    def get_generator(self, name: str) -> DataGenerator:
        if name not in self.generators:
            raise ValueError(f"Generator '{name}' not found.")
        return self.generators[name]

class NumberGenerator(DataGenerator):
    def __init__(self, low: int = 0, high: int = 100, fixed: int = None):
        self.low = low
        self.high = high
        self.fixed = fixed

    def generate(self, size: int = 1) -> int:
        if self.fixed is not None:
            return self.fixed
        return random.randint(self.low, self.high)


#TODO:add the string geneation logic
class StringGenerator(DataGenerator):
    def __init__(self,alphabit=['A','B','C']):
        self.alphabit = alphabit if alphabit else ['A', 'B', 'C']
    def generate(self, size: int = 1) -> int:
        return ''.join(random.choices(self.alphabit, k=size))
    def generate_pair(self, size1: int, size2: int, similarity: float = 0.5) -> tuple[str, str]:
        common_size = int(min(size1, size2) * similarity)


        common_part = ''.join(random.choices(self.alphabit, k=common_size))
        str1_unique = ''.join(random.choices(self.alphabit, k=size1 - common_size))
        str2_unique = ''.join(random.choices(self.alphabit, k=size2 - common_size))
        str1 = common_part + str1_unique
        str2 = common_part + str2_unique
        str1 = ''.join(random.sample(str1, len(str1)))
        str2 = ''.join(random.sample(str2, len(str2)))
        return str1, str2

class GraphGenerator(DataGenerator):
    def __init__(self, directed: bool = False, weighted: bool = True):
        self.directed = directed
        self.weighted = weighted

    def generate(self, size: int) -> nx.Graph:
        graph = nx.DiGraph() if self.directed else nx.Graph()

        # Create nodes
        for i in range(size):
            graph.add_node(i)

        # Create edges with random weights
        for i in range(size):
            for j in range(i + 1, size):
                if random.random() < 0.3:  # Sparsity control
                    weight = random.randint(1, 10) if self.weighted else 1
                    graph.add_edge(i, j, weight=weight)

        return graph



def main():
    # Factory setup
    factory = DataGeneratorFactory()
    factory.register_generator("linear", LinearDataGenerator())
    factory.register_generator("random", RandomDataGenerator(0, 50))
    factory.register_generator("gaussian", GaussianDataGenerator(0, 1))
    factory.register_generator("number", NumberGenerator(1, 100))
    factory.register_generator("graph", GraphGenerator(directed=True, weighted=True))

    # Generate a number
    number_generator = factory.get_generator("number")
    print(f"Generated Number: {number_generator.generate()}")

    # Generate a graph
    graph_generator = factory.get_generator("graph")
    graph = graph_generator.generate(5)
    print("Generated Graph:")
    print(graph.edges(data=True))  # Print edges with weights

if __name__ == "__main__":
    main()

