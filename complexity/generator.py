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
        pass
    def generate(self, size: int = 1) -> int:
        pass

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


class StringGenerator:
    def __init__(self, alphabet=['A', 'B', 'C']):
        """
        Initializes the StringGenerator with a given alphabet.
        :param alphabet: List of characters to use for generating strings.
        """
        self.alphabet = alphabet

    def generate(self, size=1):
        """
        Generates a random string of a given size using the alphabet.
        :param size: Length of the generated string.
        :return: Random string.
        """
        return ''.join(random.choices(self.alphabet, k=size))

    def generate_pair(self, m, n, similarity=0.5):
        """
        Generates a pair of strings with specified lengths and similarity.
        :param m: Length of the first string.
        :param n: Length of the second string.
        :param similarity: Proportion of shared characters (0 to 1).
        :return: Tuple of two strings.
        """
        # Generate a base string to introduce similarity
        base = self.generate(min(m, n))
        
        # Mutate the base string to generate the first string
        str1 = ''.join(
            random.choice(self.alphabet) if random.random() > similarity else char
            for char in base
        )
        
        # Mutate the base string to generate the second string
        str2 = ''.join(
            random.choice(self.alphabet) if random.random() > similarity else char
            for char in base
        )

        # Ensure lengths of the generated strings
        return str1[:m], str2[:n]
