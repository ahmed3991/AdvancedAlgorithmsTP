from abc import ABC, abstractmethod
from typing import Any
import random
import numpy as np
import networkx as nx


# Abstract Base Class for Data Generators
class DataProducer(ABC):
    @abstractmethod
    def produce(self, size: int) -> Any:
        """Generate synthetic data of the given size."""
        pass

# Linear Data Producer
class LinearDataProducer(DataProducer):
    def produce(self, size: int) -> list[int]:
        return list(range(1, size + 1))

# Random Data Producer
class RandomDataProducer(DataProducer):
    def initialize(self, low: int = 0, high: int = 100):
        self.low = low
        self.high = high

    def produce(self, size: int) -> list[int]:
        return [random.randint(self.low, self.high) for _ in range(size)]

# Gaussian Data Producer
class GaussianDataProducer(DataProducer):
    def initialize(self, mean: float = 0, std: float = 1):
        self.mean = mean
        self.std = std

    def produce(self, size: int) -> np.ndarray:
        return np.random.normal(self.mean, self.std, size)

# Factory for Data Producers
class DataProducerFactory:
    def initialize(self):
        self.producers = {}

    def register_producer(self, name: str, producer: DataProducer):
        self.producers[name] = producer

    def get_producer(self, name: str) -> DataProducer:
        if name not in self.producers:
            raise ValueError(f"Producer '{name}' not found.")
        return self.producers[name]

# Integer Producer
class IntegerProducer(DataProducer):
    def initialize(self, low: int = 0, high: int = 100, fixed: int = None):
        self.low = low
        self.high = high
        self.fixed = fixed

    def produce(self, size: int = 1) -> int:
        if self.fixed is not None:
            return self.fixed
        return random.randint(self.low, self.high)

# String Producer
class StringProducer(DataProducer):
    def initialize(self, alphabet=['A', 'B', 'C']):
        self.alphabet = alphabet

    def produce(self, size: int = 1) -> str:
        return ''.join(random.choices(self.alphabet, k=size))

# Graph Producer
class GraphProducer(DataProducer):
    def initialize(self, directed: bool = False, weighted: bool = True):
        self.directed = directed
        self.weighted = weighted

    def produce(self, size: int) -> nx.Graph:
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

# Main function for testing
def main():
    # Factory setup
    factory = DataProducerFactory()
    factory.register_producer("linear", LinearDataProducer())
    factory.register_producer("random", RandomDataProducer(0, 50))
    factory.register_producer("gaussian", GaussianDataProducer(0, 1))
    factory.register_producer("integer", IntegerProducer(1, 100))
    factory.register_producer("graph", GraphProducer(directed=True, weighted=True))
    factory.register_producer("string", StringProducer(['A', 'C', 'G', 'T']))

    # Generate a number
    integer_producer = factory.get_producer("integer")
    print(f"Generated Integer: {integer_producer.produce()}")

    # Generate a graph
    graph_producer = factory.get_producer("graph")
    graph = graph_producer.produce(5)
    print("Generated Graph:")
    print(graph.edges(data=True))  # Print edges with weights

    # Generate a string
    string_producer = factory.get_producer("string")
    random_string = string_producer.produce(10)
    print(f"Generated String: {random_string}")

if __name__ == "__main__":
    main()
