from abc import ABC, abstractmethod
from typing import Any, List, Tuple
import random
import numpy as np
import networkx as nx

# Abstract Base Class for Data Generators
class SyntheticDataGenerator(ABC):
    @abstractmethod
    def create(self, size: int) -> Any:
        """Create synthetic data of a specified size."""
        pass

# Linear Data Generator
class SequentialData(SyntheticDataGenerator):
    def create(self, size: int) -> List[int]:
        return [i for i in range(1, size + 1)]

# Random Number Generator
class UniformRandomData(SyntheticDataGenerator):
    def __init__(self, min_val: int = 0, max_val: int = 100):
        self.min_val = min_val
        self.max_val = max_val

    def create(self, size: int) -> List[int]:
        return [random.randint(self.min_val, self.max_val) for _ in range(size)]

# Gaussian Data Generator
class NormalDistributedData(SyntheticDataGenerator):
    def __init__(self, mean: float = 0.0, std_dev: float = 1.0):
        self.mean = mean
        self.std_dev = std_dev

    def create(self, size: int) -> np.ndarray:
        return np.random.normal(self.mean, self.std_dev, size)

# Factory for Data Generators
class GeneratorFactory:
    def __init__(self):
        self.registry = {}

    def add_generator(self, key: str, generator: SyntheticDataGenerator):
        self.registry[key] = generator

    def get_generator(self, key: str) -> SyntheticDataGenerator:
        if key not in self.registry:
            raise ValueError(f"Generator with key '{key}' is not registered.")
        return self.registry[key]

# String Generator
class RandomStringGenerator:
    def __init__(self, charset: List[str] = ['A', 'B', 'C']):
        self.charset = charset

    def create(self, size: int) -> str:
        return ''.join(random.choice(self.charset) for _ in range(size))

    def create_pair(self, len1: int, len2: int, match_ratio: float = 0.0) -> Tuple[str, str]:
        if not (0.0 <= match_ratio <= 1.0):
            raise ValueError("Match ratio must be between 0.0 and 1.0")

        base = [random.choice(self.charset) for _ in range(min(len1, len2))]
        shared_count = int(len(base) * match_ratio)
        shared_indices = random.sample(range(len(base)), shared_count)

        for idx in shared_indices:
            base[idx] = random.choice(self.charset)

        str1 = ''.join(base[:len1]) + ''.join(random.choices(self.charset, k=(len1 - len(base))))
        str2 = ''.join(base[:len2]) + ''.join(random.choices(self.charset, k=(len2 - len(base))))

        return str1, str2

# Graph Generator
class RandomGraphGenerator(SyntheticDataGenerator):
    def __init__(self, directed: bool = False, weighted: bool = True):
        self.directed = directed
        self.weighted = weighted

    def create(self, size: int) -> nx.Graph:
        graph = nx.DiGraph() if self.directed else nx.Graph()

        for node in range(size):
            graph.add_node(node)

        for node1 in range(size):
            for node2 in range(node1 + 1, size):
                if random.random() < 0.3:
                    weight = random.randint(1, 10) if self.weighted else 1
                    graph.add_edge(node1, node2, weight=weight)

        return graph

def main():
    # Setting up the factory
    factory = GeneratorFactory()
    factory.add_generator("linear", SequentialData())
    factory.add_generator("random", UniformRandomData(0, 50))
    factory.add_generator("gaussian", NormalDistributedData(0, 1))
    factory.add_generator("graph", RandomGraphGenerator(directed=True, weighted=True))

    # Generate linear data
    linear_gen = factory.get_generator("linear")
    print("Linear Data:", linear_gen.create(10))

    # Generate random data
    random_gen = factory.get_generator("random")
    print("Random Data:", random_gen.create(10))

    # Generate Gaussian data
    gaussian_gen = factory.get_generator("gaussian")
    print("Gaussian Data:", gaussian_gen.create(10))

    # Generate graph
    graph_gen = factory.get_generator("graph")
    graph = graph_gen.create(5)
    print("Graph Edges:", graph.edges(data=True))

if __name__ == "__main__":
    main()
